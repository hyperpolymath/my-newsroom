"""
Comprehensive unit tests for Dempster-Shafer implementation.

Test coverage includes:
- BeliefMass creation and validation
- All fusion rules (Dempster, Yager, Dubois-Prade, Average)
- Conflict calculation
- Belief and plausibility calculations
- Edge cases and error handling
"""

import pytest
import warnings
from mynewsroom.dempster_shafer import (
    BeliefMass,
    FusionRule,
    fuse_beliefs,
    calculate_conflict,
    fuse_multiple,
)


class TestBeliefMassCreation:
    """Test BeliefMass initialization and validation."""

    def test_simple_belief_mass(self):
        """Test creating a simple belief mass."""
        theta = frozenset({"true", "false"})
        m = BeliefMass({
            frozenset({"true"}): 0.7,
            theta: 0.3
        })
        assert m.is_valid()
        assert abs(sum(m.masses.values()) - 1.0) < 1e-6

    def test_frame_inference(self):
        """Test automatic frame inference from masses."""
        m = BeliefMass({
            frozenset({"A"}): 0.5,
            frozenset({"B"}): 0.3,
            frozenset({"A", "B"}): 0.2
        })
        assert m.frame == frozenset({"A", "B"})

    def test_normalization(self):
        """Test that masses sum to 1.0."""
        m = BeliefMass({
            frozenset({"A"}): 0.5,
            frozenset({"B"}): 0.5
        })
        assert abs(sum(m.masses.values()) - 1.0) < 1e-6

    def test_invalid_mass_range(self):
        """Test that masses must be in [0, 1]."""
        with pytest.raises(ValueError, match="out of range"):
            BeliefMass({
                frozenset({"A"}): 1.5,  # Invalid: > 1.0
            })

    def test_invalid_sum(self):
        """Test that masses must sum to 1.0."""
        with pytest.raises(ValueError, match="must sum to 1.0"):
            BeliefMass({
                frozenset({"A"}): 0.5,
                frozenset({"B"}): 0.3,  # Sum = 0.8, not 1.0
            })

    def test_empty_masses(self):
        """Test that empty masses are rejected."""
        with pytest.raises(ValueError, match="cannot be empty"):
            BeliefMass({})


class TestBeliefPlausibility:
    """Test belief and plausibility calculations."""

    def test_belief_calculation(self):
        """Test belief (lower probability) calculation."""
        theta = frozenset({"A", "B", "C"})
        m = BeliefMass({
            frozenset({"A"}): 0.4,
            frozenset({"B"}): 0.3,
            frozenset({"A", "B"}): 0.2,
            theta: 0.1
        })

        # Bel({A, B}) = m({A}) + m({B}) + m({A, B})
        assert abs(m.belief(frozenset({"A", "B"})) - 0.9) < 1e-6

        # Bel({A}) = m({A})
        assert abs(m.belief(frozenset({"A"})) - 0.4) < 1e-6

    def test_plausibility_calculation(self):
        """Test plausibility (upper probability) calculation."""
        theta = frozenset({"A", "B", "C"})
        m = BeliefMass({
            frozenset({"A"}): 0.4,
            frozenset({"B"}): 0.3,
            frozenset({"A", "B"}): 0.2,
            theta: 0.1
        })

        # Pl({A}) = m({A}) + m({A, B}) + m(θ) = 0.4 + 0.2 + 0.1
        assert abs(m.plausibility(frozenset({"A"})) - 0.7) < 1e-6

        # Pl({A, B}) = all masses (everything intersects {A, B})
        assert abs(m.plausibility(frozenset({"A", "B"})) - 1.0) < 1e-6

    def test_uncertainty_interval(self):
        """Test [Bel, Pl] uncertainty interval."""
        m = BeliefMass({
            frozenset({"A"}): 0.5,
            frozenset({"B"}): 0.3,
            frozenset({"A", "B"}): 0.2
        })

        bel, pl = m.uncertainty_interval(frozenset({"A"}))
        assert abs(bel - 0.5) < 1e-6  # Bel({A})
        assert abs(pl - 0.7) < 1e-6   # Pl({A})

        # Bel(A) <= Pl(A) must always hold
        assert bel <= pl


