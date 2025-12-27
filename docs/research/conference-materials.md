# Conference Materials

**Status:** Abstracts Complete | Slides In Progress
**Target Venues:** 30+ conferences across security, PL, distributed systems
**Timeline:** 2025-2026 speaking circuit

---

## Overview

This document contains 9 talk abstracts designed for submission to technical conferences, covering topics from the My-newsroom project including epistemic programming, formal verification, and political autonomy in software.

---

## Talk 1: Post-JavaScript Liberation

**Format:** 45 min technical talk
**Target Venues:** FOSDEM, JSConf, ReactConf, NodeConf
**Audience:** Web developers, frontend engineers

### Abstract

The web platform has evolved beyond JavaScript's original design constraints, yet we remain locked into a language designed for form validation in 1995. This talk presents a path to "post-JavaScript liberation" through compile-to-JS languages that offer type safety, memory safety, and epistemic reasoning without sacrificing browser compatibility.

We'll explore the My Language family—a suite of dialects from Me (epistemic types) through Ensemble (multi-agent systems)—demonstrating how modern language design can improve reliability while maintaining the reach of the web platform.

### Outline

1. The JavaScript Trap (5 min)
2. Compile-to-JS Landscape (10 min)
3. Me Dialect Demo: Belief States in the Browser (10 min)
4. Solo Dialect: Memory Safety Without GC (10 min)
5. The Path Forward: Gradual Migration (10 min)

### Key Takeaways

- TypeScript is a stepping stone, not the destination
- Affine types can eliminate entire bug classes
- Epistemic programming enables uncertainty-aware UIs

---

## Talk 2: Distributed State Without Coordination

**Format:** 60 min deep-dive
**Target Venues:** Strange Loop, Hydra, Papers We Love
**Audience:** Distributed systems engineers, researchers

### Abstract

Coordination is the enemy of availability. This talk presents a coordination-free approach to distributed belief systems using CRDTs (Conflict-free Replicated Data Types) combined with Dempster-Shafer evidence theory. We show how agents can independently update beliefs and merge without conflicts, achieving eventual consistency with formal guarantees.

Live demo: 50 simulated journalist agents reaching consensus on claim verification without any central coordinator.

### Outline

1. The Coordination Problem (10 min)
2. CRDTs Primer (15 min)
3. Dempster-Shafer Theory (15 min)
4. Belief CRDTs: The Synthesis (10 min)
5. Live Demo: Newsroom Simulation (10 min)

### Key Takeaways

- CRDTs enable offline-first distributed systems
- Belief fusion is naturally commutative and associative
- Epistemic ledgers provide audit trails without blockchain overhead

---

## Talk 3: 10+ Dimensions of Security

**Format:** 60 min security talk
**Target Venues:** DEF CON, Black Hat, BSides, OWASP
**Audience:** Security professionals, pentesters

### Abstract

Modern security goes far beyond OWASP Top 10. This talk presents a multi-dimensional security framework covering memory safety, type safety, supply chain security, operational security, cryptographic hygiene, and—crucially—political autonomy from vendor lock-in.

We'll demonstrate how the RSR (Rhodium Standard Repository) framework addresses each dimension, with practical examples from the My-newsroom project.

### Outline

1. Beyond OWASP: The Security Landscape (10 min)
2. Memory Safety: Why Rust Isn't Enough (10 min)
3. Supply Chain: Reproducible Builds with Guix/Nix (10 min)
4. Political Autonomy: Vendor Lock-in as Security Risk (10 min)
5. RSR Framework: Putting It Together (10 min)
6. Threat Modeling Demo (10 min)

### Key Takeaways

- Vendor lock-in is a security vulnerability
- Type systems are security tools
- Air-gapped operation should be the default

---

## Talk 4: RSR - Politically Autonomous Software

**Format:** 20 min research talk
**Target Venues:** FOSDEM (Legal Track), OSS Summit, CopyleftConf
**Audience:** Open source maintainers, legal professionals

### Abstract

The Rhodium Standard Repository (RSR) framework provides guidelines for creating software that remains functional and forkable regardless of corporate acquisitions, service shutdowns, or political pressure. This talk presents RSR's core principles and demonstrates compliance with a live repository audit.

### Outline

1. The Problem: Rug Pulls and Lock-in (5 min)
2. RSR Core Principles (5 min)
3. Live Audit: My-newsroom Compliance (5 min)
4. Adoption Roadmap (5 min)

### Key Takeaways

- Offline-first is a political choice
- Repository structure affects forkability
- TPCF enables graduated trust without gatekeeping

---

## Talk 5: Dempster-Shafer for Developers

**Format:** 30 min tutorial
**Target Venues:** PyCon, JuliaCon, RustConf
**Audience:** Developers interested in uncertainty quantification

### Abstract

Probabilities aren't always enough. This tutorial introduces Dempster-Shafer evidence theory—a mathematical framework for reasoning about uncertainty, ignorance, and conflicting evidence. We'll implement belief fusion from scratch and show how it improves on naive Bayesian approaches for real-world applications like fact-checking and sensor fusion.

### Outline

1. Why Not Just Use Probabilities? (5 min)
2. Belief Functions: The Math (10 min)
3. Live Coding: Fusion in Julia/Rust (10 min)
4. Applications: Newsroom, IoT, Medical (5 min)

