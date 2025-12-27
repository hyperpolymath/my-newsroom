# Academic Papers

**Status:** Outlines Complete | Drafts In Progress
**Target Venues:** ICSE, PLDI, CHI, Middleware, CHASE
**Timeline:** Submissions 2025-2026

---

## Overview

This document outlines 5 academic papers planned for the My-newsroom project, covering epistemic programming languages, formal verification, and neurosymbolic AI for journalism.

---

## Paper 1: Rhodium Standard Repository Framework

**Target:** ICSE 2026 (Software Engineering Practice Track)
**Length:** 12 pages
**Status:** Outline complete

### Abstract

We present the Rhodium Standard Repository (RSR) framework, a comprehensive set of guidelines for creating politically autonomous, offline-first software repositories. RSR addresses the growing concern of vendor lock-in and cloud dependency in modern software development by establishing standards for repository structure, governance, security, and sustainability.

### Key Contributions

1. **RSR Specification** - Formal requirements for repository compliance
2. **TPCF Governance** - Tri-Perimeter Contribution Framework for graduated trust
3. **Offline-First Patterns** - Architecture patterns for air-gapped operation
4. **Case Study** - My-newsroom as reference implementation

### Outline

1. Introduction: The Problem of Vendor Lock-in
2. Background: Existing Standards (CHAOSS, CII Best Practices)
3. RSR Framework Design
   - Repository Structure Requirements
   - Security Standards (RFC 9116, threat modeling)
   - Governance Model (TPCF)
4. Implementation: My-newsroom Case Study
5. Evaluation: Compliance Metrics
6. Discussion: Adoption Challenges
7. Related Work
8. Conclusion

### Target Reviewers

- Software engineering practitioners
- Open source maintainers
- DevSecOps engineers

---

## Paper 2: TPCF - A Graduated Trust Model for Open Source

**Target:** CHI 2026 (Human Factors Track)
**Length:** 10 pages
**Status:** Outline complete

### Abstract

The Tri-Perimeter Contribution Framework (TPCF) introduces a graduated trust model for open source projects, balancing openness with security through three concentric contribution zones. We present empirical evidence from deploying TPCF in the My-newsroom project and analyze its effects on contributor behavior, code quality, and security incidents.

### Key Contributions

1. **Perimeter Model** - Formal definition of 3-tier access control
2. **Trust Graduation** - Mechanisms for contributors to advance
3. **Empirical Study** - Deployment in real project with metrics
4. **UX Guidelines** - How to communicate perimeters to contributors

### Outline

1. Introduction: Trust in Open Source
2. Background: Existing Governance Models
3. TPCF Design
   - Perimeter 1: Core Maintainers
   - Perimeter 2: Verified Contributors
   - Perimeter 3: Community Sandbox
4. Trust Graduation Mechanisms
5. Implementation
6. Evaluation: Contributor Study (N=50+)
7. Discussion
8. Conclusion

---

## Paper 3: CRDTs for Offline-First Epistemic Systems

**Target:** Middleware 2026
**Length:** 12 pages
**Status:** Outline complete

### Abstract

We present a novel application of Conflict-free Replicated Data Types (CRDTs) to epistemic programming systems, enabling distributed belief fusion without coordination. Our approach allows multiple agents to update belief states offline and merge consistently when connectivity is restored, with formal guarantees of eventual consistency.

### Key Contributions

1. **Belief CRDTs** - CRDT variants for Dempster-Shafer belief masses
2. **Fusion Commutativity** - Proof that D-S fusion is CRDT-compatible
3. **Offline Protocol** - Sync protocol for air-gapped agents
4. **Performance** - Benchmarks on 100-agent newsroom simulation

### Outline

1. Introduction: Distributed Belief Systems
2. Background: CRDTs, Dempster-Shafer Theory
3. Belief Mass CRDTs
   - Definition and Properties
   - Commutativity Proof
4. Epistemic Ledger Design
5. Implementation in Ensemble Dialect
6. Evaluation
7. Related Work
8. Conclusion

---

## Paper 4: iSOS - Multi-Language Verification Pipeline

**Target:** PLDI 2026
**Length:** 12 pages
**Status:** Outline complete

### Abstract

We introduce iSOS (Integrated System of Systems), a multi-language verification pipeline that enables gradual formalization from prototype to production. iSOS supports a spectrum from dynamically-typed prototypes (Me dialect) through memory-safe systems code (Solo) to formally verified implementations (Duet), with type information flowing across language boundaries.

### Key Contributions

1. **Dialect Pipeline** - Formal semantics of Me → Solo → Duet translation
2. **Type Export** - Cross-language type preservation
3. **Incremental Verification** - Verify critical paths first
4. **Synthesis Integration** - AI-assisted code generation with proofs

### Outline

1. Introduction: The Verification Gap
2. Background: Gradual Typing, Formal Methods
3. My Language Family Overview
4. Type System Design
   - Me: Epistemic Types
   - Solo: Affine Types
   - Duet: Refinement Types
5. Translation Semantics
6. Verification Pipeline
7. Case Study: Dempster-Shafer Fusion
8. Evaluation
9. Conclusion

---

## Paper 5: Emotional Temperature Metrics for Development

**Target:** CHASE 2026 (Workshop)
**Length:** 8 pages
**Status:** Outline complete

### Abstract

We propose "emotional temperature" metrics for software development teams, measuring collaboration health through communication patterns, response times, and conflict resolution. Unlike traditional productivity metrics, emotional temperature focuses on sustainable development practices and early detection of burnout or dysfunction.

### Key Contributions

1. **Metric Definition** - Formal definition of emotional temperature
2. **Measurement Tools** - Non-invasive data collection methods
3. **Intervention Triggers** - When to act on temperature changes
4. **Privacy Considerations** - Ethical data collection guidelines

### Outline

1. Introduction: Beyond Velocity
2. Background: Team Health Metrics
3. Emotional Temperature Model
4. Measurement Methodology
5. Case Study: My-newsroom Development
6. Discussion: Privacy and Ethics
7. Conclusion

---

## Submission Timeline

| Paper | Venue | Deadline | Status |
|-------|-------|----------|--------|
| RSR Framework | ICSE 2026 | Oct 2025 | Outlining |
| TPCF Trust Model | CHI 2026 | Sep 2025 | Outlining |
| Belief CRDTs | Middleware 2026 | May 2026 | Outlining |
| iSOS Pipeline | PLDI 2026 | Nov 2025 | Outlining |
| Emotional Temp | CHASE 2026 | Feb 2026 | Outlining |

---

## Contributing

Interested in co-authoring? See [CONTRIBUTING.md](../../CONTRIBUTING.md) for how to get involved in research activities.

**Requirements:**
- Academic affiliation or equivalent research experience
- Familiarity with epistemic logic, type systems, or distributed systems
- Commitment to open access publication

---

## References

Key references informing this research:

1. Shafer, G. (1976). A Mathematical Theory of Evidence
2. Pierce, B. C. (2002). Types and Programming Languages
3. Wooldridge, M. (2009). An Introduction to MultiAgent Systems
4. Fagin, R. et al. (1995). Reasoning About Knowledge
5. Shapiro, M. et al. (2011). Conflict-free Replicated Data Types
