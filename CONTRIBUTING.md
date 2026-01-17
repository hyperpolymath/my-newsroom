# Contributing to My-newsroom

Welcome! We're excited you're interested in contributing to epistemic programming and neurosymbolic AI for journalism. 🎉

**Version:** 1.0.0
**Last Updated:** 2025-11-22
**Governance:** TPCF Perimeter 3 (Community Sandbox)

---

## 🎯 Quick Start

### 1. Understand the Project

Before contributing, familiarize yourself with:

- **[README.md](README.md)** - Project overview and quick start
- **[My Language Index](docs/MY-LANGUAGE-INDEX.md)** - All 4 dialects explained
- **[Newroom Roadmap](docs/NEWROOM-ROADMAP.md)** - Demonstration project plan
- **[claude.md](claude.md)** - AI assistant guidelines and development philosophy

### 2. Set Up Development Environment

```bash
# Clone repository
git clone https://gitlab.com/Hyperpolymath/My-newsroom.git
cd My-newsroom

# Install dependencies
## Python (for prototyping)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Testing and linting tools

## Rust (for Solo dialect compiler)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup default stable
cargo build

## Node.js (for Me dialect playground)
nvm install 20
nvm use 20
npm install

# Run tests to verify setup
pytest tests/              # Python tests
cargo test                 # Rust tests
npm test                   # JavaScript tests
```

### 3. Find Something to Work On

- **Good First Issues:** https://gitlab.com/Hyperpolymath/My-newsroom/-/issues?label_name[]=good%20first%20issue
- **Help Wanted:** https://gitlab.com/Hyperpolymath/My-newsroom/-/issues?label_name[]=help%20wanted
- **Roadmap Tracking:** See [NEWROOM-ROADMAP.md](docs/NEWROOM-ROADMAP.md) for big-picture tasks

### 4. Make Your Changes

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes with frequent commits
git add src/module/file.rs
git commit -m "feat: add Dempster-Shafer normalization"

# Run tests and linting
pytest tests/
cargo test
cargo clippy -- -D warnings

# Push and create merge request
git push origin feature/your-feature-name
```

Then open a merge request on GitLab with:
- Clear title (use conventional commits format)
- Description of changes
- Link to related issues
- Screenshots/examples if applicable

---

## 🏛️ Governance: TPCF Model

**My-newsroom** follows the **Tri-Perimeter Contribution Framework (TPCF)**:

### Perimeter 3: Community Sandbox (Current)

**Access:** Fully open contributions from anyone
**Permissions:**
- ✅ Fork repository
- ✅ Create merge requests
- ✅ Comment on issues
- ✅ Participate in discussions

**Review Required:**
- All contributions reviewed by ≥1 Perimeter 2 maintainer
- First-time contributors get extra scrutiny (welcome, but verify!)
- Large changes (>500 LOC) may require design doc first

**Typical Contributors:**
- First-time contributors
- Occasional contributors
- Bug reporters
- Documentation improvers

### Perimeter 2: Verified Contributors (Future)

**Access:** Invitation-only after sustained contribution
**Permissions:**
- ✅ All Perimeter 3 permissions
- ✅ Direct push to non-protected branches
- ✅ Review and approve others' merge requests
- ✅ Triage and label issues

**Requirements:**
- ≥5 merged contributions
- ≥3 months active participation
- Demonstrated understanding of project values
- Nomination by Perimeter 1 maintainer

**Typical Contributors:**
- Regular contributors
- Subject matter experts
- Long-term community members

### Perimeter 1: Core Maintainers (Future)

**Access:** By invitation only
**Permissions:**
- ✅ All Perimeter 2 permissions
- ✅ Direct commit to protected branches
- ✅ Create releases
- ✅ Manage CI/CD pipeline
- ✅ Invite Perimeter 2 members

**Requirements:**
- ≥20 merged contributions
- ≥6 months active participation
- Deep expertise in ≥1 dialect
- Trusted by existing Perimeter 1 members

**Typical Contributors:**
- Project founders
- Lead developers
- Architecture decision-makers

### Current Status (2025-11-22)

- **Perimeter 1:** 1 member (project creator)
- **Perimeter 2:** 0 members (accepting nominations!)
- **Perimeter 3:** All contributors welcome

---

## 📝 Contribution Types

### Code Contributions

**Languages:**
- **Python** (prototyping, Dempster-Shafer implementation)
- **Rust** (Solo dialect compiler, runtime)
- **TypeScript** (Me dialect playground)
- **Ada 2022** (Duet dialect verifier - future)
- **Elixir/Haskell** (Ensemble dialect runtime - future)

**Areas:**
- Compiler development (parsers, type checkers, code generators)
- Runtime systems (memory management, garbage collection)
- Belief fusion algorithms (Dempster-Shafer, Yager, Dubois-Prade)
- Agent frameworks (actor models, communication protocols)
- Formal verification (SPARK proofs, property-based testing)

### Documentation Contributions

**Types:**
- **Tutorials** - Step-by-step guides for newcomers
- **How-to guides** - Task-oriented instructions
- **Reference** - Complete API/syntax documentation
- **Explanations** - Theoretical background and design decisions

**Style:**
- Use active voice ("Run the compiler" not "The compiler is run")
- Include runnable examples with expected output
- Link to related docs liberally
- Update the master index when adding new pages

### Research Contributions

**Academic Work:**
- **Paper writing** - See [academic-papers.md](docs/research/academic-papers.md)
- **Experiments** - Design and run evaluations
- **Literature reviews** - Survey related work
- **Formal proofs** - Prove language properties (type safety, soundness)

**Conference Talks:**
- **Abstracts** - See [conference-materials.md](docs/research/conference-materials.md)
- **Slides** - Design presentations
- **Demos** - Build live demonstrations
- **Videos** - Record talks and tutorials

### Community Contributions

**Non-Code:**
- **Bug reports** - File detailed issue reports
- **Feature requests** - Propose new capabilities
- **Testing** - Try out features and report findings
- **Advocacy** - Write blog posts, give talks, spread the word

---

## 🧪 Testing Requirements

### Test Coverage Targets

- **Python:** ≥80% line coverage (measured with `pytest-cov`)
- **Rust:** ≥80% line coverage (measured with `tarpaulin`)
- **TypeScript:** ≥70% line coverage (measured with `jest`)

### Testing Pyramid

```
       /\
      /  \  E2E Tests (5% - slow, brittle)
     /----\
    /      \ Integration Tests (15% - medium speed)
   /--------\
  /          \ Unit Tests (80% - fast, focused)
 /------------\