### Key Takeaways

- "I don't know" is different from "50/50"
- Conflict detection prevents overconfident conclusions
- Dempster-Shafer is implementable in < 100 LOC

---

## Talk 6: Type Systems as Documentation

**Format:** 25 min talk
**Target Venues:** Write the Docs, API World, DevRelCon
**Audience:** Technical writers, API designers, DevRel

### Abstract

The best documentation is the kind that can't go stale. This talk argues that rich type systems—epistemic types, refinement types, session types—serve as living documentation that's checked by the compiler. We'll show how the My Language family uses types to document uncertainty, ownership, and protocol compliance.

### Outline

1. Documentation Rot (5 min)
2. Types as Contracts (10 min)
3. Epistemic Types: Documenting Uncertainty (5 min)
4. Session Types: Documenting Protocols (5 min)

### Key Takeaways

- If it's not in the types, it's not guaranteed
- Refinement types capture business rules
- Compiler-checked docs never drift

---

## Talk 7: AI-Assisted Formal Verification

**Format:** 45 min talk
**Target Venues:** POPL (co-located), ICFP, Lambda Days
**Audience:** PL researchers, formal methods practitioners

### Abstract

Formal verification has a user experience problem. This talk presents Duet, a dialect designed for human-AI collaborative programming where humans specify intent and invariants while AI synthesizes implementations with machine-checkable proofs. We demonstrate synthesis of Dempster-Shafer fusion with automatically generated SPARK proofs.

### Outline

1. The Verification UX Problem (10 min)
2. Duet Dialect Design (10 min)
3. Synthesis Pipeline (10 min)
4. Live Demo: Verified Belief Fusion (10 min)
5. Open Challenges (5 min)

### Key Takeaways

- AI can generate proofs, not just code
- Synthesis holes + verification = trustworthy AI
- Humans specify "what", AI figures out "how"

---

## Talk 8: Building a 100-Agent Newsroom

**Format:** 40 min case study
**Target Venues:** Journalism conferences (ONA, IRE), AI ethics events
**Audience:** Journalists, media technologists, AI ethicists

### Abstract

What if a newsroom could verify claims using 100 AI agents with formal uncertainty quantification? This talk presents Newroom, a research prototype for multi-agent journalism that combines Dempster-Shafer belief fusion with Byzantine fault tolerance. We discuss the ethical implications and limitations of AI-assisted fact-checking.

### Outline

1. The Misinformation Problem (5 min)
2. Multi-Agent Architecture (10 min)
3. Belief Fusion for Fact-Checking (10 min)
4. Demo: Claim Verification Pipeline (10 min)
5. Ethics and Limitations (5 min)

### Key Takeaways

- AI fact-checking requires uncertainty quantification
- "Confidence" should be formally defined, not vibes
- Human editors remain essential

---

## Talk 9: TPCF - Trust Without Gatekeeping

**Format:** 20 min lightning talk
**Target Venues:** Maintainerati, SustainOSS, Community Leadership Summit
**Audience:** Open source maintainers, community managers

### Abstract

How do you balance openness with security? The Tri-Perimeter Contribution Framework (TPCF) provides a graduated trust model where contributors advance through concentric zones based on demonstrated trustworthiness. This talk shows how TPCF enables inclusive communities without sacrificing code quality or security.

### Outline

1. The Trust Dilemma (5 min)
2. Three Perimeters (5 min)
3. Graduation Mechanics (5 min)
4. Results from My-newsroom (5 min)

### Key Takeaways

- Trust is earned incrementally
- Perimeters clarify expectations
- Everyone starts in Perimeter 3—and that's okay

---

## Conference Submission Tracker

| Talk | Status | Submitted To | Response |
|------|--------|--------------|----------|
| Post-JavaScript Liberation | Ready | - | - |
| Distributed State | Ready | - | - |
| 10+ Dimensions of Security | Ready | - | - |
| RSR Framework | Ready | - | - |
| Dempster-Shafer Tutorial | Ready | - | - |
| Types as Documentation | Ready | - | - |
| AI-Assisted Verification | Ready | - | - |
| 100-Agent Newsroom | Ready | - | - |
| TPCF Trust Model | Ready | - | - |

---

## Speaking Kit

### Bio (Short)

Jonathan D.A. Jewell (hyperpolymath) is the creator of the My Language family and researcher in epistemic programming for neurosymbolic journalism. His work focuses on formal uncertainty quantification, political autonomy in software, and multi-agent systems.

### Bio (Long)

Jonathan D.A. Jewell, known online as hyperpolymath, is a polyglot programmer and independent researcher exploring the intersection of programming language theory, distributed systems, and journalism technology. He created the My Language family—a suite of four dialects for epistemic programming—and the RSR (Rhodium Standard Repository) framework for politically autonomous software. His current research focuses on Dempster-Shafer belief fusion for automated fact-checking and AI-assisted formal verification.

### Requirements

- Projector with HDMI
- Internet access for live demos (or offline backup)
- 30 min setup time for multi-agent demos

---

## Contributing

Interested in co-presenting? See [CONTRIBUTING.md](../../CONTRIBUTING.md) for collaboration opportunities.
