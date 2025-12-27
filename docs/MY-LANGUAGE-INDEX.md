# My Language: Complete Index

**Version:** 0.1.0-alpha
**Last Updated:** 2025-11-22
**Purpose:** Master reference for all four dialects (Me, Solo, Duet, Ensemble)

---

## Quick Navigation

| Dialect | Status | Purpose | Frozen Features | Exploratory |
|---------|--------|---------|-----------------|-------------|
| **Me** | ✅ Complete | Epistemic types, belief states | 8 features | 7 features |
| **Solo** | 🚧 40% | Systems programming, memory safety | 8 features | 11 features |
| **Duet** | 📋 Spec | Human-AI co-programming, verification | 5 features | 8 features |
| **Ensemble** | 📋 Spec | Multi-agent orchestration, belief fusion | 5 features | 8 features |

### Specification Links

| Dialect | Spec | Examples |
|---------|------|----------|
| **Me** | [me.md](dialects/me.md) | [examples/me/](../examples/me/) |
| **Solo** | [solo.md](dialects/solo.md) | [examples/solo/](../examples/solo/) |
| **Duet** | [duet.md](dialects/duet.md) | [examples/duet/](../examples/duet/) |
| **Ensemble** | [ensemble.md](dialects/ensemble.md) | [examples/ensemble/](../examples/ensemble/) |

---

## Overview

**My Language** is a family of four dialects with **graduated trust semantics**, designed for:

- **Epistemic reasoning** - Formal uncertainty quantification
- **Political autonomy** - No vendor lock-in, offline-first
- **Neurosymbolic AI** - Hybrid symbolic-neural systems
- **Journalism technology** - Fact-checking, source credibility, belief fusion

### Design Principles

1. **Gradual Typing** - Python → TypeScript → Rust/Ada progression
2. **Offline-First** - All dialects work air-gapped (no cloud dependencies)
3. **Type Safety** - Prevent entire classes of bugs at compile-time
4. **Memory Safety** - Zero `unsafe` in production code (Rust/Ada)
5. **Explainability** - All AI decisions are traceable and auditable

---

## Dialect Pipeline

The four dialects form an **explicit compilation and integration pipeline**:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                        MY LANGUAGE DIALECT PIPELINE                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌──────────┐           ║
║   │   Me    │────▶│  Solo   │────▶│  Duet   │────▶│ Ensemble │           ║
║   │ v0.1.0  │     │ v0.1.0α │     │  spec   │     │   spec   │           ║
║   └────┬────┘     └────┬────┘     └────┬────┘     └────┬─────┘           ║
║        │               │               │               │                 ║
║   ┌────▼────┐     ┌────▼────┐     ┌────▼────┐     ┌────▼─────┐           ║
║   │Epistemic│     │ Memory  │     │  Formal │     │  Multi-  │           ║
║   │  Types  │     │  Safe   │     │ Verified│     │  Agent   │           ║
║   │ Beliefs │     │ Affine  │     │AI Synth │     │ Fusion   │           ║
║   └─────────┘     └─────────┘     └─────────┘     └──────────┘           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Pipeline Stages

| Stage | Input | Output | Key Transformation |
|-------|-------|--------|-------------------|
| **Me → Solo** | Belief prototypes | Performance code | Add memory safety, remove GC |
| **Solo → Duet** | Memory-safe code | Verified code | Add formal proofs, AI synthesis |
| **Duet → Ensemble** | Verified agents | Distributed system | Add multi-agent coordination |

### Data Flow

```
Me Types          Solo Implementation       Duet Verification      Ensemble Orchestration
─────────         ──────────────────        ─────────────────      ──────────────────────
belief x: Float   struct Belief<T> {        fn fuse(...) where     agent FactChecker {
  confidence(0.8)   value: T,                 @verify: "valid"       beliefs: BeliefState
                    confidence: f64           @synth { ... }         fn verify(&self) {
x ~ Uniform(0,1)  }                         }                          duet::fuse(...)
                                                                    }
```

### Interoperability Protocol

1. **Types flow forward**: Me defines epistemic types, Solo implements them, Duet verifies them, Ensemble distributes them
2. **Proofs flow backward**: Ensemble agents call Duet-verified functions, which compile to Solo
3. **Beliefs propagate**: All dialects share the `Belief<T>` type with confidence semantics