```

**Example: Adding Dempster-Shafer Normalization**

```python
# tests/test_dempster_shafer.py
import pytest
from mynewsroom.dempster_shafer import BeliefMass, fuse_beliefs

class TestDempsterShaferFusion:
    def test_normalization_with_conflict(self):
        """Dempster's rule normalizes by dividing by (1 - conflict)."""
        m1 = BeliefMass({"A": 0.9, "B": 0.1})
        m2 = BeliefMass({"A": 0.1, "B": 0.9})

        result = fuse_beliefs(m1, m2, method="dempster")

        # Conflict = 0.9*0.9 + 0.1*0.1 = 0.82
        # Expected: A = (0.9*0.1) / (1-0.82) = 0.09/0.18 = 0.5
        assert abs(result["A"] - 0.5) < 1e-6
        assert abs(result["B"] - 0.5) < 1e-6

    def test_normalization_with_zero_conflict(self):
        """When there's no conflict, normalization is identity."""
        m1 = BeliefMass({"A": 0.7, "Θ": 0.3})
        m2 = BeliefMass({"A": 0.5, "Θ": 0.5})

        result = fuse_beliefs(m1, m2, method="dempster")

        # No conflict, so no normalization needed
        assert result["A"] > 0.7  # Belief in A increases
        assert abs(sum(result.values()) - 1.0) < 1e-6

    def test_high_conflict_raises_warning(self):
        """Warn when conflict > 0.9 (result unreliable)."""
        m1 = BeliefMass({"A": 1.0})
        m2 = BeliefMass({"B": 1.0})

        with pytest.warns(UserWarning, match="High conflict"):
            fuse_beliefs(m1, m2, method="dempster")
```

**Run Tests:**
```bash
pytest tests/test_dempster_shafer.py -v --cov=mynewsroom.dempster_shafer
```

---

## 📏 Code Style

### Python (PEP 8 + Type Hints)

```python
# ✅ Good: Type hints, docstrings, clear names
from typing import Dict, Set, Optional

def calculate_conflict(
    m1: BeliefMass,
    m2: BeliefMass
) -> float:
    """Calculate Dempster-Shafer conflict between two belief masses.

    Args:
        m1: First belief mass function
        m2: Second belief mass function

    Returns:
        Conflict measure in [0, 1], where 0 = no conflict

    Raises:
        ValueError: If m1 and m2 have different frames of discernment
    """
    if m1.frame != m2.frame:
        raise ValueError(f"Incompatible frames: {m1.frame} vs {m2.frame}")

    conflict = 0.0
    for set_a in m1.focal_sets:
        for set_b in m2.focal_sets:
            if set_a.isdisjoint(set_b):
                conflict += m1[set_a] * m2[set_b]

    return conflict

# ❌ Bad: No types, unclear names, no docs
def calc(m1, m2):
    c = 0.0
    for a in m1.keys():
        for b in m2.keys():
            if a & b == set():
                c += m1[a] * m2[b]
    return c
