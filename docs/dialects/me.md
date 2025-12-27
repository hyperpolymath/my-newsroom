# Me Dialect Specification

**Version:** 0.1.0
**Status:** Complete (HTML Playground Available)
**Parent Language:** My Language Family
**Paradigm:** Epistemic Programming with Belief States

---

## Specification Status

### FROZEN (Stable API - Breaking Changes Require RFC)

| Feature | Status | Since | Description |
|---------|--------|-------|-------------|
| **Belief Declarations** | Frozen | v0.1.0 | `belief x: Type where confidence(n)` |
| **Distribution Syntax** | Frozen | v0.1.0 | `x ~ Distribution(params)` |
| **Confidence Accessor** | Frozen | v0.1.0 | `confidence(belief_var)` |
| **Trust Declarations** | Frozen | v0.1.0 | `trust(source, level=High\|Medium\|Low)` |
| **Observe Statement** | Frozen | v0.1.0 | `observe(evidence="...", credibility=n)` |
| **Print Statement** | Frozen | v0.1.0 | `print(expr)` |
| **Basic Types** | Frozen | v0.1.0 | `Bool`, `Float`, `Int`, `String` |
| **Distributions** | Frozen | v0.1.0 | `Uniform`, `Bernoulli`, `Normal` |

### EXPLORATORY (Subject to Change)

| Feature | Status | Target | Description |
|---------|--------|--------|-------------|
| **Fuse Expression** | Exploratory | v0.2.0 | `fuse(a, b, rule=Dempster)` syntax |
| **Weighted Fusion** | Exploratory | v0.2.0 | `weighted_fuse(beliefs)` |
| **Conditional Beliefs** | Exploratory | v0.3.0 | `belief x: T if condition` |
| **Belief Arrays** | Exploratory | v0.3.0 | `belief[] claims: Float` |
| **Source Functions** | Exploratory | v0.2.0 | `source(name, credibility, says)` |
| **Threshold Checks** | Exploratory | v0.2.0 | `if confidence(x) >= threshold` |
| **Fuse All** | Exploratory | v0.2.0 | `fuse_all([evidence1, evidence2, ...])` |

---

## Table of Contents