class TestConflictCalculation:
    """Test conflict measurement between belief masses."""

    def test_zero_conflict(self):
        """Test case with no conflict."""
        m1 = BeliefMass({
            frozenset({"A"}): 0.7,
            frozenset({"A", "B"}): 0.3
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.5,
            frozenset({"A", "B"}): 0.5
        })

        # No disjoint sets, so K = 0
        conflict = calculate_conflict(m1, m2)
        assert abs(conflict - 0.0) < 1e-6

    def test_partial_conflict(self):
        """Test case with partial conflict."""
        m1 = BeliefMass({
            frozenset({"A"}): 0.8,
            frozenset({"B"}): 0.2
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.6,
            frozenset({"B"}): 0.4
        })

        # K = m1(A)·m2(B) + m1(B)·m2(A) = 0.8·0.4 + 0.2·0.6 = 0.44
        conflict = calculate_conflict(m1, m2)
        assert abs(conflict - 0.44) < 1e-6

    def test_total_conflict(self):
        """Test case with total conflict."""
        m1 = BeliefMass({
            frozenset({"A"}): 1.0
        })
        m2 = BeliefMass({
            frozenset({"B"}): 1.0
        })

        # K = 1.0 (complete contradiction)
        conflict = calculate_conflict(m1, m2)
        assert abs(conflict - 1.0) < 1e-6

    def test_incompatible_frames(self):
        """Test that incompatible frames are rejected."""
        m1 = BeliefMass({frozenset({"A"}): 1.0})
        m2 = BeliefMass({frozenset({"X"}): 1.0})

        with pytest.raises(ValueError, match="Incompatible frames"):
            calculate_conflict(m1, m2)


class TestDempsterRule:
    """Test Dempster's rule of combination."""

    def test_basic_combination(self):
        """Test basic Dempster combination."""
        theta = frozenset({"A", "B"})
        m1 = BeliefMass({
            frozenset({"A"}): 0.7,
            theta: 0.3
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.5,
            theta: 0.5
        })

        result = fuse_beliefs(m1, m2, rule=FusionRule.DEMPSTER)

        # After combination, belief in A should increase
        assert result[frozenset({"A"})] > 0.7
        assert result.is_valid()

    def test_normalization_with_conflict(self):
        """Test that Dempster rule normalizes by (1 - K)."""
        m1 = BeliefMass({
            frozenset({"A"}): 0.9,
            frozenset({"B"}): 0.1
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.1,
            frozenset({"B"}): 0.9
        })

        # K = 0.9·0.9 + 0.1·0.1 = 0.82
        # m₁₂({A}) = (0.9·0.1) / (1 - 0.82) = 0.09 / 0.18 = 0.5
        # m₁₂({B}) = (0.1·0.9) / (1 - 0.82) = 0.09 / 0.18 = 0.5

        result = fuse_beliefs(m1, m2, rule=FusionRule.DEMPSTER)

        assert abs(result[frozenset({"A"})] - 0.5) < 1e-6
        assert abs(result[frozenset({"B"})] - 0.5) < 1e-6

    def test_total_conflict_raises(self):
        """Test that total conflict raises exception."""
        m1 = BeliefMass({frozenset({"A"}): 1.0})
        m2 = BeliefMass({frozenset({"B"}): 1.0})

        with pytest.raises(ValueError, match="Total conflict"):
            fuse_beliefs(m1, m2, rule=FusionRule.DEMPSTER)

    def test_high_conflict_warning(self):
        """Test that high conflict triggers warning."""
        m1 = BeliefMass({
            frozenset({"A"}): 0.95,
            frozenset({"B"}): 0.05
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.05,
            frozenset({"B"}): 0.95
        })

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = fuse_beliefs(m1, m2, rule=FusionRule.DEMPSTER)

            assert len(w) == 1
            assert "High conflict" in str(w[0].message)


