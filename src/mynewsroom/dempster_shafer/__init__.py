"""
Dempster-Shafer Theory of Evidence Implementation

This module provides a complete implementation of Dempster-Shafer belief fusion,
including multiple combination rules and conflict handling.

References:
    - Shafer, G. (1976). A Mathematical Theory of Evidence.
    - Smets, P. (1990). The Combination of Evidence in the Transferable Belief Model.
"""

from mynewsroom.dempster_shafer.core import (
    Frame,
    BeliefMass,
    FusionRule,
    fuse_beliefs,
    calculate_conflict,
    calculate_belief,
    calculate_plausibility,
)

__all__ = [
    "Frame",
    "BeliefMass",
    "FusionRule",
    "fuse_beliefs",
    "calculate_conflict",
    "calculate_belief",
    "calculate_plausibility",
]