1. [Overview](#overview)
2. [Design Philosophy](#design-philosophy)
3. [Syntax](#syntax)
4. [Type System](#type-system)
5. [Semantics](#semantics)
6. [Examples](#examples)
7. [Playground](#playground)

---

## Overview

**Me** is the foundational dialect in the My Language family, designed for **epistemic programming** - reasoning formally about beliefs, uncertainty, and evidence. It provides:

- **Epistemic types** - Variables that carry confidence levels
- **Probabilistic reasoning** - Distributions and Bayesian updates
- **Trust semantics** - Source credibility modeling
- **Belief fusion** - Combining evidence from multiple sources

### Pipeline Position

```
┌─────────────────────────────────────────────────────────────────┐
│                    MY LANGUAGE PIPELINE                         │
├─────────┬─────────┬─────────┬──────────┬───────────────────────┤
│   Me    │    →    │  Solo   │    →     │  Duet  →  Ensemble    │
│ (here)  │ exports │         │ verifies │                       │
├─────────┼─────────┼─────────┼──────────┼───────────────────────┤
│Epistemic│  types  │ Systems │  proofs  │ Multi-Agent           │
│ Types   │    +    │   +     │    +     │ Orchestration         │
│         │ beliefs │ Memory  │    AI    │                       │
└─────────┴─────────┴─────────┴──────────┴───────────────────────┘
```

**Me's Role:**
- **Entry point** for learning epistemic programming
- **Prototype environment** for belief modeling
- **Type definitions** that propagate to Solo, Duet, Ensemble

---

## Design Philosophy

### 1. Simplicity First

Me prioritizes **ease of learning** over performance:

```me
# Simple belief declaration
belief claim_is_true: Float where confidence(0.75);
```

### 2. Explicit Uncertainty

All beliefs carry **explicit confidence levels** - no hidden certainty:

```me
# Bad: Implicit certainty
let x = true;  # ERROR: Use belief for epistemic values

# Good: Explicit uncertainty
belief x: Bool where confidence(0.95);
```

### 3. Traceable Updates

Every belief update is **traceable**:

```me
observe(evidence="Reuters confirms", credibility=0.9);
# Runtime: Belief updated from 0.75 → 0.88 via Bayesian inference
```

---

## Syntax

### Belief Declarations (FROZEN)

```me
belief <name>: <Type> where confidence(<value>);
```

**Examples:**
```me
belief claim_true: Bool where confidence(0.85);
belief temperature: Float where confidence(0.70);
belief category: String where confidence(0.60);
```

### Distribution Assignment (FROZEN)

```me
<belief_var> ~ <Distribution>(<params>);
```

**Supported Distributions:**
- `Uniform(low, high)` - Uniform distribution
- `Bernoulli(p)` - Binary outcome with probability p
- `Normal(mean, std)` - Gaussian distribution

**Examples:**
```me
claim_true ~ Bernoulli(0.7);      # 70% prior probability
measurement ~ Normal(20.0, 2.5);  # Mean 20, std dev 2.5
score ~ Uniform(0, 100);          # Uniform over [0, 100]
```

### Trust Declarations (FROZEN)

```me
trust(<source>, level=<High|Medium|Low>);
```

**Examples:**
```me
trust(Reuters, level=High);
trust(Twitter, level=Medium);
trust(RandomBlog, level=Low);
```

### Observe Statement (FROZEN)

```me
observe(evidence="<description>", credibility=<0.0-1.0>);
```

**Examples:**
```me
observe(evidence="Peer-reviewed study confirms", credibility=0.95);
observe(evidence="Anonymous tip", credibility=0.30);
```

### Print Statement (FROZEN)

```me
print(<expression>);
print("<string>", <expression>);
```

**Examples:**
```me
print(claim_true);
print("Current belief:", claim_true);
print("Confidence:", confidence(claim_true));
```

### Fusion (EXPLORATORY)

```me
# Basic fusion
result := fuse(source_a, source_b, rule=Dempster);

# Multi-source fusion
combined := fuse_all([evidence1, evidence2, evidence3]);

# Source declaration
evidence1 := source(IPCC, credibility=0.95, says=true);
```

---

## Type System

### Primitive Types (FROZEN)

| Type | Description | Example |
|------|-------------|---------|
| `Bool` | Boolean value | `true`, `false` |
| `Float` | 64-bit floating point | `0.85`, `3.14159` |
| `Int` | 64-bit integer | `42`, `-17` |
| `String` | UTF-8 string | `"hello"` |

### Epistemic Types (FROZEN)

```me
# Belief type: value + confidence
belief x: Float where confidence(0.8);

# Equivalent to:
# { value: Float, confidence: Float }
```

### Trust Levels (FROZEN)

```me
enum TrustLevel {
    High,    # 0.9+ credibility weight
    Medium,  # 0.5-0.9 credibility weight
    Low,     # <0.5 credibility weight
}
```

---

## Semantics

### Confidence Propagation

When beliefs are combined, confidence propagates according to **Bayesian rules**:

```me
belief a: Float where confidence(0.8);
belief b: Float where confidence(0.7);

# Combined confidence = f(0.8, 0.7) based on fusion rule
result := fuse(a, b, rule=Dempster);
```

### Observation Updates

`observe()` triggers **Bayesian posterior update**:

```
P(H|E) = P(E|H) * P(H) / P(E)

Where:
- P(H) = prior belief (current confidence)
- P(E|H) = likelihood (evidence credibility)
- P(H|E) = posterior belief (updated confidence)
```

---

## Examples

### Example 1: Basic Belief

```me
# Basic Belief State
belief claim_true: Float where confidence(0.75);
claim_true ~ Uniform(0, 1);

print("Initial belief:", claim_true);
print("Confidence level:", confidence(claim_true));
```

### Example 2: Belief Fusion

```me
# Combining evidence from multiple sources
belief source_a: Float where confidence(0.85);
belief source_b: Float where confidence(0.70);

source_a ~ Bernoulli(0.8);
source_b ~ Bernoulli(0.7);

# Fuse beliefs using Dempster-Shafer
result := fuse(source_a, source_b, rule=Dempster);

print("Source A:", source_a, "confidence:", confidence(source_a));
print("Source B:", source_b, "confidence:", confidence(source_b));
print("Fused:", result, "confidence:", confidence(result));
```

### Example 3: Newsroom Scenario

```me
# Multi-source verification with decision threshold
belief climate_claim: Bool where confidence(0.0);

# Gather evidence from multiple sources
evidence1 := source(IPCC, credibility=0.95, says=true);
evidence2 := source(NASA, credibility=0.90, says=true);
evidence3 := source(University, credibility=0.85, says=true);

# Progressively fuse evidence
climate_claim = fuse_all([evidence1, evidence2, evidence3]);

# Editorial decision
threshold := 0.85;
if confidence(climate_claim) >= threshold {
    print("PUBLISH - Confidence:", confidence(climate_claim));
} else {
    print("HOLD - Need more evidence");
}
```

---

## Playground

An interactive HTML playground is available at:

```
examples/me/playground.html
```

### Features

- **Code Editor** - Write Me dialect code
- **Output Panel** - See execution results
- **Example Programs** - 5 pre-built demos
- **URL Sharing** - Share code via encoded URLs

### Running Locally

```bash
# Open in browser
open examples/me/playground.html

# Or serve via HTTP
python -m http.server 8000
# Then visit http://localhost:8000/examples/me/playground.html
```

---

## Changelog

### v0.1.0 (2025-11-22)

- Initial specification
- Frozen: belief declarations, distributions, trust, observe, print
- Exploratory: fusion syntax, conditional beliefs
- HTML playground complete

---

**Next Dialect:** [Solo](solo.md) - Systems programming with affine types
