# Solo Dialect Specification

**Version:** 0.1.0-alpha
**Status:** 40% Complete (Lexer Working, Parser In Progress)
**Parent Language:** My Language Family
**Paradigm:** Systems Programming with Affine Types

---

## Specification Status

### FROZEN (Stable API - Breaking Changes Require RFC)

| Feature | Status | Since | Description |
|---------|--------|-------|-------------|
| **Keywords** | Frozen | v0.1.0 | `fn`, `let`, `mut`, `if`, `else`, `while`, `return`, `belief` |
| **Primitive Types** | Frozen | v0.1.0 | `i32`, `i64`, `u32`, `u64`, `f32`, `f64`, `bool`, `String` |
| **Function Syntax** | Frozen | v0.1.0 | `fn name(args) -> Type { body }` |
| **Let Bindings** | Frozen | v0.1.0 | `let x = expr;`, `let mut x = expr;` |
| **Operators** | Frozen | v0.1.0 | `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=` |
| **Arrow Operators** | Frozen | v0.1.0 | `->` (return type), `=>` (match arm) |
| **Comments** | Frozen | v0.1.0 | `// line`, `/* block */` |
| **Tilde Operator** | Frozen | v0.1.0 | `~` for distributions (epistemic extension) |

### EXPLORATORY (Subject to Change)

| Feature | Status | Target | Description |
|---------|--------|--------|-------------|
| **Affine Types** | Exploratory | v0.2.0 | Move semantics, linear ownership |
| **Arena Allocation** | Exploratory | v0.2.0 | `arena { ... }` blocks |
| **Struct Definitions** | Exploratory | v0.2.0 | `struct Name { fields }` |
| **Enum Definitions** | Exploratory | v0.2.0 | `enum Name { Variants }` |
| **Pattern Matching** | Exploratory | v0.3.0 | `match expr { patterns }` |
| **Generics** | Exploratory | v0.3.0 | `fn name<T>(x: T) -> T` |
| **Lifetimes** | Exploratory | v0.3.0 | `'a` lifetime annotations |
| **Trait System** | Exploratory | v0.4.0 | `trait Name { methods }` |
| **Result Type** | Exploratory | v0.2.0 | `Result<T, E>` for error handling |
| **Option Type** | Exploratory | v0.2.0 | `Option<T>` for nullable values |
| **Path Syntax** | Exploratory | v0.2.0 | `::` for module paths |

---

## Table of Contents

