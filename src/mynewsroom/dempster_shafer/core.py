"""
Core Dempster-Shafer implementation with multiple fusion rules.
"""

from __future__ import annotations
from typing import Dict, Set, FrozenSet, Optional, Union
from enum import Enum
from dataclasses import dataclass, field
import warnings
from itertools import combinations


class FusionRule(Enum):
    """Available belief fusion rules."""
    DEMPSTER = "dempster"
    YAGER = "yager"
    DUBOIS_PRADE = "dubois_prade"
    AVERAGE = "average"


# Type alias for frames of discernment
Frame = FrozenSet[str]


@dataclass
class BeliefMass:
    """
    Belief mass function (basic probability assignment) over a frame of discernment.

    A belief mass assigns probability mass to subsets of a frame Θ, representing
    different levels of certainty about which element(s) of Θ are true.

    Attributes:
        masses: Dictionary mapping focal sets (subsets of Θ) to probability masses
        frame: The frame of discernment (universal set)
        epsilon: Tolerance for floating-point comparisons

    Examples:
        >>> theta = frozenset({"true", "false"})
        >>> m = BeliefMass({
        ...     frozenset({"true"}): 0.7,
        ...     theta: 0.3  # Uncertainty
        ... })
        >>> m.is_valid()
        True
    """

    masses: Dict[Frame, float] = field(default_factory=dict)
    frame: Optional[Frame] = None
    epsilon: float = 1e-6

    def __post_init__(self):
        """Validate and normalize the belief mass function."""
        if not self.masses:
            raise ValueError("Belief mass cannot be empty")

        # Infer frame from masses if not provided
        if self.frame is None:
            all_elements = set()
            for focal_set in self.masses.keys():
                all_elements.update(focal_set)
            self.frame = frozenset(all_elements)

        # Validate masses
        for focal_set, mass in self.masses.items():
            if not isinstance(focal_set, frozenset):
                raise TypeError(f"Focal sets must be frozensets, got {type(focal_set)}")
            if not (0.0 <= mass <= 1.0 + self.epsilon):
                raise ValueError(f"Mass {mass} out of range [0, 1]")
            if not focal_set.issubset(self.frame):
                raise ValueError(f"Focal set {focal_set} not in frame {self.frame}")

        # Normalize if sum is close to 1.0 but not exact
        total = sum(self.masses.values())
        if abs(total - 1.0) > self.epsilon:
            raise ValueError(f"Masses sum to {total}, must sum to 1.0 (±{self.epsilon})")

        # Exact normalization to fix floating-point errors
        if abs(total - 1.0) < self.epsilon and total != 1.0:
            factor = 1.0 / total
            self.masses = {k: v * factor for k, v in self.masses.items()}

    def is_valid(self) -> bool:
        """Check if this is a valid belief mass function."""
        try:
            total = sum(self.masses.values())
            return abs(total - 1.0) < self.epsilon
        except:
            return False

    def belief(self, proposition: Frame) -> float:
        """
        Calculate the belief (lower probability) in a proposition.

        Bel(A) = Σ m(B) for all B ⊆ A

        Args:
            proposition: The proposition to calculate belief for

        Returns:
            Belief value in [0, 1]
        """
        return sum(
            mass for focal_set, mass in self.masses.items()
            if focal_set.issubset(proposition)
        )

    def plausibility(self, proposition: Frame) -> float:
        """
        Calculate the plausibility (upper probability) in a proposition.

        Pl(A) = Σ m(B) for all B ∩ A ≠ ∅

        Args:
            proposition: The proposition to calculate plausibility for

        Returns:
            Plausibility value in [0, 1]
        """
        return sum(
            mass for focal_set, mass in self.masses.items()
            if not focal_set.isdisjoint(proposition)
        )

    def uncertainty_interval(self, proposition: Frame) -> tuple[float, float]:
        """
        Get the uncertainty interval [Bel(A), Pl(A)] for a proposition.

        Args:
            proposition: The proposition

        Returns:
            Tuple of (belief, plausibility)
        """
        return (self.belief(proposition), self.plausibility(proposition))

    def __getitem__(self, key: Union[Frame, str]) -> float:
        """Get mass for a focal set or singleton element."""
        if isinstance(key, str):
            key = frozenset({key})
        return self.masses.get(key, 0.0)

    def __repr__(self) -> str:
        items = ", ".join(f"{set(k)}: {v:.4f}" for k, v in self.masses.items())
        return f"BeliefMass({{{items}}})"


def calculate_conflict(m1: BeliefMass, m2: BeliefMass) -> float:
    """
    Calculate the conflict between two belief masses.

    K = Σ m₁(A) · m₂(B) for all A ∩ B = ∅

    Args:
        m1: First belief mass
        m2: Second belief mass

    Returns:
        Conflict value in [0, 1]
    """
    if m1.frame != m2.frame:
        raise ValueError(f"Incompatible frames: {m1.frame} vs {m2.frame}")

    conflict = 0.0
    for set_a, mass_a in m1.masses.items():
        for set_b, mass_b in m2.masses.items():
            if set_a.isdisjoint(set_b):
                conflict += mass_a * mass_b

    return conflict


