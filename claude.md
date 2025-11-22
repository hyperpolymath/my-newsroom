# Claude AI Assistant Guidelines for My-newsroom

**Version:** 1.0.0
**Last Updated:** 2025-11-22
**Compliance:** RSR Framework, TPCF Perimeter 3 (Community Sandbox)

---

## 🎯 Project Overview

**My-newsroom** is a research project exploring epistemic programming languages and neurosymbolic AI for journalism. It implements the **My Language** family (Me, Solo, Duet, Ensemble dialects) and demonstrates multi-agent belief fusion using Dempster-Shafer theory.

### Core Mission
- Develop type-safe epistemic programming with graduated trust semantics
- Build neurosymbolic AI tooling for journalistic verification
- Demonstrate distributed multi-agent systems with formal uncertainty quantification
- Create politically autonomous software resistant to vendor lock-in

---

## 🤖 AI Training & Usage Policies

### Training Data Opt-Out
```
User-Agent: *
Disallow: /src/
Disallow: /examples/
Disallow: /tests/

# AI Training Crawlers
User-Agent: GPTBot
Disallow: /

User-Agent: ChatGPT-User
Disallow: /

User-Agent: CCBot
Disallow: /

User-Agent: anthropic-ai
Disallow: /

User-Agent: Claude-Web
Disallow: /

User-Agent: Google-Extended
Disallow: /
```

**Policy Statement:** This repository's code, documentation, and research materials are **NOT** authorized for inclusion in AI training datasets without explicit written permission. See `.well-known/ai.txt` for machine-readable policy.

### Permitted AI Assistance

✅ **Allowed:**
- Code generation assistance for contributors with explicit intent
- Documentation writing and technical editing
- Test case generation and validation
- Type checking and formal verification assistance
- Academic paper writing and research analysis
- Conference talk preparation
- Bug detection and security analysis

❌ **Prohibited:**
- Bulk scraping for training data
- Unauthorized derivative model fine-tuning
- Commercial AI product training without license
- Synthetic data generation for resale

---

## 📋 Claude-Specific Instructions

### 1. Repository Philosophy

This project follows the **Rhodium Standard Repository (RSR)** framework:

- **Offline-first:** No network calls in core logic; works air-gapped
- **Type-safe:** Gradual typing from Python → TypeScript → Rust/Ada
- **Memory-safe:** Zero `unsafe` in production Rust code
- **Politically autonomous:** No vendor lock-in; reproducible builds

### 2. Dialect-Specific Assistance

When working with **My Language** code:

#### Me Dialect (Epistemic Foundation)
```my
belief x: Float where confidence(0.75);
x ~ Uniform(0, 1);  # Epistemic uncertainty modeling
```
- Focus: Probabilistic types, belief states, trust semantics
- Key files: `docs/dialects/me.md`, `examples/me/`

#### Solo Dialect (Systems Programming)
```solo
fn process(data: &[u8]) -> Result<Vec<u8>, Error> {
    // Affine types, arena allocation, compile-time checks
}
```
- Focus: Performance, safety, no-GC memory management
- Key files: `docs/dialects/solo.md`, `src/solo/`

#### Duet Dialect (Human-AI Co-programming)
```duet
intent("Implement Dempster-Shafer belief combination")
fn combine_beliefs(b1: Belief, b2: Belief) -> Belief where
    @verify: "commutativity: combine(b1,b2) == combine(b2,b1)" {
    @synth { /* AI fills implementation */ }
}
```
- Focus: Formal contracts, AI-assisted synthesis, verification
- Key files: `docs/dialects/duet.md`, `examples/duet/`

#### Ensemble Dialect (Multi-Agent Orchestration)
```ensemble
comptime orchestrate NewsVerificationRing {
    agents: [ReporterAgent; 5],
    topology: Ring,
    fusion: DempsterShafer,
    consensus: Threshold(0.85),
}
```
- Focus: Agent coordination, belief fusion, distributed systems
- Key files: `docs/dialects/ensemble.md`, `src/newroom/`

### 3. Development Workflows

#### When Implementing Features
1. ✅ **Read existing specs first** - Check `docs/dialects/` before coding
2. ✅ **Write tests first** - TDD approach, 80%+ coverage target
3. ✅ **Update docs** - Keep `CHANGELOG.md` and dialect specs current
4. ✅ **Run compliance checks** - Use `just validate` before committing
5. ✅ **Follow RSR checklist** - See `docs/RSR-COMPLIANCE.md`

#### When Writing Documentation
- Use **active voice** and **imperative mood** for technical docs
- Include **runnable examples** with expected output
- Add **mathematical notation** for formal semantics (use LaTeX)
- Cross-reference **related dialects** and **prior art**
- Update **master index** (`docs/MY-LANGUAGE-INDEX.md`)

#### When Doing Research Analysis
- Cite **primary sources** (papers, RFCs, specifications)
- Include **page numbers** and **DOIs** where available
- Note **assumptions** and **limitations** explicitly
- Suggest **experiments** or **validation approaches**
- Link to **related conversations** (use commit SHAs)

### 4. Code Style & Standards

#### Rust (Solo dialect implementation)
```rust
// ✅ Good: Explicit error handling, no unwrap()
fn parse_belief(s: &str) -> Result<Belief, ParseError> {
    let value = s.parse::<f64>()
        .map_err(|e| ParseError::InvalidFloat(e))?;
    Belief::new(value).ok_or(ParseError::OutOfRange)
}

// ❌ Bad: Panics on error
fn parse_belief(s: &str) -> Belief {
    Belief::new(s.parse().unwrap()).unwrap()
}
```

