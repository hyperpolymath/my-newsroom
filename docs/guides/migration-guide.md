# Migration Guide

**Purpose:** Migrate existing code to My Language dialects
**Audience:** Developers with Python, TypeScript, or Rust experience
**Status:** Draft - Expanding with community feedback

---

## Overview

This guide helps you migrate existing codebases to the My Language family. Each section covers migration from a common source language to the appropriate My dialect.

---

## Quick Reference

| From | To | Difficulty | Guide Section |
|------|-----|------------|---------------|
| Python | Me | Easy | [Python → Me](#python-to-me) |
| TypeScript | Me | Easy | [TypeScript → Me](#typescript-to-me) |
| Rust | Solo | Medium | [Rust → Solo](#rust-to-solo) |
| Python | Solo | Hard | [Python → Solo](#python-to-solo) |
| Any → Duet | Medium | [Adding Verification](#adding-verification) |
| Duet → Ensemble | Medium | [Scaling to Agents](#scaling-to-agents) |

---

## Python to Me

### Why Migrate?

- **Explicit uncertainty** - Python floats don't carry confidence levels
- **Type safety** - Catch errors before runtime
- **Formal semantics** - Mathematically defined belief operations

### Step-by-Step

#### 1. Identify Probabilistic Code

Look for patterns like:

```python
# Python: Implicit uncertainty
confidence = 0.85
if confidence > 0.8:
    publish(result)
```

#### 2. Convert to Me Syntax

```me
# Me: Explicit epistemic type
belief result: Bool where confidence(0.85);

if confidence(result) > 0.8 {
    print("Publishing:", result);
}
```

#### 3. Add Distributions

```python
# Python: Magic numbers
prior = 0.5
posterior = prior * likelihood / evidence
```

```me
# Me: Named distributions
belief hypothesis: Bool where confidence(0.5);
hypothesis ~ Bernoulli(0.5);

observe(evidence="Study confirms", credibility=0.9);
# Posterior automatically updated
```

### Common Patterns

| Python Pattern | Me Equivalent |
|----------------|---------------|
| `prob = 0.7` | `belief x: Float where confidence(0.7)` |
| `if prob > threshold` | `if confidence(x) > threshold` |
| `combined = p1 * p2` | `result := fuse(b1, b2, rule=Dempster)` |

---

## TypeScript to Me

### Why Migrate?

- **Beyond types** - Me adds confidence to type information
- **Formal uncertainty** - Not just `null | T` but `Belief<T>`
- **Playground available** - Iterate quickly in browser

### Step-by-Step

#### 1. Identify Uncertainty Handling

```typescript
// TypeScript: Nullable or confidence field
interface Claim {
  value: boolean;
  confidence?: number;
}
```

#### 2. Convert to Me

```me
# Me: First-class belief type
belief claim: Bool where confidence(0.0);
```

#### 3. Replace Manual Propagation

```typescript
// TypeScript: Manual combination
function combine(a: Claim, b: Claim): Claim {
  return {
    value: a.value && b.value,
    confidence: a.confidence! * b.confidence!
  };
}
```

```me
# Me: Built-in fusion
result := fuse(claim_a, claim_b, rule=Dempster);
```

---

## Rust to Solo

### Why Migrate?

- **Epistemic extension** - Rust doesn't have belief types
- **Arena-first** - Solo optimizes for arena allocation patterns
- **Pipeline integration** - Solo feeds into Duet verification

### Key Differences

| Rust | Solo |
|------|------|
| `Box<T>`, `Rc<T>`, `Arc<T>` | Arena allocation preferred |
| No belief types | `belief x: Belief<T>` |
| `unsafe` allowed | `unsafe` forbidden |
| LLVM backend | QBE backend |

### Step-by-Step

#### 1. Replace Smart Pointers with Arenas

```rust
// Rust: Mixed allocation strategies
fn process(data: Vec<Box<Item>>) -> Vec<Box<Result>> {
    data.iter().map(|item| Box::new(transform(item))).collect()
}
```

```solo
// Solo: Arena-scoped allocation
fn process(data: Vec<Item>) -> Vec<Result> {
    arena {
        data.iter().map(|item| transform(item)).collect()
    }
}
```

#### 2. Add Epistemic Types

```rust
// Rust: No confidence tracking
struct Measurement {
    value: f64,
}
```

```solo
// Solo: With epistemic extension
belief measurement: Belief<f64> where confidence(0.95);
```

---

## Python to Solo

### Why Migrate?

- **Performance** - 10-100x speedup for numerical code
- **Memory safety** - No GC pauses, deterministic cleanup
- **Compile-time errors** - Catch bugs before deployment

### This is a Significant Rewrite

Python → Solo requires substantial refactoring:

1. Add explicit types to all functions
2. Convert dynamic allocation to arenas
3. Handle ownership explicitly
4. Replace exceptions with `Result<T, E>`

### Recommended Path

```
Python → Me (quick port) → Solo (optimize hot paths)
```

### Example

```python
# Python
def fuse_beliefs(masses):
    result = {}
    for m1 in masses:
        for m2 in masses:
            # ... fusion logic
    return normalize(result)
```

```solo
// Solo
fn fuse_beliefs(masses: &[BeliefMass]) -> Result<BeliefMass, FusionError> {
    arena {
        let mut result = HashMap::new();
        for m1 in masses {
            for m2 in masses {
                // ... fusion logic with explicit types
            }
        }
        normalize(result)
    }
}
```

---

## Adding Verification

### When to Use Duet

- **Safety-critical code** - Medical, financial, infrastructure
- **Complex algorithms** - Sorting, searching, cryptography
- **Regulatory requirements** - Auditable correctness proofs

### Migration Steps

#### 1. Identify Critical Functions

```solo
// Solo: Unverified
fn fuse_beliefs(m1: BeliefMass, m2: BeliefMass) -> BeliefMass {
    // implementation
}
```

#### 2. Add Verification Contracts

```duet
// Duet: With formal contracts
fn fuse_beliefs(m1: BeliefMass, m2: BeliefMass) -> BeliefMass where
    @verify: "valid_belief_mass(m1)",
    @verify: "valid_belief_mass(m2)",
    @verify: "valid_belief_mass(result)",
    @verify: "commutativity: fuse(m1, m2) == fuse(m2, m1)" {

    // Same implementation, now verified
}
```

#### 3. Run Verification

```bash
duet build --verify-level=2
```

---

## Scaling to Agents

### When to Use Ensemble

- **Distributed systems** - Multiple independent processes
- **Multi-source fusion** - Combining evidence from many sources
- **Fault tolerance** - Byzantine fault tolerance requirements

### Migration Steps

#### 1. Identify Agent Boundaries

Each independent decision-maker becomes an agent:

```duet
// Duet: Single-process function
fn verify_claim(sources: Vec<Source>) -> Belief {
    // ...
}
```

#### 2. Convert to Agent

```ensemble
// Ensemble: Distributed agent
agent FactCheckerAgent {
    sources: Vec<Source>,

    fn verify_claim(&self, claim: &Claim) -> Belief {
        // Same logic, now distributed
    }
}
```

#### 3. Add Orchestration

```ensemble
comptime orchestrate Newsroom {
    agents: [FactCheckerAgent; 10],
    topology: Ring,
    fusion: Dempster,
    consensus: Threshold(0.85),
}
```

---

## Common Migration Challenges

### Challenge 1: Dynamic Typing

**Problem:** Python/JS code relies on duck typing.

**Solution:** Add type annotations first, then migrate.

### Challenge 2: Null Handling

**Problem:** `null` scattered throughout codebase.

**Solution:** Use `Option<T>` in Solo, model as uncertainty in Me.

### Challenge 3: Exceptions

**Problem:** Try/catch everywhere.

**Solution:** Convert to `Result<T, E>` pattern.

### Challenge 4: Global State

**Problem:** Mutable global variables.

**Solution:** Pass state explicitly, use arenas for shared data.

---

## Getting Help

- **Questions:** Open an issue with the `migration` label
- **Examples:** See `examples/` directory for each dialect
- **Community:** Discussions on GitLab

---

## Contributing

Found a common migration pattern? Submit a PR to expand this guide!

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.