def fuse_dempster(m1: BeliefMass, m2: BeliefMass) -> BeliefMass:
    """
    Dempster's rule of combination.

    Normalizes by dividing by (1 - K) where K is the conflict mass.
    Requires K < 1 (not total conflict).

    Args:
        m1: First belief mass
        m2: Second belief mass

    Returns:
        Combined belief mass

    Raises:
        ValueError: If conflict = 1.0 (total contradiction)
    """
    conflict = calculate_conflict(m1, m2)

    if conflict >= 1.0 - m1.epsilon:
        raise ValueError(
            f"Total conflict (K={conflict:.4f}). Cannot use Dempster's rule. "
            "Consider Yager's rule or Dubois-Prade rule instead."
        )

    if conflict >= 0.9:
        warnings.warn(
            f"High conflict (K={conflict:.4f}). Result may be unreliable. "
            "Consider examining sources or using alternative fusion rule.",
            UserWarning
        )

    # Compute conjunctive combination
    combined: Dict[Frame, float] = {}

    for set_a, mass_a in m1.masses.items():
        for set_b, mass_b in m2.masses.items():
            intersection = set_a & set_b
            if intersection:  # Non-empty intersection
                combined[intersection] = combined.get(intersection, 0.0) + mass_a * mass_b

    # Normalize by (1 - K)
    normalization = 1.0 - conflict
    normalized = {k: v / normalization for k, v in combined.items()}

    return BeliefMass(masses=normalized, frame=m1.frame)


def fuse_yager(m1: BeliefMass, m2: BeliefMass) -> BeliefMass:
    """
    Yager's rule of combination.

    Assigns all conflicting mass to the frame (ignorance) instead of normalizing.
    More cautious than Dempster's rule.

    Args:
        m1: First belief mass
        m2: Second belief mass

    Returns:
        Combined belief mass
    """
    conflict = calculate_conflict(m1, m2)

    # Compute conjunctive combination
    combined: Dict[Frame, float] = {}

    for set_a, mass_a in m1.masses.items():
        for set_b, mass_b in m2.masses.items():
            intersection = set_a & set_b
            if intersection:  # Non-empty intersection
                combined[intersection] = combined.get(intersection, 0.0) + mass_a * mass_b

    # Add conflict mass to frame (ignorance)
    if conflict > m1.epsilon:
        combined[m1.frame] = combined.get(m1.frame, 0.0) + conflict

    return BeliefMass(masses=combined, frame=m1.frame)


def fuse_dubois_prade(m1: BeliefMass, m2: BeliefMass) -> BeliefMass:
    """
    Dubois-Prade rule of combination.

    Redistributes conflicting mass to the union of conflicting sets.

    Args:
        m1: First belief mass
        m2: Second belief mass

    Returns:
        Combined belief mass
    """
    combined: Dict[Frame, float] = {}

    for set_a, mass_a in m1.masses.items():
        for set_b, mass_b in m2.masses.items():
            intersection = set_a & set_b
            product = mass_a * mass_b

            if intersection:  # Non-empty intersection
                combined[intersection] = combined.get(intersection, 0.0) + product
            else:  # Conflict: assign to union
                union = set_a | set_b
                combined[union] = combined.get(union, 0.0) + product

    return BeliefMass(masses=combined, frame=m1.frame)


def fuse_average(m1: BeliefMass, m2: BeliefMass) -> BeliefMass:
    """
    Simple averaging rule (not a proper Dempster-Shafer rule).

    Just averages the masses. Useful as a baseline.

    Args:
        m1: First belief mass
        m2: Second belief mass

    Returns:
        Averaged belief mass
    """
    all_sets = set(m1.masses.keys()) | set(m2.masses.keys())
    averaged = {}

    for focal_set in all_sets:
        mass_a = m1.masses.get(focal_set, 0.0)
        mass_b = m2.masses.get(focal_set, 0.0)
        averaged[focal_set] = (mass_a + mass_b) / 2.0

    return BeliefMass(masses=averaged, frame=m1.frame)


def fuse_beliefs(
    m1: BeliefMass,
    m2: BeliefMass,
    rule: FusionRule = FusionRule.DEMPSTER
) -> BeliefMass:
    """
    Fuse two belief masses using the specified rule.

    Args:
        m1: First belief mass
        m2: Second belief mass
        rule: Fusion rule to use

    Returns:
        Combined belief mass

    Raises:
        ValueError: If frames are incompatible or rule fails
    """
    if m1.frame != m2.frame:
        raise ValueError(
            f"Incompatible frames of discernment: {m1.frame} vs {m2.frame}"
        )

    fusion_functions = {
        FusionRule.DEMPSTER: fuse_dempster,
        FusionRule.YAGER: fuse_yager,
        FusionRule.DUBOIS_PRADE: fuse_dubois_prade,
        FusionRule.AVERAGE: fuse_average,
    }

    fusion_fn = fusion_functions[rule]
    return fusion_fn(m1, m2)


def calculate_belief(m: BeliefMass, proposition: Frame) -> float:
    """Calculate belief (convenience function)."""
    return m.belief(proposition)


def calculate_plausibility(m: BeliefMass, proposition: Frame) -> float:
    """Calculate plausibility (convenience function)."""
    return m.plausibility(proposition)


def fuse_multiple(
    masses: list[BeliefMass],
    rule: FusionRule = FusionRule.DEMPSTER
) -> BeliefMass:
    """
    Fuse multiple belief masses iteratively.

    Args:
        masses: List of belief masses to fuse
        rule: Fusion rule to use

    Returns:
        Combined belief mass

    Raises:
        ValueError: If list is empty or masses are incompatible
    """
    if not masses:
        raise ValueError("Cannot fuse empty list of belief masses")

    if len(masses) == 1:
        return masses[0]

    result = masses[0]
    for m in masses[1:]:
        result = fuse_beliefs(result, m, rule=rule)

    return result