1. [Overview](#overview)
2. [Design Philosophy](#design-philosophy)
3. [Lexical Structure](#lexical-structure)
4. [Syntax](#syntax)
5. [Type System](#type-system)
6. [Memory Model](#memory-model)
7. [Epistemic Extension](#epistemic-extension)
8. [Implementation Status](#implementation-status)
9. [Examples](#examples)

---

## Overview

**Solo** is the systems programming dialect in the My Language family, designed for **performance-critical code** with **compile-time memory safety**. It provides:

- **Affine types** - Linear ownership prevents use-after-free
- **Arena allocation** - Deterministic memory management without GC
- **Zero-cost abstractions** - No runtime overhead for safety
- **Epistemic extension** - Belief types from Me dialect

### Pipeline Position

```
┌─────────────────────────────────────────────────────────────────┐
│                    MY LANGUAGE PIPELINE                         │
├─────────┬─────────┬─────────┬──────────┬───────────────────────┤
│   Me    │    →    │  Solo   │    →     │  Duet  →  Ensemble    │
│         │ exports │ (here)  │ verifies │                       │
├─────────┼─────────┼─────────┼──────────┼───────────────────────┤
│Epistemic│  types  │ Systems │  proofs  │ Multi-Agent           │
│ Types   │    +    │   +     │    +     │ Orchestration         │
│         │ beliefs │ Memory  │    AI    │                       │
└─────────┴─────────┴─────────┴──────────┴───────────────────────┘
```

**Solo's Role:**
- **Performance backend** for Me prototypes
- **Memory-safe implementation** language
- **Foundation** for Duet verification

---

## Design Philosophy

### 1. Rust-Like Safety, Ada-Like Clarity

Solo combines Rust's ownership model with Ada's readability:

```solo
// Clear, explicit ownership
fn process(data: Buffer) -> Result<Vec<u8>, Error> {
    let processed = transform(data);  // data moved here
    Ok(processed)
}
```

### 2. No Garbage Collection

Memory is managed via **arenas** and **affine types**:

```solo
arena {
    let buffer = allocate(1024);
    process(buffer);
    // buffer automatically freed at arena exit
}
```

### 3. Epistemic Extension

Solo inherits belief types from Me:

```solo
// Belief type with confidence
belief claim: Belief<bool> where confidence(0.85);
claim ~ Bernoulli(0.7);
```

---

## Lexical Structure

### Keywords (FROZEN)

```
fn      let     mut     if      else    while   return
struct  enum    impl    trait   for     in      loop
break   continue match  pub     use     mod     const
static  type    where   as      ref     self    Self
true    false   belief
```

### Operators (FROZEN)

| Operator | Meaning |
|----------|---------|
| `+` `-` `*` `/` | Arithmetic |
| `==` `!=` | Equality |
| `<` `>` `<=` `>=` | Comparison |
| `&&` `\|\|` `!` | Logical |
| `&` `\|` `^` | Bitwise |
| `->` | Return type |
| `=>` | Match arm |
| `::` | Path separator |
| `~` | Distribution (epistemic) |

### Literals

```solo
// Integers
42          // i32 (default)
42i64       // explicit i64
0xFF        // hex
0b1010      // binary

// Floats
3.14        // f64 (default)
3.14f32     // explicit f32

// Strings
"hello"     // String
'c'         // char

// Booleans
true false
```

### Comments (FROZEN)

```solo
// Line comment

/* Block
   comment */

/// Doc comment (for documentation generation)
```

---

## Syntax

### Functions (FROZEN)

```solo
fn function_name(param1: Type1, param2: Type2) -> ReturnType {
    // body
}
```

**Examples:**
```solo
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn greet(name: String) {
    println("Hello, {}", name);
}

fn factorial(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * factorial(n - 1) }
}
```

### Let Bindings (FROZEN)

```solo
let x = 42;           // immutable
let mut y = 0;        // mutable
let z: i64 = 100;     // explicit type
```

### Control Flow (FROZEN)

```solo
// If-else
if condition {
    // ...
} else if other {
    // ...
} else {
    // ...
}

// While loop
while condition {
    // ...
}

// Return
return value;
```

### Structs (EXPLORATORY)

```solo
struct Point {
    x: f64,
    y: f64,
}

struct BeliefState {
    value: f64,
    confidence: f64,
}
```

### Enums (EXPLORATORY)

```solo
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

### Pattern Matching (EXPLORATORY)

```solo
match value {
    Some(x) => process(x),
    None => default(),
}
```

### Arena Blocks (EXPLORATORY)

```solo
arena {
    let data = Vec::with_capacity(1000);
    for i in 0..1000 {
        data.push(compute(i));
    }
    process(data);
    // All allocations freed here
}
```

---

## Type System

### Primitive Types (FROZEN)

| Type | Size | Description |
|------|------|-------------|
| `i8`, `i16`, `i32`, `i64` | 1-8 bytes | Signed integers |
| `u8`, `u16`, `u32`, `u64` | 1-8 bytes | Unsigned integers |
| `f32`, `f64` | 4-8 bytes | Floating point |
| `bool` | 1 byte | Boolean |
| `char` | 4 bytes | Unicode scalar |

### Compound Types (EXPLORATORY)

```solo
// Tuple
let pair: (i32, String) = (42, "hello");

// Array (fixed size)
let arr: [i32; 5] = [1, 2, 3, 4, 5];

// Slice (borrowed view)
let slice: &[i32] = &arr[1..3];

// Vec (dynamic array)
let vec: Vec<i32> = Vec::new();
```

### Affine Types (EXPLORATORY)

Values can be used **at most once**:

```solo
fn consume(data: Buffer) {
    // data is consumed here
}

let buf = Buffer::new();
consume(buf);
// buf is no longer valid here - compile error if used
```

### Borrowing (EXPLORATORY)

```solo
fn read_only(data: &Buffer) {
    // Can read, cannot modify
}

fn modify(data: &mut Buffer) {
    // Can read and modify
}

let mut buf = Buffer::new();
read_only(&buf);      // Immutable borrow
modify(&mut buf);     // Mutable borrow
```

---

## Memory Model

### Ownership Rules (EXPLORATORY)

1. Each value has exactly one owner
2. When owner goes out of scope, value is dropped
3. Values can be moved (ownership transfer) or borrowed (temporary access)

### Arena Allocation (EXPLORATORY)

```solo
arena 'a {
    // All allocations use arena 'a
    let x = allocate::<i32>(42);
    let y = allocate::<String>("hello");

    // No individual deallocation needed
} // All memory freed here
```

**Benefits:**
- No garbage collection pauses
- Predictable memory usage
- Cache-friendly allocation patterns

---

## Epistemic Extension

Solo inherits epistemic types from Me dialect:

### Belief Type (EXPLORATORY)

```solo
struct Belief<T> {
    value: T,
    confidence: f64,
}

belief claim: Belief<bool> where confidence(0.85);
```

### Distribution Assignment (EXPLORATORY)

```solo
claim ~ Bernoulli(0.7);
measurement ~ Normal(20.0, 2.5);
```

### Confidence Check (EXPLORATORY)

```solo
if confidence(claim) >= 0.9 {
    publish(claim);
}
```

---

## Implementation Status

### Completed (40%)

- [x] **Lexer** - Full tokenization with all frozen features
- [x] **Token types** - Keywords, operators, literals, comments
- [x] **Error handling** - Line/column tracking for diagnostics
- [x] **Embedded tests** - 6 test suites in lexer.rs

### In Progress

- [ ] **Parser** - Recursive descent parser (started)
- [ ] **AST** - Abstract syntax tree definitions
- [ ] **Type checker** - Basic type inference

### Planned

- [ ] **Borrow checker** - Affine type verification
- [ ] **IR generation** - QBE intermediate representation
- [ ] **Code generation** - Native binary output
- [ ] **Optimizer** - Basic optimizations

### Compiler Architecture

```
Source Code (.solo)
       ↓
    Lexer (✅ Complete)
       ↓
    Tokens
       ↓
    Parser (🚧 In Progress)
       ↓
    AST
       ↓
    Type Checker
       ↓
    Typed AST
       ↓
    Borrow Checker
       ↓
    QBE IR
       ↓
    Native Binary
```

---

## Examples

### Example 1: Hello World

```solo
// hello_world.solo
fn main() {
    println("Hello, Solo!");
}
```

### Example 2: Affine Types

```solo
// Buffer that can only be used once
struct Buffer {
    data: Vec<u8>,
}

fn process(buf: Buffer) -> Vec<u8> {
    // buf is consumed here
    transform(buf.data)
}

fn main() {
    let buffer = Buffer::new(1024);
    let result = process(buffer);
    // buffer is no longer valid
    // let error = buffer.data;  // COMPILE ERROR
}
```

### Example 3: Epistemic Extension

```solo
// belief_example.solo
fn verify_claim(sources: Vec<Source>) -> Belief<bool> {
    belief result: Belief<bool> where confidence(0.0);

    for source in sources {
        let evidence = source.query();
        result = fuse(result, evidence, rule=Dempster);
    }

    result
}

fn main() {
    let sources = vec![
        Source::new("Reuters", credibility=0.95),
        Source::new("AP", credibility=0.90),
    ];

    let claim = verify_claim(sources);

    if confidence(claim) >= 0.85 {
        println("Verified with confidence: {}", confidence(claim));
    }
}
```

### Example 4: Arena Allocation

```solo
fn process_large_dataset(path: &str) -> Stats {
    arena {
        // All allocations happen in this arena
        let data = read_file(path);
        let parsed = parse_csv(data);
        let filtered = parsed.filter(|row| row.valid);
        let stats = compute_stats(filtered);

        // Only stats escapes the arena (via return)
        stats
    } // All intermediate allocations freed here
}
```

---

## Comparison to Rust

| Feature | Solo | Rust |
|---------|------|------|
| Ownership | ✅ Affine types | ✅ Affine types |
| Borrowing | ✅ & and &mut | ✅ & and &mut |
| Lifetimes | ✅ Explicit | ✅ Explicit |
| GC | ❌ None | ❌ None |
| Unsafe | ❌ Forbidden | ⚠️ Allowed |
| Arenas | ✅ First-class | ⚠️ Via crates |
| Epistemic Types | ✅ Built-in | ❌ None |
| Target | QBE → Native | LLVM → Native |

---

## Changelog

### v0.1.0-alpha (2025-11-22)

- Initial specification
- Frozen: keywords, operators, primitive types, basic syntax
- Exploratory: affine types, arenas, structs, enums, generics
- Lexer complete with 6 test suites

---

**Previous Dialect:** [Me](me.md) - Epistemic types and belief states
**Next Dialect:** [Duet](duet.md) - Human-AI co-programming with verification