class TestYagerRule:
    """Test Yager's rule of combination."""

    def test_conflict_to_ignorance(self):
        """Test that Yager assigns conflict to ignorance."""
        theta = frozenset({"A", "B"})
        m1 = BeliefMass({
            frozenset({"A"}): 0.8,
            frozenset({"B"}): 0.2
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.3,
            frozenset({"B"}): 0.7
        })

        result = fuse_beliefs(m1, m2, rule=FusionRule.YAGER)

        # Conflict mass should be assigned to theta
        conflict = calculate_conflict(m1, m2)
        assert abs(result[theta] - conflict) < 1e-6
        assert result.is_valid()

    def test_total_conflict_handled(self):
        """Test that Yager handles total conflict gracefully."""
        theta = frozenset({"A", "B"})
        m1 = BeliefMass({frozenset({"A"}): 1.0})
        m2 = BeliefMass({frozenset({"B"}): 1.0})

        # Yager should not raise, assigns all mass to theta
        result = fuse_beliefs(m1, m2, rule=FusionRule.YAGER)
        assert abs(result[theta] - 1.0) < 1e-6


class TestDuboisPradeRule:
    """Test Dubois-Prade rule of combination."""

    def test_conflict_to_union(self):
        """Test that Dubois-Prade assigns conflict to union."""
        theta = frozenset({"A", "B"})
        m1 = BeliefMass({
            frozenset({"A"}): 0.8,
            frozenset({"B"}): 0.2
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.3,
            frozenset({"B"}): 0.7
        })

        result = fuse_beliefs(m1, m2, rule=FusionRule.DUBOIS_PRADE)

        # Conflicting mass goes to A ∪ B = theta
        assert result[theta] > 0
        assert result.is_valid()


class TestAverageRule:
    """Test simple averaging rule."""

    def test_basic_average(self):
        """Test basic averaging of belief masses."""
        m1 = BeliefMass({
            frozenset({"A"}): 0.8,
            frozenset({"B"}): 0.2
        })
        m2 = BeliefMass({
            frozenset({"A"}): 0.6,
            frozenset({"B"}): 0.4
        })

        result = fuse_beliefs(m1, m2, rule=FusionRule.AVERAGE)

        # Average of A: (0.8 + 0.6) / 2 = 0.7
        assert abs(result[frozenset({"A"})] - 0.7) < 1e-6
        # Average of B: (0.2 + 0.4) / 2 = 0.3
        assert abs(result[frozenset({"B"})] - 0.3) < 1e-6


class TestMultipleFusion:
    """Test fusing multiple belief masses."""

    def test_three_way_fusion(self):
        """Test fusing three belief masses."""
        theta = frozenset({"A", "B"})
        masses = [
            BeliefMass({frozenset({"A"}): 0.6, theta: 0.4}),
            BeliefMass({frozenset({"A"}): 0.7, theta: 0.3}),
            BeliefMass({frozenset({"A"}): 0.8, theta: 0.2}),
        ]

        result = fuse_multiple(masses, rule=FusionRule.DEMPSTER)

        # All evidence points to A, so belief should be very high
        assert result[frozenset({"A"})] > 0.9
        assert result.is_valid()

    def test_empty_list_raises(self):
        """Test that empty list raises exception."""
        with pytest.raises(ValueError, match="empty list"):
            fuse_multiple([])

    def test_single_mass_returns_unchanged(self):
        """Test that single mass is returned unchanged."""
        m = BeliefMass({frozenset({"A"}): 0.7, frozenset({"B"}): 0.3})
        result = fuse_multiple([m])
        assert result is m


