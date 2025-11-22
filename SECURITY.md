# Security Policy

**Version:** 1.0.0
**Last Updated:** 2025-11-22
**Compliance:** RSR Framework Security Requirements

---

## 🛡️ Security Commitment

**My-newsroom** follows security-first design principles:

- **Offline-first:** No network calls in core logic; works air-gapped
- **Memory-safe:** Zero `unsafe` blocks in production Rust code
- **Type-safe:** Gradual typing from Python → Rust/Ada
- **Least privilege:** TPCF perimeter-based access control
- **Defense in depth:** Multiple security layers (crypto, types, runtime checks)

---

## 📊 Supported Versions

| Version | Status | Security Updates | End of Life |
|---------|--------|-----------------|-------------|
| 0.1.x (alpha) | 🚧 Development | Best-effort | TBD |
| 1.0.x (planned) | 📋 Future | Full support | 2027-01-01 |

**Current Status:** Pre-release research prototype. Use in production at your own risk.

---

## 🚨 Reporting a Vulnerability

### Coordinated Disclosure Process

We follow **90-day coordinated disclosure**:

1. **Report privately** - Do NOT create public issues for security bugs
2. **We acknowledge** within 72 hours
3. **We investigate** and provide initial assessment within 14 days
4. **We fix** critical issues within 30 days, moderate issues within 60 days
5. **We disclose** publicly after fix is released OR 90 days, whichever is sooner

### How to Report

**Preferred Method:** Email security@[project-domain] with PGP encryption

**PGP Key Fingerprint:**
```
[TODO: Generate and publish PGP key]
Key ID: XXXX XXXX XXXX XXXX
Fingerprint: XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX
```

