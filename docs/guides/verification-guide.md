# Verification Guide

**Purpose:** Formal verification with Duet dialect and SPARK integration
**Audience:** Developers writing safety-critical code
**Status:** Draft - Expanding as Duet implementation progresses

---

## Overview

This guide explains how to add formal verification to your My Language code using the Duet dialect. Duet integrates with SPARK/Ada provers to generate machine-checkable correctness proofs.

---

## Prerequisites

- Familiarity with Solo dialect syntax
- Basic understanding of formal logic (predicates, quantifiers)
- (Optional) Experience with SPARK, Dafny, or similar tools

### Tool Requirements

| Tool | Purpose | Status |
|------|---------|--------|
| Duet compiler | Parse and type-check Duet code | Planned |
| SPARK/GNATprove | Generate and check proofs | External dep |
| Z3 | SMT solving | External dep |

---

## Verification Concepts

### What is Formal Verification?

Formal verification uses mathematical proofs to guarantee program properties:

- **Functional correctness:** Does the code do what it should?
- **Memory safety:** No buffer overflows, use-after-free
- **Termination:** Does the program always halt?
- **Absence of runtime errors:** No division by zero, overflow

### Verification vs Testing

| Testing | Verification |
|---------|--------------|
| Finds bugs | Proves absence of bugs |
| Finite cases | All possible inputs |
| "Works on my machine" | Works everywhere (mathematically) |
| Fast feedback | Slower, more rigorous |

### When to Verify

Use Duet verification for:

- **Safety-critical systems** - Medical devices, aviation, nuclear
- **Security-sensitive code** - Cryptography, authentication
- **Financial calculations** - Trading, accounting, billing
- **Core algorithms** - Sorting, searching, parsing

---

## Duet Verification Syntax

### Basic Contracts

```duet
fn function_name(params) -> ReturnType where
    @verify: "precondition",
    @verify: "postcondition" {
    // implementation
}
```

### Preconditions

Preconditions specify what must be true **before** the function runs:

```duet
fn divide(a: i32, b: i32 where b != 0) -> i32 where
    @verify: "precondition: b != 0" {
    a / b
}
```

### Postconditions

Postconditions specify what must be true **after** the function runs:

```duet
fn abs(x: i32) -> i32 where
    @verify: "postcondition: result >= 0",
    @verify: "postcondition: result == x || result == -x" {
    if x < 0 { -x } else { x }
}
```

### Loop Invariants

For loops, specify invariants that hold on every iteration:

```duet
fn sum(arr: &[i32]) -> i32 where
    @verify: "postcondition: result == sum_of(arr)" {

    let mut total = 0;

    for i in 0..arr.len() {
        @invariant: "total == sum_of(arr[0..i])";
        total += arr[i];
    }

    total
}
```

---

## Verification Levels

Duet supports multiple verification levels for different stages of development:

| Level | Checks | Time | Use Case |
|-------|--------|------|----------|
| 0 (None) | None | Fast | Prototyping |
| 1 (Flow) | Data flow | <1s | Development |
| 2 (Proof) | Auto proofs | 10-60s | Pre-commit |
| 3 (Full) | Interactive | Minutes+ | Release |

### Running Verification

```bash
# Quick check during development
duet build --verify-level=1

# Full verification before merge
duet build --verify-level=2

# Release verification with interactive proofs
duet build --verify-level=3
```

---

## Common Verification Patterns

### Pattern 1: Numeric Safety

Verify no overflow or division by zero:

```duet
fn safe_divide(a: i32, b: i32) -> Option<i32> where
    @verify: "postcondition: b == 0 => result.is_none()",
    @verify: "postcondition: b != 0 => result == Some(a / b)" {

    if b == 0 {
        None
    } else {
        Some(a / b)
    }
}
```

### Pattern 2: Array Bounds

Verify no out-of-bounds access:

```duet
fn get_safe(arr: &[T], index: usize) -> Option<&T> where
    @verify: "postcondition: index >= arr.len() => result.is_none()",
    @verify: "postcondition: index < arr.len() => result == Some(&arr[index])" {

    if index < arr.len() {
        Some(&arr[index])
    } else {
        None
    }
}
```

### Pattern 3: Sorting Correctness

Verify sorting produces sorted, permuted output:

```duet
fn sort<T: Ord>(arr: &mut [T]) where
    @verify: "postcondition: sorted(arr)",
    @verify: "postcondition: permutation(old(arr), arr)" {

    // Implementation...
}
```

### Pattern 4: Belief Mass Validity

Verify Dempster-Shafer invariants:

```duet
fn fuse_beliefs(m1: BeliefMass, m2: BeliefMass) -> BeliefMass where
    @verify: "precondition: valid_belief_mass(m1)",
    @verify: "precondition: valid_belief_mass(m2)",
    @verify: "postcondition: valid_belief_mass(result)",
    @verify: "postcondition: sum(result.values()) ≈ 1.0" {

    // Implementation...
}

// Helper specification
@spec fn valid_belief_mass(m: BeliefMass) -> bool {
    m.values().all(|v| v >= 0.0 && v <= 1.0) &&
    (m.values().sum() - 1.0).abs() < 1e-6
}
```

---

## AI-Assisted Verification

Duet supports `@synth` holes where AI generates verified implementations:

### Basic Synthesis

```duet
intent("Implement binary search")
fn binary_search<T: Ord>(arr: &[T], target: &T) -> Option<usize> where
    @verify: "precondition: sorted(arr)",
    @verify: "postcondition: result.is_some() => arr[result.unwrap()] == *target",
    @verify: "postcondition: result.is_none() => !arr.contains(target)" {

    @synth { }  // AI fills this in
}
```

### Synthesis with Hints

```duet
intent("Implement quicksort with median-of-3 pivot")
fn quicksort<T: Ord>(arr: &mut [T]) where
    @verify: "postcondition: sorted(arr)" {

    @synth(hints=["use Hoare partition", "recurse on smaller half first"]) { }
}
```

### Synthesis Strategies

| Strategy | Description |
|----------|-------------|
| `exhaustive` | Try all approaches, pick proven one |
| `heuristic` | Use LLM to guess, then verify |
| `interactive` | Ask human for guidance |

---

## Debugging Failed Proofs

### Understanding Counterexamples

When verification fails, the prover provides a counterexample:

```
Verification failed at src/main.duet:42
Counterexample:
  a = 2147483647
  b = 1
  result = -2147483648  (OVERFLOW!)

Expected: result >= 0
```

### Common Proof Failures

| Failure | Cause | Solution |
|---------|-------|----------|
| Overflow | Integer bounds | Add bounds checks or use wider type |
| Division by zero | Missing guard | Add precondition or runtime check |
| Array bounds | Index too large | Add bounds precondition |
| Loop invariant | Wrong invariant | Strengthen or weaken invariant |
| Termination | Infinite loop | Add decreasing measure |

### Proof Debugging Commands

```bash
# Show detailed proof trace
duet debug-proof src/main.duet:42

# Interactive proof session
duet prove --interactive src/main.duet

# Show all proof obligations
duet obligations src/main.duet
```

---

## SPARK Integration

Duet compiles to SPARK/Ada for proof generation:

### Translation Example

```duet
// Duet
fn abs(x: i32) -> i32 where
    @verify: "result >= 0" {
    if x < 0 { -x } else { x }
}
```

```ada
-- Generated SPARK
function Abs_Value (X : Integer) return Integer
  with Post => Abs_Value'Result >= 0
is
begin
   if X < 0 then
      return -X;
   else
      return X;
   end if;
end Abs_Value;
```

### Running GNATprove

```bash
# Duet generates SPARK, then calls GNATprove
duet build --backend=spark

# Or run GNATprove directly
gnatprove -P project.gpr --level=2
```

---

## Best Practices

### 1. Start Small

Begin with simple functions, then expand:

```duet
// Start here
fn add(a: i32, b: i32) -> i32 where
    @verify: "no_overflow(a, b, result)" {
    a + b
}
```

### 2. Verify Incrementally

Don't try to verify everything at once:

```bash
# Verify one file at a time
duet build --verify-level=2 src/critical.duet

# Skip non-critical code
duet build --skip-verify=src/utils.duet
```

### 3. Use Specifications

Separate specification from implementation:

```duet
@spec fn sorted<T: Ord>(arr: &[T]) -> bool {
    arr.windows(2).all(|w| w[0] <= w[1])
}

@spec fn permutation<T>(a: &[T], b: &[T]) -> bool {
    a.len() == b.len() && /* multiset equality */
}
```

### 4. Document Assumptions

Make preconditions explicit:

```duet
// Good: Clear precondition
fn process(data: &[u8] where data.len() > 0) -> Result { ... }

// Bad: Hidden assumption
fn process(data: &[u8]) -> Result { ... }  // Crashes on empty!
```

---

## Resources

### Documentation

- [Duet Dialect Specification](../dialects/duet.md)
- [SPARK User's Guide](https://docs.adacore.com/spark2014-docs/html/ug/)
- [Z3 Tutorial](https://microsoft.github.io/z3guide/)

### Examples

- `examples/duet/verified_sort.duet` - Verified quicksort
- `examples/duet/belief_fusion.duet` - Verified Dempster-Shafer
- `examples/duet/parser.duet` - Verified recursive descent parser

### Getting Help

- Open an issue with the `verification` label
- Check existing proofs in `test/proofs/`

---

## Contributing

Found a useful verification pattern? Submit a PR!

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.