#### Python (Prototyping & Research)
```python
# ✅ Good: Type hints, docstrings, validation
def fuse_beliefs(
    b1: BeliefMass,
    b2: BeliefMass,
    method: FusionRule = FusionRule.DEMPSTER
) -> BeliefMass:
    """Combine two belief masses using Dempster-Shafer theory.

    Args:
        b1: First belief mass function over frame Θ
        b2: Second belief mass function over same frame
        method: Fusion rule (Dempster, Yager, or Dubois-Prade)

    Returns:
        Combined belief mass with conflict resolution

    Raises:
        ValueError: If b1 and b2 have incompatible frames
    """
    if b1.frame != b2.frame:
        raise ValueError("Incompatible frames of discernment")
    # ... implementation
```

#### Markdown (Documentation)
- Use **heading anchors** for linking: `## Syntax {#syntax}`
- Include **YAML frontmatter** for metadata
- Add **code fence languages**: ` ```my `, ` ```solo `, ` ```ensemble `
- Use **tables** for comparisons, **lists** for procedures
- Include **diagrams** (Mermaid, PlantUML, TikZ) where helpful

### 5. Security & Privacy

#### Handling Sensitive Data
- **Never commit secrets** - Use `.env.example` templates
- **No PII in examples** - Use synthetic data only
- **Anonymize logs** - Redact user identifiers in traces
- **Document threat model** - Update `SECURITY.md` for new features

#### Vulnerability Reporting
See `.well-known/security.txt` for coordinated disclosure process.

**Quick reference:**
- Email: security@[project-domain]
- PGP: [Key fingerprint]
- Policy: 90-day disclosure timeline

### 6. Academic & Research Support

When preparing **academic papers**:
```markdown
1. Literature review → Use Semantic Scholar API (cite 20-30 papers)
2. Related work → Compare to 5-7 closest systems
3. Formal semantics → Write operational semantics in LaTeX
4. Evaluation → Design experiments with N≥50 for quantitative
5. Threats to validity → Address internal/external/construct validity
```

When preparing **conference talks**:
```markdown
1. Abstract (250 words) → Submit to 3-5 venues simultaneously
2. Outline (3-act structure) → Problem → Solution → Evaluation
3. Slides (1 slide/min) → 30% diagrams, 20% code, 50% bullet points
4. Demo (5-10 min) → Live coding or pre-recorded with narration
5. Q&A prep (10-15 questions) → Anticipate objections & edge cases
```

### 7. Collaboration Etiquette

#### With Human Contributors
- **Be concise** - Respect their time; summarize key points first
- **Show uncertainty** - Say "I think" or "Possibly" when unsure
- **Suggest, don't prescribe** - Offer options, let humans decide
- **Credit ideas** - Acknowledge prior art and contributor suggestions
- **Ask clarifying questions** - Don't guess at ambiguous requirements

#### With Other AI Assistants
- **Share context** - Use `claude.md` to align on project norms
- **Avoid redundancy** - Check recent commits before regenerating docs
- **Maintain consistency** - Follow established patterns in codebase
- **Version decisions** - Document "why" in commit messages

### 8. Continuous Improvement

#### Self-Assessment Questions
Before completing a task, ask:
1. ✅ Did I read existing docs before proposing changes?
2. ✅ Are my suggestions RSR-compliant?
3. ✅ Did I test the code (or suggest tests)?
4. ✅ Is the documentation updated?
5. ✅ Would this work offline/air-gapped?
6. ✅ Is this politically autonomous (no vendor lock-in)?
7. ✅ Did I avoid over-engineering?

#### Learning from Feedback
- **Track issues** - Monitor GitLab issue tracker for recurring themes
- **Read changelogs** - Understand how project evolved over time
- **Study rejections** - If code is rejected, ask why and adapt
- **Update this file** - Propose amendments to `claude.md` when patterns emerge

---

## 📚 Key Resources

### Essential Reading (Priority Order)
1. `docs/MY-LANGUAGE-INDEX.md` - Master index of all 4 dialects
2. `docs/NEWROOM-ROADMAP.md` - Demonstration project plan
3. `docs/RSR-COMPLIANCE.md` - Repository standards checklist
4. `docs/dialects/duet.md` - Human-AI co-programming spec
5. `docs/dialects/ensemble.md` - Multi-agent orchestration spec

### External References
- [RSR Framework](https://gitlab.com/rhodium-project/rsr) - Repository standards
- [Dempster-Shafer Theory](https://en.wikipedia.org/wiki/Dempster–Shafer_theory) - Belief fusion math
- [TPCF Model](https://gitlab.com/rhodium-project/tpcf) - Tri-Perimeter access control
- [Palimpsest License v0.8](https://palimpsest.license) - Remediation-first licensing

### Quick Commands
```bash
just validate     # Run RSR compliance checks
just test         # Run full test suite
just docs         # Generate documentation
just examples     # Run all example code
```

---

## 🔄 Changelog

### 2025-11-22 - Initial Version
- Created `claude.md` with AI policies and development guidelines
- Established RSR compliance baseline (targeting Bronze → Silver)
- Documented all 4 dialects (Me, Solo, Duet, Ensemble)
- Added academic research support guidelines

---

## 📝 License & Attribution

- **Code:** Dual-licensed MIT + Palimpsest v0.8 (see `LICENSE.txt`)
- **Documentation:** CC BY-SA 4.0
- **Research Papers:** CC BY 4.0 (preprints), varies by venue (published)

**Contributors:** See `MAINTAINERS.md` and `.well-known/humans.txt`

**AI Disclosure:** This file was initially drafted by Claude (Anthropic) on 2025-11-22 under human direction, then reviewed and approved by project maintainers. All subsequent edits by humans/AI are tracked in git history.

---

**Questions?** Open an issue on GitLab or consult the FAQ in `docs/FAQ.md`.