**Alternative Method:** GitLab confidential issue (if you don't have PGP)
1. Go to https://gitlab.com/Hyperpolymath/My-newsroom/-/issues/new
2. Check "This issue is confidential"
3. Title: "SECURITY: [Brief Description]"
4. Include details below

### What to Include

```markdown
## Summary
Brief description of the vulnerability (1-2 sentences)

## Impact
What can an attacker do? (e.g., RCE, XSS, data leak)

## Affected Components
- File: src/module/file.rs
- Function: vulnerable_function()
- Version: 0.1.0

## Steps to Reproduce
1. Step one
2. Step two
3. Observe vulnerability

## Proof of Concept
```bash
# Exploit code (if safe to share)
```

## Suggested Fix
(Optional) How you think it should be fixed

## CVE Requested?
[ ] Yes - Please request CVE on my behalf
[ ] No - I will request CVE myself
```

---

## 🔍 Security Scope

### In Scope

✅ **We accept reports for:**

- **Code execution:** RCE, arbitrary code injection, command injection
- **Memory safety:** Buffer overflows, use-after-free, data races
- **Cryptographic issues:** Weak algorithms, improper key handling, timing attacks
- **Authentication/Authorization:** Bypass, privilege escalation, session hijacking
- **Data leakage:** Sensitive data exposure, PII leaks, credential theft
- **Denial of Service:** Algorithmic complexity attacks, resource exhaustion
- **Injection attacks:** SQL, XSS, template injection, YAML/JSON deserialization
- **Supply chain:** Malicious dependencies, compromised build artifacts

### Out of Scope

❌ **We do NOT accept reports for:**

- **Social engineering:** Phishing project maintainers, impersonation
- **Physical security:** Theft of developer laptops, data center access
- **Third-party services:** Bugs in GitLab, GitHub, NPM, Cargo registries
- **Browser-specific bugs:** Unless they affect our HTML playground specifically
- **Denial of Service:** Network-level DDoS (we don't control infrastructure)
- **Issues requiring user interaction:** "Click this malicious link" type attacks
- **Already-known issues:** Check existing CVEs and security advisories first
- **Theoretical attacks:** Must be demonstrable with PoC

---

## 🏆 Recognition

### Hall of Fame

We maintain a **Security Researchers Hall of Fame** in `.well-known/security-researchers.txt`:

- Name (or pseudonym)
- Date of disclosure
- Severity of issue found
- Link to CVE (if assigned)

**Example:**
```
2025-11-22 | Alice Research (@alice) | CRITICAL | CVE-2025-XXXXX | RCE in Duet verifier
2025-12-01 | Bob Security Inc. | HIGH | CVE-2025-XXXXX | Type confusion in Solo compiler
```

### Bounties

**Current Status:** No bug bounty program (unfunded research project)

**Future Plans:** If we secure funding, we will offer:
- Critical: $500-1000
- High: $250-500
- Medium: $100-250
- Low: $50-100

---

## 🔐 Security Features

### Current Protections

| Feature | Status | Details |
|---------|--------|---------|
| Memory Safety | ✅ Rust/Ada | Zero `unsafe` in production code |
| Type Safety | ✅ Gradual | Python → TypeScript → Rust/Ada |
| Input Validation | 🚧 Partial | Parser enforces syntax, semantic checks TODO |
| Cryptographic Signing | 📋 Planned | Belief updates signed with Ed25519 |
| Sandboxing | 📋 Planned | WASM isolation for AI synthesis |
| Audit Logging | 📋 Planned | Immutable epistemic ledger |
| Dependency Scanning | 📋 TODO | Cargo audit, npm audit, safety (Python) |

### Threat Model

**Assumptions:**
1. **Network attacker:** Can intercept/modify traffic (MITM capable)
2. **Compromised agents:** Up to 33% of agents may be Byzantine
3. **Poisoned training data:** AI models may have backdoors
4. **Insider threat:** Some contributors may be malicious

**Non-Assumptions:**
1. **No physical access:** Adversary does not have physical access to servers
2. **No side channels:** Timing/power/EM analysis out of scope for now
3. **No quantum adversary:** Post-quantum crypto deferred to future work

**Mitigations:**
1. **Offline-first:** Reduces attack surface (no network = no MITM)
2. **Byzantine fault tolerance:** Consensus requires ≥67% honest agents
3. **Formal verification:** SPARK proofs prevent entire classes of bugs
4. **Code review:** All commits reviewed by ≥1 maintainer (TPCF Perimeter 2+)

---

## 🧪 Security Testing

### Current Practices

- **Static analysis:** `cargo clippy`, `rustc -D warnings`, Ada GNAT checks
- **Fuzzing:** TODO - Plan to use `cargo fuzz` for parsers
- **Dependency scanning:** TODO - Automate with GitLab CI
- **SAST:** TODO - Integrate Semgrep or CodeQL

### Future Enhancements

- **Penetration testing:** Hire external auditors before 1.0 release
- **Formal verification:** Prove Solo compiler correctness with SPARK
- **Runtime protection:** ASAN, MSAN, UBSAN in debug builds
- **Supply chain security:** Verify all dependencies with `cargo vet`

---

## 📜 Security Advisories

### Published Advisories

None yet (project is pre-release).

Future advisories will be published at:
- https://gitlab.com/Hyperpolymath/My-newsroom/-/security/advisories
- https://github.com/advisories (mirrored for visibility)

### Notification Channels

Subscribe to security updates:
1. **GitLab Watch** - Watch repository and enable security notifications
2. **Mailing list** - security-announce@[project-domain] (low-traffic)
3. **RSS feed** - https://gitlab.com/Hyperpolymath/My-newsroom/-/security/advisories.atom

---

## 🛠️ Security Best Practices for Contributors

### Code Review Checklist

Before approving a merge request, verify:

- [ ] No `unsafe` blocks without thorough justification
- [ ] All user input is validated (syntax + semantics)
- [ ] Error messages don't leak sensitive information
- [ ] Cryptographic primitives use well-vetted libraries (no custom crypto!)
- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] Dependencies are pinned to specific versions
- [ ] Tests cover security-critical edge cases

### Secure Coding Guidelines

**Rust (Solo dialect):**
```rust
// ✅ Good: Explicit error handling
fn parse_belief(s: &str) -> Result<Belief, ParseError> {
    let value = s.parse::<f64>()
        .map_err(|_| ParseError::InvalidFloat)?;
    if value < 0.0 || value > 1.0 {
        return Err(ParseError::OutOfRange);
    }
    Ok(Belief::new(value))
}

// ❌ Bad: Panics on invalid input
fn parse_belief(s: &str) -> Belief {
    Belief::new(s.parse().unwrap())
}
```

**Python (Prototyping):**
```python
# ✅ Good: Input validation with clear errors
def fuse_beliefs(m1: BeliefMass, m2: BeliefMass) -> BeliefMass:
    if m1.frame != m2.frame:
        raise ValueError(f"Incompatible frames: {m1.frame} vs {m2.frame}")
    if not m1.is_valid() or not m2.is_valid():
        raise ValueError("Invalid belief mass (probabilities don't sum to 1)")
    # ... safe to proceed

# ❌ Bad: Assumes inputs are valid
def fuse_beliefs(m1, m2):
    return BeliefMass({k: m1[k] * m2[k] for k in m1.keys()})
```

---

## 🔗 Related Resources

- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **Rust Security Guidelines:** https://anssi-fr.github.io/rust-guide/
- **CWE (Common Weakness Enumeration):** https://cwe.mitre.org/
- **CVE Database:** https://cve.mitre.org/
- **NVD (National Vulnerability Database):** https://nvd.nist.gov/

---

## 📞 Contact

- **Security Team:** security@[project-domain]
- **PGP Key:** See `.well-known/security.txt`
- **Urgent Issues:** Use Signal/WhatsApp (DM for phone number)

**Office Hours:** We aim to respond within 72 hours. For critical issues (RCE, data breach), we'll respond within 24 hours.

---

## 📝 Changelog

### 2025-11-22 - Initial Version
- Established 90-day coordinated disclosure policy
- Defined scope (in/out)
- Created reporting templates
- Documented threat model

---

**Security is a journey, not a destination.** We appreciate responsible disclosure and collaborative improvement. Thank you for helping keep My-newsroom secure! 🔒