---

## Dialect Comparison

### High-Level Overview

```
┌─────────┬─────────┬─────────┬──────────┐
│   Me    │  Solo   │  Duet   │ Ensemble │
├─────────┼─────────┼─────────┼──────────┤
│ Belief  │ Systems │ Verify  │  Agents  │
│ States  │  Prog   │   +AI   │ + Fusion │
└─────────┴─────────┴─────────┴──────────┘
     ↓         ↓         ↓         ↓
  Epistemic  Memory  Formal    Multi-
   Types     Safe    Proofs    Agent
```

### Feature Matrix

| Feature | Me | Solo | Duet | Ensemble |
|---------|----|----|------|----------|
| **Epistemic Types** | ✅ | ✅ | ✅ | ✅ |
| **Belief States** | ✅ | ✅ | ✅ | ✅ |
| **Probabilistic Reasoning** | ✅ | ⚠️ | ✅ | ✅ |
| **Affine Types** | ❌ | ✅ | ✅ | ✅ |
| **Arena Allocation** | ❌ | ✅ | ✅ | ✅ |
| **Garbage Collection** | ✅ | ❌ | ❌ | ⚠️ |
| **Formal Verification** | ❌ | ⚠️ | ✅ | ✅ |
| **AI Synthesis** | ❌ | ❌ | ✅ | ⚠️ |
| **Multi-Agent** | ❌ | ❌ | ❌ | ✅ |
| **Dempster-Shafer Fusion** | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **Epistemic Ledger** | ❌ | ❌ | ❌ | ✅ |

Legend: ✅ Full support | ⚠️ Partial/planned | ❌ Not supported

### Complexity Spectrum

```
Simplicity ←─────────────────────────────→ Power

Me           Solo          Duet         Ensemble
│            │             │            │
Easy to      Performance   Correctness  Distributed
learn        critical      critical     systems
│            │             │            │
Prototype    Production    Safety-      Multi-agent
             systems       critical     coordination
```

---

## Dialect Details

### Me Dialect (Epistemic Foundation)

**Status:** ✅ Complete (HTML playground available)

**Key Features:**
- Epistemic types: `belief x: Float where confidence(0.75)`
- Probabilistic reasoning: `x ~ Uniform(0, 1)`
- Trust semantics: `trust(source, level=High)`

**Use Cases:**
- Modeling uncertainty in data
- Prototyping belief fusion algorithms
- Teaching epistemic reasoning concepts

**Example:**
```my
belief claim_is_true: Bool where confidence(0.85);
claim_is_true ~ Bernoulli(0.7);  # Prior belief: 70% likely true

observe(evidence="Reuters confirms", credibility=0.9);
# Posterior belief updated via Bayesian inference
```