```

**Formatting:**
```bash
black src/ tests/        # Auto-format with Black
isort src/ tests/        # Sort imports
mypy src/               # Type checking
pylint src/             # Linting
```

### Rust (Clippy + rustfmt)

```rust
// ✅ Good: Explicit types, error handling, documentation
/// Parses a belief value from a string representation.
///
/// # Arguments
/// * `s` - String in format "value@confidence" (e.g., "0.7@0.85")
///
/// # Returns
/// * `Ok(Belief)` - Successfully parsed belief
/// * `Err(ParseError)` - Invalid format or out-of-range values
///
/// # Examples
/// ```
/// let belief = parse_belief("0.7@0.85")?;
/// assert_eq!(belief.value(), 0.7);
/// assert_eq!(belief.confidence(), 0.85);
/// ```
pub fn parse_belief(s: &str) -> Result<Belief, ParseError> {
    let parts: Vec<&str> = s.split('@').collect();
    if parts.len() != 2 {
        return Err(ParseError::InvalidFormat);
    }

    let value = parts[0].parse::<f64>()
        .map_err(|_| ParseError::InvalidValue)?;
    let confidence = parts[1].parse::<f64>()
        .map_err(|_| ParseError::InvalidConfidence)?;

    Belief::new(value, confidence)
        .ok_or(ParseError::OutOfRange)
}

// ❌ Bad: Panics, no docs, unclear errors
pub fn parse_belief(s: &str) -> Belief {
    let parts: Vec<&str> = s.split('@').collect();
    let v = parts[0].parse().unwrap();
    let c = parts[1].parse().unwrap();
    Belief::new(v, c).unwrap()
}
```

**Formatting:**
```bash
cargo fmt               # Auto-format
cargo clippy -- -D warnings  # Linting (treat warnings as errors)
```

### Commit Messages (Conventional Commits)

Format: `<type>(<scope>): <subject>`

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `style` - Formatting, whitespace
- `refactor` - Code restructuring (no behavior change)
- `perf` - Performance improvement
- `test` - Adding/fixing tests
- `chore` - Build system, dependencies

**Examples:**
```
feat(solo): add QBE backend for code generation
fix(dempster): handle high-conflict normalization correctly
docs(ensemble): add agent topology examples
test(duet): add property-based tests for verification
```

---

## 🔍 Review Process

### Merge Request Checklist

Before requesting review, verify:

- [ ] **Tests pass** - All CI checks green
- [ ] **Coverage maintained** - No decrease in test coverage
- [ ] **Linting clean** - No warnings from clippy/pylint/eslint
- [ ] **Docs updated** - README, CHANGELOG, and relevant guides
- [ ] **Examples work** - Run example code and verify output
- [ ] **No secrets** - No API keys, passwords, or PII committed
- [ ] **License headers** - All new files have copyright notice
- [ ] **RSR compliant** - Offline-first, type-safe, memory-safe

### Review Timeline

- **First response:** ≤ 3 business days
- **Full review:** ≤ 7 business days
- **Large changes (>500 LOC):** ≤ 14 business days

If your MR hasn't been reviewed in 7 days, ping in comments or email maintainers.

### Review Criteria

Reviewers check for:

1. **Correctness** - Does it work? Are edge cases handled?
2. **Security** - Any vulnerabilities introduced?
3. **Performance** - Is it efficient? Any algorithmic issues?
4. **Maintainability** - Is it readable? Well-documented?
5. **Consistency** - Does it match existing code style?
6. **Testing** - Adequate test coverage?

### Responding to Feedback

- **Be gracious** - Reviews are about code, not you personally
- **Ask questions** - If feedback is unclear, ask for clarification
- **Explain trade-offs** - If you disagree, explain your reasoning
- **Iterate quickly** - Address feedback within 3-5 days if possible

---

## 🚀 Release Process

(For Perimeter 1 maintainers only)

### Versioning (SemVer)

- **Major (1.0.0):** Breaking changes
- **Minor (0.1.0):** New features, backwards-compatible
- **Patch (0.0.1):** Bug fixes, no new features

### Release Checklist

1. Update `CHANGELOG.md` with all changes since last release
2. Bump version in `Cargo.toml`, `package.json`, `pyproject.toml`
3. Run full test suite: `pytest && cargo test && npm test`
4. Tag release: `git tag -a v0.1.0 -m "Release v0.1.0"`
5. Push tag: `git push origin v0.1.0`
6. GitLab CI automatically builds and publishes artifacts
7. Announce on mailing list, Twitter, HN, Reddit, etc.

---

## 📞 Getting Help

### Communication Channels

- **GitLab Issues:** https://gitlab.com/Hyperpolymath/My-newsroom/-/issues
- **GitLab Discussions:** https://gitlab.com/Hyperpolymath/My-newsroom/-/discussions
- **Email:** contributors@[project-domain]

### Resources

- **Development Docs:** [docs/](docs/)
- **Language Specs:** [docs/dialects/](docs/dialects/)
- **Roadmap:** [NEWROOM-ROADMAP.md](docs/NEWROOM-ROADMAP.md)
- **AI Guidelines:** [claude.md](claude.md)

---

## 🙏 Recognition

We value all contributions! Every contributor is listed in:

- **.well-known/humans.txt** - Full credits
- **MAINTAINERS.md** - Active maintainers
- **Release notes** - Per-release contributors

---

## 📜 License

By contributing, you agree to license your work under the same dual MIT + Palimpsest v0.8 terms as the rest of the project. See [LICENSE.txt](LICENSE.txt).

---

**Thank you for contributing to epistemic programming!** Together we're building politically autonomous software for journalism's future. 🚀📰🤖