class TestRealWorldScenarios:
    """Test realistic journalism use cases."""

    def test_source_credibility_fusion(self):
        """Test fusing beliefs from sources with different credibility."""
        claim = frozenset({"true", "false"})

        # Source A (high credibility): 90% believe claim is true
        source_a = BeliefMass({
            frozenset({"true"}): 0.9,
            claim: 0.1
        })

        # Source B (medium credibility): 70% believe claim is true
        source_b = BeliefMass({
            frozenset({"true"}): 0.7,
            claim: 0.3
        })

        # Source C (skeptical): 40% believe, 40% disbelieve
        source_c = BeliefMass({
            frozenset({"true"}): 0.4,
            frozenset({"false"}): 0.4,
            claim: 0.2
        })

        # Fuse all three
        result = fuse_multiple([source_a, source_b, source_c], FusionRule.DEMPSTER)

        # Strong evidence from A and B should outweigh C's skepticism
        assert result[frozenset({"true"})] > 0.7
        assert result.is_valid()

    def test_conflicting_eyewitnesses(self):
        """Test handling conflicting eyewitness reports."""
        suspects = frozenset({"Alice", "Bob", "Charlie"})

        # Witness 1: Saw Alice (80% certain)
        witness_1 = BeliefMass({
            frozenset({"Alice"}): 0.8,
            suspects: 0.2
        })

        # Witness 2: Saw Bob (70% certain)
        witness_2 = BeliefMass({
            frozenset({"Bob"}): 0.7,
            suspects: 0.3
        })

        # High conflict expected, use Yager rule
        result = fuse_beliefs(witness_1, witness_2, rule=FusionRule.YAGER)

        # Most mass should go to ignorance due to conflict
        assert result[suspects] > 0.5
        assert result.is_valid()


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_vacuous_belief(self):
        """Test belief mass that assigns all mass to frame (total ignorance)."""
        theta = frozenset({"A", "B", "C"})
        m_ignorance = BeliefMass({theta: 1.0})

        m_informative = BeliefMass({
            frozenset({"A"}): 0.6,
            theta: 0.4
        })

        # Fusing with ignorance should leave informative mass unchanged
        result = fuse_beliefs(m_ignorance, m_informative, FusionRule.DEMPSTER)
        assert abs(result[frozenset({"A"})] - 0.6) < 1e-6

    def test_singleton_frame(self):
        """Test degenerate case with only one element in frame."""
        m = BeliefMass({frozenset({"A"}): 1.0})
        assert m.is_valid()
        assert m.frame == frozenset({"A"})

    def test_floating_point_precision(self):
        """Test that floating-point errors don't break validation."""
        # Masses that sum to 0.9999999999 (close to 1.0)
        m = BeliefMass({
            frozenset({"A"}): 0.333333333,
            frozenset({"B"}): 0.333333333,
            frozenset({"C"}): 0.333333334,
        })
        assert m.is_valid()

    def test_associativity(self):
        """Test that fusion is associative: (A⊕B)⊕C = A⊕(B⊕C)."""
        theta = frozenset({"X", "Y"})
        m1 = BeliefMass({frozenset({"X"}): 0.6, theta: 0.4})
        m2 = BeliefMass({frozenset({"X"}): 0.7, theta: 0.3})
        m3 = BeliefMass({frozenset({"X"}): 0.8, theta: 0.2})

        # (m1 ⊕ m2) ⊕ m3
        left = fuse_beliefs(fuse_beliefs(m1, m2, FusionRule.DEMPSTER), m3, FusionRule.DEMPSTER)

        # m1 ⊕ (m2 ⊕ m3)
        right = fuse_beliefs(m1, fuse_beliefs(m2, m3, FusionRule.DEMPSTER), FusionRule.DEMPSTER)

        # Should be equal (within floating-point tolerance)
        assert abs(left[frozenset({"X"})] - right[frozenset({"X"})]) < 1e-6

    def test_commutativity(self):
        """Test that fusion is commutative: A⊕B = B⊕A."""
        m1 = BeliefMass({frozenset({"A"}): 0.7, frozenset({"B"}): 0.3})
        m2 = BeliefMass({frozenset({"A"}): 0.4, frozenset({"B"}): 0.6})

        result_12 = fuse_beliefs(m1, m2, FusionRule.DEMPSTER)
        result_21 = fuse_beliefs(m2, m1, FusionRule.DEMPSTER)

        assert abs(result_12[frozenset({"A"})] - result_21[frozenset({"A"})]) < 1e-6
        assert abs(result_12[frozenset({"B"})] - result_21[frozenset({"B"})]) < 1e-6


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