**Learn More:**
- [Me Dialect Specification](dialects/me.md)
- [Me Playground](../examples/me/playground.html)
- [Me Tutorial](dialects/me.md#tutorial)

---

### Solo Dialect (Systems Programming)

**Status:** 🚧 40% Complete (parser + QBE backend in progress)

**Key Features:**
- Affine types (linear ownership, no aliasing)
- Arena allocation (no garbage collection)
- Compile-time memory safety
- Rust-like performance, Ada-like safety

**Use Cases:**
- Performance-critical systems
- Embedded systems (no GC overhead)
- Compilers and runtimes
- Low-level infrastructure

**Example:**
```solo
// Affine types: can't use-after-move
fn process(data: Buffer) -> Result<Vec<u8>, Error> {
    let processed = transform(data);
    // data is now moved, can't use here
    Ok(processed)
}

// Arena allocation: deterministic cleanup
arena {
    let temp = allocate_large_buffer();
    compute(temp);
    // temp automatically freed at arena exit
}
```

**Learn More:**
- [Solo Dialect Specification](dialects/solo.md)
- [Solo Compiler Status](dialects/solo.md#implementation-status)
- [Solo vs. Rust Comparison](dialects/solo.md#comparison-to-rust)

---

### Duet Dialect (Human-AI Co-Programming)

**Status:** 📋 Specification Complete (implementation planned Q2-Q4 2025)

**Key Features:**
- Intent declarations: `intent("sort array in O(n log n)")`
- Verification contracts: `@verify: "sorted(result)"`
- AI synthesis holes: `@synth { /* AI fills in */ }`
- SPARK formal verification integration

**Use Cases:**
- Safety-critical systems (aviation, medical)
- Correctness-critical algorithms (cryptography)
- Educational tools (learn formal methods)
- Accelerating development with AI assistance

**Example:**
```duet
intent("Implement Dempster-Shafer belief fusion")
fn fuse_beliefs(m1: BeliefMass, m2: BeliefMass) -> BeliefMass where
    @verify: "commutativity: fuse(m1, m2) == fuse(m2, m1)",
    @verify: "valid_belief_mass(result)" {

    @synth { /* AI generates provably correct implementation */ }
}
```

**Learn More:**
- [Duet Dialect Specification](dialects/duet.md)
- [Duet Verification Guide](dialects/duet.md#verification-system)
- [Duet AI Integration](dialects/duet.md#ai-integration)

---

### Ensemble Dialect (Multi-Agent Orchestration)

**Status:** 📋 Specification Complete (implementation planned Q3 2025 - Q4 2026)

**Key Features:**
- Agent abstraction: `agent ReporterAgent { ... }`
- Dempster-Shafer belief fusion
- Byzantine fault tolerance (33% malicious agents)
- Epistemic ledger (immutable audit trail)
- Comptime orchestration: `comptime orchestrate { ... }`

**Use Cases:**
- Distributed newsrooms (Newroom project)
- Multi-agent simulations
- Decentralized fact-checking
- Collaborative decision-making systems

**Example:**
```ensemble
comptime orchestrate NewsVerificationRing {
    agents: [
        ReporterAgent(domain="politics"),
        ReporterAgent(domain="science"),
        FactCheckerAgent(sources=[Snopes, FactCheck]),
        EditorAgent(threshold=0.85),
    ],
    topology: Ring,
    fusion: Dempster,
    consensus: Threshold(0.85),
}
```

**Learn More:**
- [Ensemble Dialect Specification](dialects/ensemble.md)
- [Ensemble Agent Model](dialects/ensemble.md#agent-model)
- [Ensemble Newroom Example](dialects/ensemble.md#example-1-simple-newsroom-5-agents)

---

## When to Use Which Dialect

### Decision Tree

```
Start here:
    │
    ├─ Prototyping / Learning?
    │   └─→ Use Me (easiest, playground available)
    │
    ├─ Performance-critical single process?
    │   └─→ Use Solo (no GC, memory-safe)
    │
    ├─ Need formal correctness proofs?
    │   └─→ Use Duet (SPARK verification)
    │
    └─ Multi-agent distributed system?
        └─→ Use Ensemble (belief fusion, BFT)
```

### Use Case → Dialect Mapping

| Use Case | Recommended Dialect | Why |
|----------|-------------------|-----|
| **Teaching epistemic types** | Me | Interactive playground, simple syntax |
| **Belief fusion prototype** | Me | Quick iteration, Bayesian inference |
| **Compiler / Runtime** | Solo | Performance, manual memory management |
| **Embedded systems** | Solo | No GC, predictable timing |
| **Safety-critical code** | Duet | Formal verification, provable correctness |
| **AI-assisted development** | Duet | Synthesis holes, automated testing |
| **Fact-checking system** | Ensemble | Multi-agent, Dempster-Shafer fusion |
| **Distributed newsroom** | Ensemble | BFT, epistemic ledger, scalability |

---

## Graduation Path

### Learning Progression

```
1. Start with Me
   ├─ Learn epistemic types
   ├─ Experiment in playground
   └─ Build simple belief models
      │
      ↓
2. Move to Solo
   ├─ Add performance concerns
   ├─ Learn affine types
   └─ Implement efficient algorithms
      │
      ↓
3. Adopt Duet
   ├─ Add verification needs
   ├─ Use AI synthesis
   └─ Prove correctness formally
      │
      ↓
4. Scale with Ensemble
   ├─ Add multi-agent coordination
   ├─ Implement belief fusion
   └─ Build distributed systems
```

### Migration Example

**Me (Prototype):**
```my
belief claim_true: Float where confidence(0.8);
```

**Solo (Performance):**
```solo
struct Belief {
    value: f64,
    confidence: f64,
}
```

**Duet (Verified):**
```duet
type Belief = (Float, Float) where
    @verify: "0.0 <= confidence && confidence <= 1.0";
```

**Ensemble (Distributed):**
```ensemble
agent ReporterAgent {
    beliefs: HashMap<Claim, Belief>,

    fn update_belief(&mut self, claim: Claim, evidence: Evidence) {
        // Distributed belief update with ledger
    }
}
```

---

## Cross-Cutting Concerns

### Type System Evolution

| Concept | Me | Solo | Duet | Ensemble |
|---------|----|----|------|----------|
| **Primitives** | Int, Float, Bool, String | ✓ + sized | ✓ + refined | ✓ + agent types |
| **Structs** | Named fields | ✓ + affine | ✓ + contracts | ✓ + agent state |
| **Enums** | Tagged unions | ✓ + exhaustiveness | ✓ + proofs | ✓ + messages |
| **Generics** | Type parameters | ✓ + lifetimes | ✓ + dependent | ✓ + session types |
| **Effects** | None | ⚠️ Partial | ✓ Pure/IO/Mut | ✓ Agent effects |

### Compilation Targets

| Dialect | Stage 1 | Stage 2 | Final Output |
|---------|---------|---------|--------------|
| **Me** | TypeScript | HTML/JS | Browser app |
| **Solo** | Rust | QBE IR | Native binary |
| **Duet** | Solo + Ada | SPARK verification | Verified binary |
| **Ensemble** | Duet | Elixir actors | BEAM bytecode |

### Interoperability

```
┌──────────┐
│    Me    │  ← Prototype ideas
└────┬─────┘
     │ export types
     ↓
┌──────────┐
│   Solo   │  ← Implement performance-critical parts
└────┬─────┘
     │ call via FFI
     ↓
┌──────────┐
│   Duet   │  ← Verify correctness formally
└────┬─────┘
     │ deploy as agent
     ↓
┌──────────┐
│ Ensemble │  ← Orchestrate multi-agent system
└──────────┘
```

**Example:**
```ensemble
// Ensemble agent calls Duet-verified function
agent FactCheckerAgent {
    fn verify_claim(&self, claim: &Claim) -> Belief {
        // Calls Duet-verified Dempster-Shafer fusion
        let belief_a = self.source_a.query(claim);
        let belief_b = self.source_b.query(claim);

        duet::fuse_beliefs(belief_a, belief_b)  // Provably correct!
    }
}
```

---

## Common Patterns

### Pattern 1: Epistemic State Machine

**Me (Specification):**
```my
belief state: Enum["initial", "gathering", "verified", "published"];
transition(state, "gathering" → "verified") where confidence(evidence) >= 0.8;
```

**Ensemble (Implementation):**
```ensemble
agent NewsArticleAgent {
    state: ArticleState,

    fn transition(&mut self, event: Event) {
        match (self.state, event) {
            (Gathering, EvidenceGathered(e)) if e.confidence >= 0.8 => {
                self.state = Verified;
                self.emit(StateTransition { old: Gathering, new: Verified });
            }
            // ...
        }
    }
}
```

### Pattern 2: Verified Algorithm

**Solo (Implementation):**
```solo
fn binary_search<T: Ord>(arr: &[T], target: &T) -> Option<usize> {
    // Fast, memory-safe implementation
}
```

**Duet (Verification):**
```duet
fn binary_search<T: Ord>(arr: &[T], target: &T) -> Option<usize> where
    @verify: "precondition: sorted(arr)",
    @verify: "postcondition: result.is_some() => arr[result.unwrap()] == *target" {
    // Solo implementation + SPARK proofs
}
```

### Pattern 3: Multi-Agent Consensus

**Ensemble:**
```ensemble
comptime orchestrate ConsensusRing {
    agents: [Agent; N],
    topology: Ring,
    fusion: Dempster,
    consensus: Threshold(0.85),
}

fn reach_consensus(claim: Claim) -> Option<Belief> {
    let all_beliefs = agents.iter().map(|a| a.belief(&claim)).collect();
    let fused = fuse_all(all_beliefs);

    if fused.confidence >= 0.85 {
        Some(fused)
    } else {
        None  // Insufficient agreement
    }
}
```

---

## Resources

### Documentation

- **Specifications:**
  - [Me Dialect](dialects/me.md)
  - [Solo Dialect](dialects/solo.md)
  - [Duet Dialect](dialects/duet.md)
  - [Ensemble Dialect](dialects/ensemble.md)

- **Guides:**
  - [Getting Started](../README.md#quick-start)
  - [Contribution Guide](../CONTRIBUTING.md)
  - [Migration Guide](guides/migration-guide.md)
  - [Verification Guide](guides/verification-guide.md)

- **Research:**
  - [Academic Papers](research/academic-papers.md)
  - [Conference Materials](research/conference-materials.md)
  - [Newroom Roadmap](NEWROOM-ROADMAP.md)

### Examples

```
examples/
├── me/
│   ├── playground.html          # Interactive Me playground
│   ├── belief_inference.my      # Bayesian belief updating
│   └── trust_propagation.my     # Trust graph traversal
├── solo/
│   ├── hello_world.solo         # Basic syntax demo
│   ├── arena_allocation.solo    # Manual memory management
│   └── parser.solo              # Recursive descent parser
├── duet/
│   ├── dempster_shafer.duet     # Verified belief fusion
│   ├── quicksort.duet           # Verified sorting algorithm
│   └── parser_synth.duet        # AI-synthesized parser
└── ensemble/
    ├── simple_newsroom.ens      # 5-agent example
    ├── reuters_scale.ens        # 100-agent simulation
    └── bft_consensus.ens        # Byzantine fault tolerance
```

### External References

- **Theoretical Foundations:**
  - Dempster-Shafer Theory (Shafer 1976)
  - Type Systems (Pierce 2002)
  - Multi-Agent Systems (Wooldridge 2009)
  - Epistemic Logic (Fagin et al. 1995)

- **Implementation Inspiration:**
  - Rust (affine types, ownership)
  - Ada/SPARK (formal verification)
  - Elixir (actor model, fault tolerance)
  - Haskell (purity, type classes)

---

## FAQ

### Q: Which dialect should I start with?

**A:** Start with **Me** if you're new to epistemic programming. It has an interactive playground and gentlest learning curve.

### Q: Can I mix dialects in one project?

**A:** Yes! Dialects are designed to interoperate:
- Prototype in **Me**
- Optimize bottlenecks in **Solo**
- Verify critical parts with **Duet**
- Orchestrate as agents in **Ensemble**

### Q: Do I need to learn all four dialects?

**A:** No. Use what you need:
- **Me only:** Modeling and prototyping
- **Me + Solo:** Production systems
- **Me + Solo + Duet:** Safety-critical systems
- **All four:** Multi-agent distributed systems (Newroom project)

### Q: What's the learning curve?

**Estimated time to proficiency:**
- **Me:** 1-2 weeks (if familiar with Python/TypeScript)
- **Solo:** 1-2 months (if familiar with Rust)
- **Duet:** 2-3 months (requires formal methods background)
- **Ensemble:** 3-6 months (requires distributed systems experience)

### Q: Is this production-ready?

**Current status (2025-11-22):**
- **Me:** ✅ Yes (use for prototyping)
- **Solo:** ⚠️ Not yet (40% complete, MVP in Q1 2025)
- **Duet:** ❌ No (spec only, implementation Q2-Q4 2025)
- **Ensemble:** ❌ No (spec only, implementation 2025-2026)

---

## Changelog

### 2025-11-22 - Initial Version

- Created master index for all 4 dialects
- Added feature comparison matrix
- Documented graduation path and interoperability
- Included decision tree for dialect selection
- Added 3 common patterns with examples

---

**Questions?** Open an issue on [GitLab](https://gitlab.com/Hyperpolymath/My-newsroom/-/issues) or consult [claude.md](../claude.md) for AI assistant guidelines.

**Ready to dive in?** Try the [Me Playground](../examples/me/playground.html) or read the [Quick Start Guide](../README.md#quick-start)!
