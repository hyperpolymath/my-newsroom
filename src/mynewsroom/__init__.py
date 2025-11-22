"""
My-newsroom: Epistemic Programming for Neurosymbolic Journalism

A research project exploring belief fusion, multi-agent systems, and
formal uncertainty quantification for fact-checking and verification.
"""

__version__ = "0.1.0-alpha"
__author__ = "My-newsroom Contributors"
__license__ = "MIT OR Palimpsest-0.8"

from mynewsroom.dempster_shafer import (
    BeliefMass,
    Frame,
    FusionRule,
    fuse_beliefs,
    calculate_conflict,
)

__all__ = [
    "BeliefMass",
    "Frame",
    "FusionRule",
    "fuse_beliefs",
    "calculate_conflict",
]
