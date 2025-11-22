# Duet Dialect Specification

**Version:** 0.1.0-draft
**Status:** Specification Phase (No Implementation Yet)
**Parent Language:** My Language Family
**Paradigm:** Human-AI Co-programming with Formal Verification

---

## Table of Contents

1. [Overview](#overview)
2. [Design Philosophy](#design-philosophy)
3. [Syntax](#syntax)
4. [Type System](#type-system)
5. [Verification System](#verification-system)
6. [AI Integration](#ai-integration)
7. [Compilation Model](#compilation-model)
8. [Examples](#examples)
9. [Tooling](#tooling)
10. [Implementation Plan](#implementation-plan)

---

## Overview

**Duet** is the third dialect in the My Language family, designed for **human-AI collaborative programming** with **formal verification guarantees**. It extends Solo's type safety with:

- **Intent declarations** - High-level specifications of what code should do
- **Verification contracts** - Formal properties checked at compile-time
- **Synthesis holes** - Placeholders where AI fills in implementation
- **Proof obligations** - Mathematical guarantees about correctness

### Key Features

| Feature | Description | Example |
|---------|-------------|---------|
| **Intent Declarations** | Natural language spec | `intent("sort array in O(n log n)")` |
| **Verification Markers** | Formal properties | `@verify: "sorted(result)"` |
| **Synthesis Holes** | AI-filled code | `@synth { /* AI implements */ }` |
| **Type Refinements** | Dependent types | `x: Int where x > 0` |
| **Contract Attributes** | Function-level specs | `#[ai_optimize]`, `#[ai_test]` |
| **Two-Stage Compilation** | Human + AI passes | Stage 1: Types, Stage 2: Synthesis |

### Relationship to Other Dialects

```
Me      →  Solo     →  Duet         →  Ensemble
(belief)  (systems)   (verification)   (orchestration)

Epistemic  Memory     AI-Assisted      Multi-Agent
Types      Safe       Synthesis        Coordination
```

**Duet's Role:**
- **Extends Solo** with formal verification (SPARK-based)
- **Enables AI assistance** via synthesis holes and intent declarations
- **Bridges to Ensemble** by providing verified agent behaviors

---

## Design Philosophy

### 1. Graduated Autonomy

Duet supports a **spectrum of AI involvement**:

```duet
// Fully manual (no AI)
fn fibonacci(n: usize) -> usize {
    if n <= 1 { n } else { fibonacci(n-1) + fibonacci(n-2) }
}

// AI-optimized (human writes, AI optimizes)
#[ai_optimize]
fn fibonacci(n: usize) -> usize {
    if n <= 1 { n } else { fibonacci(n-1) + fibonacci(n-2) }
}
// AI suggests memoization or closed-form formula

// AI-synthesized (AI writes, human verifies)
intent("Compute Fibonacci number efficiently")
fn fibonacci(n: usize) -> usize where
    @verify: "result == fib(n)",
    @verify: "time_complexity <= O(log n)" {
    @synth { /* AI fills in matrix exponentiation */ }
}
```

### 2. Proof-Carrying Code

All AI-synthesized code must include **machine-checkable proofs**:

```duet
@synth {
    // AI generates implementation
    let phi = (1.0 + 5.0.sqrt()) / 2.0;
    ((phi.powi(n as i32) - (-phi).powi(-(n as i32))) / 5.0.sqrt()).round() as usize
}
// Proof: Uses Binet's formula, proven correct via SPARK
```

### 3. Explainability

Every verification and synthesis step is **traceable**:

```duet
#[ai_explain]
fn complex_algorithm(data: &[f64]) -> Result<Vec<f64>, Error> {
    @synth { /* AI fills in */ }
}

// Compiler output:
// [AI Explanation]
// Algorithm: Dempster-Shafer belief fusion
// Time Complexity: O(n²) where n = |data|
// Memory: O(n) for intermediate belief masses
// Correctness: Proven via SPARK (see proof trace below)
// [Proof Trace]
// 1. Precondition: data.len() > 0 ✓
// 2. Loop invariant: all belief masses sum to 1.0 ✓
// 3. Postcondition: result.len() == data.len() ✓
```

---

## Syntax

### Intent Declarations

**Purpose:** Natural language specification of desired behavior

**Syntax:**
```duet
intent("<natural language description>")
```

**Semantics:**
- Provides context to AI synthesizer
- Not enforced at runtime (only used for synthesis)
- Can reference domain knowledge (e.g., algorithms, design patterns)

**Examples:**
```duet
intent("Implement Dempster-Shafer belief combination")
intent("Sort array in-place with O(1) space, O(n log n) time")
intent("Parse JSON with proper error handling for malformed input")
```

### Verification Markers

**Purpose:** Formal properties checked at compile-time

**Syntax:**
```duet
@verify: "<property>"
@verify: "property_name: <expression>"
```

**Property Language:**
- **Assertions:** `x > 0`, `result.len() == input.len()`
- **Mathematical functions:** `sorted(result)`, `permutation(input, result)`
- **Complexity bounds:** `time_complexity <= O(n log n)`
- **Safety properties:** `no_panic`, `no_overflow`, `no_dangling_pointers`

**Examples:**
```duet
fn binary_search<T: Ord>(arr: &[T], target: &T) -> Option<usize> where
    @verify: "precondition: sorted(arr)",
    @verify: "postcondition: result.is_some() ⇒ arr[result.unwrap()] == *target",
    @verify: "postcondition: result.is_none() ⇒ ∀i. arr[i] != *target" {
    // implementation
}
```

### Synthesis Holes

**Purpose:** Placeholders where AI fills in implementation

**Syntax:**
```duet
@synth { /* optional human-provided skeleton */ }
@synth(strategy="exhaustive") { }
@synth(hints=["use dynamic programming"]) { }
```

**Strategies:**
- `exhaustive` - Enumerate all solutions, pick provably correct one
- `heuristic` - Use neural model to generate candidate, then verify
- `interactive` - Ask human for guidance during synthesis

**Examples:**
```duet
intent("Implement quicksort with Hoare partition scheme")
fn quicksort<T: Ord>(arr: &mut [T]) where
    @verify: "postcondition: sorted(arr)",
    @verify: "postcondition: permutation(old(arr), arr)" {

    @synth(strategy="heuristic", hints=["use recursion", "pivot = median of 3"]) {
        // AI fills in:
        // 1. Base case
        // 2. Pivot selection
        // 3. Partition
        // 4. Recursive calls
    }
}
```

### Type Refinements

**Purpose:** Dependent types that constrain values

**Syntax:**
```duet
x: Type where <predicate>
```

**Examples:**
```duet
// Positive integers
fn factorial(n: usize where n <= 20) -> usize {
    // Implementation
}

// Non-empty vectors
fn median(data: Vec<f64> where data.len() > 0) -> f64 {
    // Implementation
}

// Normalized belief mass (probabilities sum to 1)
type BeliefMass = HashMap<String, f64> where {
    @verify: "sum(self.values()) ≈ 1.0"  // Allow floating-point epsilon
};
```

### Contract Attributes

**Purpose:** Function-level specifications and hints

**Syntax:**
```duet
#[ai_optimize]       // AI suggests optimizations
#[ai_test]           // AI generates test cases
#[ai_prove]          // AI generates formal proof
#[ai_explain]        // AI provides natural language explanation
#[no_synth]          // Disable AI synthesis for this function
```

**Examples:**
```duet
#[ai_optimize]
#[ai_test(count=100, coverage="branch")]
fn compute_belief_fusion(m1: BeliefMass, m2: BeliefMass) -> BeliefMass {
    // Human implementation
}

// Compiler output:
// [AI Optimization Suggestions]
// 1. Precompute intersection sets (saves 30% time)
// 2. Use parallel iteration for large frames (>1000 elements)
// 3. Cache conflict normalization factor
//
// [AI Generated Tests]
// test_empty_belief_masses() ✓
// test_disjoint_belief_masses() ✓
// test_high_conflict_warning() ✓
// ... (97 more tests)
```

### Two-Stage Functions

**Purpose:** Separate human-written and AI-synthesized parts

**Syntax:**
```duet
fn function_name(...) -> ReturnType {
    // Stage 1: Human-written setup
    let x = compute_initial_state();

    @synth {
        // Stage 2: AI-synthesized core algorithm
    }

    // Stage 1: Human-written teardown
    cleanup(x);
}
```

**Example:**
```duet
fn parse_my_language(source: &str) -> Result<AST, ParseError> {
    // Human: Lexing (well-understood)
    let tokens = lex(source)?;

    intent("Parse tokens into AST using recursive descent")
    @synth(hints=["use Pratt parsing for expressions"]) {
        // AI: Parsing (tedious, error-prone)
    }

    // Human: Validation (domain-specific)
    validate_ast(&ast)?;
    Ok(ast)
}
```

---

## Type System

Duet **extends Solo's type system** with:

### 1. Refinement Types

**Definition:** Types + predicates

```duet
type NonZero = i32 where self != 0;
type SortedVec<T> = Vec<T> where sorted(self);
type Probability = f64 where 0.0 <= self && self <= 1.0;
```

**Type Checking:**
- **Static:** Check predicate at compile-time when possible
- **Dynamic:** Insert runtime checks when static verification fails
- **Proof:** Require formal proof for complex predicates

### 2. Effect Types

**Definition:** Track side effects (IO, mutation, non-termination)

```duet
fn pure_function(x: i32) -> i32 pure {
    x * 2  // OK: no effects
}

fn impure_function(x: i32) -> i32 {
    println!("x = {}", x);  // Effect: IO
    x * 2
}
```

**Effect Markers:**
- `pure` - No side effects (referentially transparent)
- `io` - Performs I/O
- `mut` - Mutates arguments or global state
- `!` - May not terminate (loops without proof of termination)

### 3. Session Types

**Definition:** Protocols for agent communication (used in Ensemble)

```duet
type ReporterProtocol = Send<Claim, Receive<Verification, End>>;

fn reporter_agent(channel: Chan<ReporterProtocol>) {
    let claim = gather_evidence();
    channel.send(claim);
    let verification = channel.receive();
    // Protocol enforces: cannot send again without receiving first
}
```

---

## Verification System

Duet uses **SPARK/Ada** for formal verification:

### 1. Proof Obligations

**Generated Automatically:**
- **Preconditions** - Arguments satisfy @verify contracts
- **Postconditions** - Return values satisfy @verify contracts
- **Loop invariants** - Inferred or user-provided
- **Overflow checks** - All arithmetic operations safe

**Example:**
```duet
fn divide(a: i32, b: i32 where b != 0) -> i32 {
    a / b
}

// Generated proof obligation:
// Prove: ∀ a b. (b != 0) ⇒ (a / b) is well-defined and no overflow
```

### 2. Verification Levels

| Level | Checks | Performance | Use Case |
|-------|--------|-------------|----------|
| **0 (None)** | None | Fast compile | Prototyping |
| **1 (Flow)** | Data flow analysis | <1s overhead | Development |
| **2 (Proof)** | Automatic proofs | 10-60s overhead | Pre-commit |
| **3 (Full)** | Interactive proofs | Minutes-hours | Release builds |

**Usage:**
```bash
duet build --verify-level=2
```

### 3. Solver Integration

**Supported Solvers:**
- **Z3** (Microsoft) - SMT solver for first-order logic
- **CVC5** - SMT solver with induction
- **Vampire** - Automated theorem prover
- **Coq** - Interactive proof assistant (for Level 3)

**Example Proof:**
```duet
fn abs(x: i32) -> i32 where
    @verify: "result >= 0",
    @verify: "result == x ∨ result == -x" {

    if x < 0 { -x } else { x }
}

// Z3 proof (automatic):
// Case 1: x < 0
//   result = -x
//   x < 0 ⇒ -x > 0  ✓ (result >= 0)
//   result == -x     ✓
// Case 2: x >= 0
//   result = x
//   x >= 0 ⇒ result >= 0  ✓
//   result == x            ✓
// QED
```

---

## AI Integration

### 1. Synthesis Pipeline

```
Intent → Spec → Candidates → Verify → Rank → Select
  ↓       ↓        ↓           ↓        ↓      ↓
 Human  Human    AI (LLM)   SPARK    AI     Human
```

**Steps:**
1. **Intent:** Human writes natural language description
2. **Spec:** Human writes @verify contracts
3. **Candidates:** AI generates N implementations (N=10 default)
4. **Verify:** SPARK proves correctness of each candidate
5. **Rank:** AI ranks by readability, performance, simplicity
6. **Select:** Human chooses best or requests regeneration

### 2. Model Fine-Tuning

**Training Data:**
- **Verified code:** Solo + SPARK proofs from open-source projects
- **Synthetic data:** Generated by enumerating specs and synthesizing implementations

**Model Architecture:**
- **Base:** Codex/StarCoder (pretrained on code)
- **Fine-tuning:** LoRA adapters for Duet syntax and SPARK proofs
- **Context:** 8K tokens (enough for full functions + dependencies)

### 3. Interaction Modes

**Batch Mode (Default):**
```bash
duet build  # Synthesizes all @synth holes, asks for confirmation
```

**Interactive Mode:**
```bash
duet build --interactive
# For each @synth hole:
# > AI generated 5 candidates. Show all? [y/N]
# > Select candidate (1-5) or regenerate [r]:
```

**Watch Mode (TDD-style):**
```bash
duet watch  # Recompiles on file change, shows verification status live
```

---

## Compilation Model

### Stage 1: Human-Driven (Type Checking + Verification)

```
Source Code
    ↓
Lexer → Tokens
    ↓
Parser → AST
    ↓
Type Checker → Typed AST
    ↓
Verification → Proof Obligations
    ↓
SPARK Prover → Verified AST (with @synth holes)
```

### Stage 2: AI-Driven (Synthesis + Re-Verification)

```
Verified AST with @synth holes
    ↓
Intent Extractor → Natural Language Specs
    ↓
LLM Synthesizer → Candidate Implementations
    ↓
SPARK Prover (again) → Filter Invalid Candidates
    ↓
Ranking Model → Ranked Valid Candidates
    ↓
Human Selection → Final AST
    ↓
Code Generator (uses Solo backend) → Executable
```

### Artifacts

```
project/
├── src/
│   └── main.duet         # Source code
├── target/
│   ├── verified/
│   │   └── main.mlw      # WhyML (SPARK input)
│   ├── synth/
│   │   ├── candidate_1.duet
│   │   ├── candidate_2.duet
│   │   └── ...
│   ├── proofs/
│   │   ├── abs.why       # Proof scripts
│   │   └── abs.v         # Coq proofs (if Level 3)
│   └── bin/
│       └── main          # Final executable
```

---

## Examples

### Example 1: Dempster-Shafer Belief Fusion

```duet
use std::collections::HashMap;

type Frame = HashSet<String>;
type BeliefMass = HashMap<Frame, Probability>;

intent("Combine two belief masses using Dempster's rule of combination")
fn fuse_beliefs(m1: BeliefMass, m2: BeliefMass) -> BeliefMass where
    @verify: "precondition: same_frame(m1, m2)",
    @verify: "precondition: valid_belief_mass(m1)",
    @verify: "precondition: valid_belief_mass(m2)",
    @verify: "postcondition: valid_belief_mass(result)",
    @verify: "postcondition: conflict(result) <= conflict(m1) + conflict(m2)",
    @verify: "commutativity: fuse_beliefs(m1, m2) == fuse_beliefs(m2, m1)" {

    @synth(strategy="heuristic", hints=["normalize by (1 - conflict)"]) {
        // AI generates:
        let mut result = HashMap::new();

        for (set_a, mass_a) in &m1 {
            for (set_b, mass_b) in &m2 {
                let intersection = set_a.intersection(set_b).cloned().collect();
                if !intersection.is_empty() {
                    *result.entry(intersection).or_insert(0.0) += mass_a * mass_b;
                }
            }
        }

        let conflict: f64 = m1.iter().flat_map(|(a, ma)| {
            m2.iter().filter_map(move |(b, mb)| {
                if a.is_disjoint(b) { Some(ma * mb) } else { None }
            })
        }).sum();

        if conflict >= 0.9 {
            warn!("High conflict ({:.2}), result may be unreliable", conflict);
        }

        for mass in result.values_mut() {
            *mass /= 1.0 - conflict;
        }

        result
    }
}

// Helper verification functions
#[ai_prove]
fn valid_belief_mass(m: &BeliefMass) -> bool {
    let sum: f64 = m.values().sum();
    (sum - 1.0).abs() < 1e-6  // Floating-point tolerance
}

#[ai_prove]
fn same_frame(m1: &BeliefMass, m2: &BeliefMass) -> bool {
    let all_elements_1: Frame = m1.keys().flatten().cloned().collect();
    let all_elements_2: Frame = m2.keys().flatten().cloned().collect();
    all_elements_1 == all_elements_2
}
```

### Example 2: Verified Sorting

```duet
intent("Sort array in-place using optimized quicksort")
fn quicksort<T: Ord>(arr: &mut [T]) where
    @verify: "postcondition: sorted(arr)",
    @verify: "postcondition: permutation(old(arr), arr)",
    @verify: "time_complexity: O(n log n) expected, O(n²) worst-case",
    @verify: "space_complexity: O(log n) for recursion stack",
    @verify: "termination: proven via measure(arr.len())" {

    @synth(strategy="exhaustive", hints=["use median-of-3 pivot"]) {
        // AI explores search space:
        // - Lomuto partition? (simpler, but slower)
        // - Hoare partition? (faster, but complex)
        // - Median-of-3? (avoids worst case on sorted input)
        //
        // AI selects Hoare partition with median-of-3 based on:
        // - Proof of correctness (SPARK verified all 3)
        // - Performance benchmarks (Hoare 15% faster)
        // - Code simplicity (reasonable)
    }
}

// SPARK generates loop invariants automatically:
// Invariant: ∀ i < left. arr[i] <= pivot
// Invariant: ∀ j > right. arr[j] >= pivot
```

### Example 3: Parser with Error Recovery

```duet
intent("Parse My Language source code with helpful error messages")
fn parse(source: &str) -> Result<AST, ParseError> where
    @verify: "postcondition: result.is_ok() ⇒ valid_ast(result.unwrap())",
    @verify: "error_recovery: parse_partial_on_error",
    @verify: "error_messages: include_line_numbers_and_suggestions" {

    let tokens = lex(source)?;

    @synth(hints=["use Pratt parsing", "error recovery at statement boundaries"]) {
        // AI generates recursive descent parser with error recovery
    }
}

#[ai_test(count=1000, corpus="real-world-my-language-code")]
#[ai_test(count=100, corpus="intentionally-malformed-input")]
fn test_parse() {
    // AI generates tests from corpus + fuzzing
}
```

---

## Tooling

### IDE Integration

**VS Code Extension:** `duet-lang`

Features:
- **Inline synthesis**: See AI-generated candidates as you type
- **Proof status**: Green checkmarks for verified functions
- **Error explanations**: Click on failed proofs to see counterexamples
- **Refactoring**: AI suggests safe refactorings (proven to preserve semantics)

### REPL

```bash
duet repl
```

```duet-repl
> intent("compute factorial")
> fn factorial(n: usize where n <= 20) -> usize { @synth { } }
[AI] Generated 3 candidates. Select:
  1. Iterative (100 LOC, O(n) time, proven ✓)
  2. Recursive (10 LOC, O(n) time, proven ✓)
  3. Lookup table (50 LOC, O(1) time, proven ✓)
> 3
[AI] Using lookup table for factorial.
> factorial(10)
3628800
```

### Debugger

**Proof Debugger:**
```bash
duet debug-proof src/main.duet:42
```

Shows:
- Which verification condition failed
- Counterexample from SMT solver
- Suggested fixes (from AI)

---

## Implementation Plan

### Phase 1: Spec + Type System (Q2 2025, 3 months)

- [ ] Finalize syntax (this document)
- [ ] Implement lexer + parser (extend Solo's)
- [ ] Type checker for refinement types
- [ ] Integration with SPARK (compile Duet → Ada subset)

**Deliverable:** Type-checked Duet programs (no synthesis yet)

### Phase 2: Verification (Q3 2025, 3 months)

- [ ] Generate SPARK contracts from @verify
- [ ] Integrate Z3 solver
- [ ] Proof obligation generation
- [ ] Error reporting with counterexamples

**Deliverable:** Verified Duet programs (manual implementation, no AI)

### Phase 3: Synthesis (Q4 2025, 3 months)

- [ ] Fine-tune LLM on Duet + SPARK corpus
- [ ] Implement @synth hole filling
- [ ] Candidate ranking model
- [ ] Interactive selection UI

**Deliverable:** AI-synthesized Duet programs with human oversight

### Phase 4: Tooling (Q1 2026, 3 months)

- [ ] VS Code extension
- [ ] REPL with synthesis
- [ ] Proof debugger
- [ ] Documentation generator

**Deliverable:** Production-ready Duet toolchain

---

## Open Questions

1. **Synthesis Quality:** Can LLMs reliably generate correct implementations for @synth holes?
   - **Mitigation:** Use verification to filter out wrong candidates
   - **Fallback:** If no candidates pass verification, ask human to provide more hints

2. **Proof Complexity:** How long do SPARK proofs take for realistic programs?
   - **Empirical:** Run benchmarks on Dempster-Shafer code
   - **Fallback:** Allow human to skip proofs (with warnings) for prototyping

3. **User Experience:** Is the two-stage compilation acceptable?
   - **Trade-off:** Compile time (slower) vs. correctness (higher)
   - **Optimization:** Cache verified @synth candidates across rebuilds

---

## References

1. **SPARK Pro User Guide** - AdaCore (formal verification in Ada)
2. **Program Synthesis from Examples** - Sumit Gulwani (Microsoft)
3. **Refinement Types for ML** - Tim Freeman, Frank Pfenning (CMU)
4. **Contracts for Higher-Order Functions** - Robert Bruce Findler et al. (Racket)
5. **The Lean Theorem Prover** - Leonardo de Moura (formal verification + tactics)

---

## Changelog

### 2025-11-22 - Initial Draft
- Complete syntax specification
- Verification system design
- AI integration plan
- 3 detailed examples (Dempster-Shafer, sorting, parsing)
- 12-month implementation roadmap

---

**Next Steps:** Prototype Stage 1 compiler (lexer + parser + type checker) in Rust.

