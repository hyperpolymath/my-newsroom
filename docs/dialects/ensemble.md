# Ensemble Dialect Specification

**Version:** 0.1.0-draft
**Status:** Specification Phase (No Implementation Yet)
**Parent Language:** My Language Family
**Paradigm:** Multi-Agent Orchestration with Epistemic Reasoning

---

## Table of Contents

1. [Overview](#overview)
2. [Design Philosophy](#design-philosophy)
3. [Agent Model](#agent-model)
4. [Belief Fusion](#belief-fusion)
5. [Communication](#communication)
6. [Orchestration](#orchestration)
7. [Epistemic Ledger](#epistemic-ledger)
8. [Examples](#examples)
9. [Runtime Architecture](#runtime-architecture)
10. [Implementation Plan](#implementation-plan)

---

## Overview

**Ensemble** is the fourth and most advanced dialect in the My Language family, designed for **multi-agent systems** with **formal uncertainty quantification**. It combines:

- **Agent abstraction** - First-class agents with beliefs, goals, and behaviors
- **Dempster-Shafer fusion** - Mathematical evidence combination
- **Epistemic ledger** - Immutable audit trail of belief updates
- **Distributed consensus** - Byzantine fault-tolerant coordination
- **Comptime orchestration** - Static agent topology configuration

### Key Features

| Feature | Description | Example |
|---------|-------------|---------|
| **Agent Types** | Specialized roles | `ReporterAgent`, `FactCheckerAgent` |
| **Belief States** | Epistemic types from Me | `belief x: Float where confidence(0.8)` |
| **Fusion Rules** | Evidence combination | `Dempster`, `Yager`, `DuboisPrade` |
| **Topologies** | Agent communication patterns | `Ring`, `Star`, `FullyConnected` |
| **Consensus** | Distributed agreement | `Threshold(0.85)`, `Unanimous` |
| **Ledger** | Audit trail | `EpistemicLedger` with crypto signatures |

### Relationship to Other Dialects

```
Me      →  Solo     →  Duet         →  Ensemble
(belief)  (systems)   (verification)   (orchestration)

Single    Single      Single + AI      Multiple Agents
Agent     Process     Assistance       + Coordination
```

**Ensemble's Role:**
- **Extends Duet** with multi-agent communication and belief fusion
- **Integrates Me** epistemic types into distributed systems
- **Enables Newroom** demonstration project (50-100 journalist agents)

---

## Design Philosophy

### 1. Epistemic Transparency

Every belief update is **traceable and explainable**:

```ensemble
// Agent A receives evidence
agent_a.update_belief("claim_123", evidence, confidence=0.75);

// Ledger records:
// [2025-11-22 10:30:15] AgentA (ID: 0x4f2a...)
//   Updated belief in claim_123: 0.5 → 0.75 (Δ +0.25)
//   Evidence: source="Reuters", verified_by=AgentB
//   Signature: ed25519:0x9a3c...
```

### 2. Byzantine Fault Tolerance

System tolerates **up to 33% malicious agents**:

```ensemble
orchestrate NewsVerificationRing {
    agents: [ReporterAgent; 100],
    byzantine_tolerance: 33,  // Tolerate 33 malicious agents
    consensus: Threshold(0.85),
}

// Even if 33 agents lie, system reaches correct consensus
```

### 3. Composability

Agents are **composable building blocks**:

```ensemble
// Atomic agent
agent FactChecker { /* ... */ }

// Composite agent (contains sub-agents)
agent Newsroom {
    reporters: Vec<ReporterAgent>,
    fact_checkers: Vec<FactCheckerAgent>,
    editor: EditorAgent,
}

// Agents can be nested arbitrarily deep
```

---

## Agent Model

### Agent Definition

**Syntax:**
```ensemble
agent AgentName {
    // State (private)
    beliefs: BeliefState,
    knowledge: KnowledgeBase,

    // Configuration (public)
    config: AgentConfig,

    // Behaviors (methods)
    fn behavior_name(...) -> ... { }
}
```

**Example:**
```ensemble
agent ReporterAgent {
    // State
    beliefs: BeliefState,
    domain: String,  // e.g., "politics", "science"
    sources: Vec<Source>,

    // Config
    config: AgentConfig {
        update_interval: Duration::from_secs(60),
        credibility_threshold: 0.75,
    },

    // Behaviors
    fn gather_evidence(&mut self, claim: &Claim) -> Evidence {
        // Query sources for evidence
        let raw_evidence = self.sources.iter()
            .filter_map(|s| s.query(claim))
            .collect();

        // Assess credibility
        let credible_evidence = raw_evidence.into_iter()
            .filter(|e| e.credibility >= self.config.credibility_threshold)
            .collect();

        Evidence::new(credible_evidence)
    }

    fn update_belief(&mut self, claim: &Claim, evidence: Evidence) {
        let new_belief = self.beliefs.update(claim, evidence);
        emit BeliefUpdate { agent: self.id, claim, old: self.beliefs[claim], new: new_belief };
    }
}
```

### Agent Lifecycle

```
Create → Initialize → Run → (Message Loop) → Terminate
  ↓         ↓         ↓                         ↓
spawn()  setup()   start()   send/recv      shutdown()
```

**Example:**
```ensemble
fn main() {
    // Create agent
    let mut agent = ReporterAgent::new(domain="politics");

    // Initialize (load knowledge base, connect to sources)
    agent.setup();

    // Start message loop
    let handle = agent.start();

    // Send messages
    handle.send(GatherEvidence { claim: "..."});

    // Receive responses
    let evidence = handle.recv();

    // Shutdown gracefully
    agent.shutdown();
}
```

---

## Belief Fusion

### Dempster-Shafer Theory

**Frame of Discernment:**
```ensemble
type Frame = HashSet<String>;

// Example: Is claim true or false?
let theta = Frame::from(["true", "false"]);
```

**Belief Mass Function:**
```ensemble
type BeliefMass = HashMap<Frame, Probability>;

// Agent A: 70% believe claim is true, 30% uncertain
let m_a = BeliefMass::from([
    (Frame::from(["true"]), 0.7),
    (theta.clone(), 0.3),  // Uncertainty
]);

// Agent B: 50% believe claim is true, 20% false, 30% uncertain
let m_b = BeliefMass::from([
    (Frame::from(["true"]), 0.5),
    (Frame::from(["false"]), 0.2),
    (theta.clone(), 0.3),
]);
```

**Fusion Rules:**

```ensemble
// Dempster's Rule (handles conflict via normalization)
let fused_dempster = fuse(m_a, m_b, rule=FusionRule::Dempster);

// Yager's Rule (assigns conflict to ignorance)
let fused_yager = fuse(m_a, m_b, rule=FusionRule::Yager);

// Dubois-Prade Rule (redistributes conflict)
let fused_dp = fuse(m_a, m_b, rule=FusionRule::DuboisPrade);
```

### Fusion Semantics

**Dempster's Rule:**
```
m₁₂(A) = Σ_{B∩C=A} m₁(B) · m₂(C) / (1 - K)

where K = Σ_{B∩C=∅} m₁(B) · m₂(C)  (conflict)
```

**Properties:**
- **Commutative:** `fuse(m1, m2) == fuse(m2, m1)`
- **Associative:** `fuse(fuse(m1, m2), m3) == fuse(m1, fuse(m2, m3))`
- **Conflict increases:** High conflict → unreliable result (warn!)

**Example:**
```ensemble
fn fuse_all_reporters(reporters: &[ReporterAgent], claim: &Claim) -> BeliefMass {
    let beliefs: Vec<BeliefMass> = reporters.iter()
        .map(|r| r.beliefs.get(claim))
        .collect();

    // Iteratively fuse all beliefs
    beliefs.into_iter().reduce(|acc, m| fuse(acc, m, FusionRule::Dempster))
        .unwrap_or_else(|| BeliefMass::ignorance())  // All uncertain
}
```

---

## Communication

### Message Types

```ensemble
enum Message {
    // Evidence sharing
    Evidence { claim: Claim, evidence: Evidence, sender: AgentId },

    // Belief updates
    BeliefUpdate { claim: Claim, belief: BeliefMass, sender: AgentId },

    // Queries
    Query { claim: Claim, requester: AgentId },
    Response { claim: Claim, belief: BeliefMass, responder: AgentId },

    // Coordination
    ProposeConsensus { claim: Claim, belief: BeliefMass, proposer: AgentId },
    VoteConsensus { claim: Claim, vote: bool, voter: AgentId },

    // Control
    Shutdown,
}
```

### Communication Patterns

**Point-to-Point:**
```ensemble
agent_a.send(agent_b, Message::Evidence { /* ... */ });
```

**Broadcast:**
```ensemble
agent_a.broadcast(all_agents, Message::BeliefUpdate { /* ... */ });
```

**Request-Response:**
```ensemble
let response = agent_a.request(agent_b, Query { claim }).await;
```

**Publish-Subscribe:**
```ensemble
// Subscribe to belief updates for specific claims
agent_a.subscribe("claim_123", |belief_update| {
    println!("Belief updated: {:?}", belief_update);
});

// Publish update
agent_b.publish(BeliefUpdate { claim: "claim_123", /* ... */ });
```

---

## Orchestration

### Comptime Configuration

**Purpose:** Define agent topology at compile-time for type safety and optimization

**Syntax:**
```ensemble
comptime orchestrate OrchestrationName {
    agents: [AgentType; Count],
    topology: TopologyType,
    fusion: FusionRule,
    consensus: ConsensusRule,
}
```

**Example:**
```ensemble
comptime orchestrate NewsVerificationRing {
    agents: [
        ReporterAgent(domain="politics"),
        ReporterAgent(domain="science"),
        ReporterAgent(domain="business"),
        FactCheckerAgent(sources=[Snopes, FactCheck]),
        EditorAgent(threshold=0.85),
    ],
    topology: Ring,
    fusion: Dempster,
    consensus: Threshold(0.85),
}
```

### Topologies

**Ring:**
```
A → B → C → D → E → A
```
- **Pros:** Low message overhead (each agent sends to 1 neighbor)
- **Cons:** Slow propagation (O(n) hops)

**Star:**
```
    B
    ↑
A ← Hub → C
    ↓
    D
```
- **Pros:** Fast propagation (O(1) from hub)
- **Cons:** Hub is bottleneck and single point of failure

**Fully Connected:**
```
A ←→ B
↕ ⤫ ↕
C ←→ D
```
- **Pros:** Fast consensus (direct communication)
- **Cons:** High message overhead (O(n²))

**Custom:**
```ensemble
comptime orchestrate CustomTopology {
    agents: [A, B, C, D],
    edges: [
        (A, B),
        (A, C),
        (B, D),
        (C, D),
    ],
}
```

### Consensus Rules

**Threshold:**
```ensemble
consensus: Threshold(0.85)  // ≥85% confidence required
```

**Unanimous:**
```ensemble
consensus: Unanimous  // All agents must agree
```

**Majority:**
```ensemble
consensus: Majority  // >50% of agents agree
```

**Quorum:**
```ensemble
consensus: Quorum(n=7, threshold=0.9)  // ≥7 agents with ≥90% confidence
```

---

## Epistemic Ledger

### Purpose

- **Audit trail:** Record all belief updates
- **Explainability:** Trace how consensus was reached
- **Accountability:** Detect Byzantine agents
- **Replay:** Reconstruct system state at any point in time

### Structure

```ensemble
struct LedgerEntry {
    timestamp: DateTime,
    agent_id: AgentId,
    claim: Claim,
    old_belief: BeliefMass,
    new_belief: BeliefMass,
    evidence: Evidence,
    signature: Ed25519Signature,  // Cryptographic proof
}

struct EpistemicLedger {
    entries: Vec<LedgerEntry>,
    merkle_root: Hash,  // For tamper detection
}
```

### Operations

**Append:**
```ensemble
ledger.append(LedgerEntry {
    timestamp: now(),
    agent_id: agent.id,
    claim: claim.clone(),
    old_belief: agent.beliefs[claim],
    new_belief: new_belief.clone(),
    evidence: evidence.clone(),
    signature: agent.sign(new_belief),
});
```

**Query:**
```ensemble
// Get all updates for a specific claim
let updates = ledger.query(claim="claim_123");

// Get all updates by a specific agent
let agent_history = ledger.query(agent_id=agent.id);

// Replay system state at timestamp T
let state_at_t = ledger.replay_until(timestamp=T);
```

**Verify:**
```ensemble
// Check ledger integrity (no tampering)
assert!(ledger.verify_merkle_root());

// Check signature of specific entry
assert!(ledger.entries[i].verify_signature());
```

---

## Examples

### Example 1: Simple Newsroom (5 Agents)

```ensemble
comptime orchestrate SimpleNewsroom {
    agents: [
        ReporterAgent(domain="politics"),
        ReporterAgent(domain="science"),
        FactCheckerAgent(sources=[Snopes]),
        EditorAgent(threshold=0.80),
    ],
    topology: Star,  // Editor is hub
    fusion: Dempster,
    consensus: Threshold(0.80),
}

fn main() {
    let mut newsroom = SimpleNewsroom::new();

    // Claim to verify
    let claim = Claim::new("COVID-19 vaccines are safe");

    // Reporters gather evidence
    for reporter in &mut newsroom.reporters {
        let evidence = reporter.gather_evidence(&claim);
        newsroom.broadcast(Message::Evidence { claim, evidence, sender: reporter.id });
    }

    // Fact checker verifies
    let fact_check_result = newsroom.fact_checker.verify(&claim);
    newsroom.broadcast(Message::BeliefUpdate {
        claim,
        belief: fact_check_result,
        sender: newsroom.fact_checker.id,
    });

    // Editor fuses all beliefs
    let consensus = newsroom.editor.fuse_beliefs(&claim);

    if consensus.confidence >= 0.80 {
        println!("Consensus reached: {:?}", consensus);
        newsroom.editor.publish_article(&claim, consensus);
    } else {
        println!("Insufficient confidence, requesting more evidence");
    }

    // Print ledger
    for entry in newsroom.ledger.entries {
        println!("[{}] Agent {:?}: {} → {}",
            entry.timestamp, entry.agent_id, entry.old_belief, entry.new_belief);
    }
}
```

### Example 2: Large-Scale Newsroom (100 Agents)

```ensemble
comptime orchestrate Reuters {
    agents: [
        ReporterAgent(domain="politics"); 20,
        ReporterAgent(domain="business"); 20,
        ReporterAgent(domain="technology"); 20,
        ReporterAgent(domain="science"); 10,
        ReporterAgent(domain="world"); 10,
        FactCheckerAgent(sources=[Snopes, FactCheck, PolitiFact]); 5,
        SourceEvaluatorAgent(credibility_db="sources.json"); 5,
        EditorAgent(threshold=0.85); 5,
        PublisherAgent(platforms=[Web, Mobile, Print]); 5,
    ],
    topology: Custom {
        // Reporters within domain form rings
        rings: [
            Ring(politics_reporters),
            Ring(business_reporters),
            Ring(tech_reporters),
            Ring(science_reporters),
            Ring(world_reporters),
        ],
        // All rings connect to fact-checkers (star topology)
        hubs: fact_checkers,
        // Fact-checkers connect to editors (fully connected)
        fully_connected: [fact_checkers, editors],
        // Editors connect to publishers (pipeline)
        pipeline: editors → publishers,
    },
    fusion: Dempster,
    consensus: Quorum(n=10, threshold=0.85),  // ≥10 agents, ≥85% confidence
    byzantine_tolerance: 33,  // Tolerate up to 33 malicious agents
}

fn main() {
    let mut reuters = Reuters::new();

    // Simulate 24-hour news cycle
    for hour in 0..24 {
        let claims = reuters.fetch_breaking_news();

        for claim in claims {
            // Parallel evidence gathering (async)
            let evidence_futures = reuters.reporters.iter()
                .map(|r| r.gather_evidence_async(&claim))
                .collect::<Vec<_>>();

            let all_evidence = futures::join_all(evidence_futures).await;

            // Fuse beliefs
            let consensus = reuters.fuse_all_evidence(&claim, &all_evidence);

            // Publish if consensus reached
            if consensus.meets_threshold() {
                reuters.publishers.iter()
                    .for_each(|p| p.publish(&claim, &consensus));
            }
        }

        // Sleep for 1 hour
        tokio::time::sleep(Duration::from_hours(1)).await;
    }
}
```

### Example 3: Byzantine Fault Tolerance

```ensemble
comptime orchestrate ByzantineResistant {
    agents: [HonestAgent; 67] + [MaliciousAgent; 33],
    topology: FullyConnected,
    fusion: Dempster,
    consensus: BFTConsensus,  // Byzantine Fault Tolerant
}

fn main() {
    let mut system = ByzantineResistant::new();

    let claim = Claim::new("Water is wet");

    // Honest agents: high confidence
    for agent in &mut system.honest_agents {
        agent.update_belief(&claim, BeliefMass::from([
            (Frame::from(["true"]), 0.95),
            (Frame::theta(), 0.05),
        ]));
    }

    // Malicious agents: try to disrupt (claim water is NOT wet)
    for agent in &mut system.malicious_agents {
        agent.update_belief(&claim, BeliefMass::from([
            (Frame::from(["false"]), 0.99),  // Lie with high confidence
            (Frame::theta(), 0.01),
        ]));
    }

    // BFT consensus ignores malicious minority
    let consensus = system.bft_consensus(&claim);

    assert!(consensus.belief_in("true") > 0.90);  // Correct belief prevails
    println!("Consensus (despite 33 liars): {:?}", consensus);
}
```

---

## Runtime Architecture

### Actor Model

**Implementation:** Elixir (Erlang VM) for fault tolerance and concurrency

```elixir
defmodule ReporterAgent do
  use GenServer  # Elixir actor

  # State
  defstruct [:beliefs, :domain, :sources]

  # Behaviors
  def handle_call({:gather_evidence, claim}, _from, state) do
    evidence = Enum.map(state.sources, &query_source(&1, claim))
    {:reply, evidence, state}
  end

  def handle_cast({:update_belief, claim, evidence}, state) do
    new_beliefs = update_beliefs(state.beliefs, claim, evidence)
    {:noreply, %{state | beliefs: new_beliefs}}
  end
end
```

### Supervision Tree

```
Supervisor (Newsroom)
    ├── ReporterSupervisor
    │   ├── ReporterAgent (politics)
    │   ├── ReporterAgent (science)
    │   └── ReporterAgent (business)
    ├── FactCheckerSupervisor
    │   └── FactCheckerAgent
    ├── EditorSupervisor
    │   └── EditorAgent
    └── LedgerSupervisor
        └── EpistemicLedger
```

**Fault Tolerance:**
- Agent crashes → Supervisor restarts it
- Supervisor crashes → Grandparent restarts whole subtree
- State recovery → Replay from epistemic ledger

---

## Implementation Plan

### Phase 1: Agent Runtime (Q3 2025, 3 months)

- [ ] Elixir actor framework for agents
- [ ] Message passing (send, broadcast, request-response)
- [ ] Agent lifecycle (create, initialize, run, shutdown)
- [ ] Supervision trees for fault tolerance

**Deliverable:** Simple 2-agent ping-pong example

### Phase 2: Belief Fusion (Q4 2025, 3 months)

- [ ] Dempster-Shafer implementation (port from Python)
- [ ] Yager and Dubois-Prade fusion rules
- [ ] Conflict detection and warnings
- [ ] BeliefState integration with Me dialect types

**Deliverable:** 5-agent newsroom with belief fusion

### Phase 3: Epistemic Ledger (Q1 2026, 2 months)

- [ ] Append-only ledger with Merkle trees
- [ ] Ed25519 cryptographic signatures
- [ ] Query and replay functionality
- [ ] Tamper detection

**Deliverable:** Auditable belief updates with replay

### Phase 4: Consensus Algorithms (Q2 2026, 2 months)

- [ ] Threshold consensus
- [ ] Quorum consensus
- [ ] Byzantine fault tolerance (BFT)
- [ ] Timeout and retry handling

**Deliverable:** 100-agent system with BFT

### Phase 5: Orchestration Compiler (Q3 2026, 3 months)

- [ ] Comptime topology specification
- [ ] Code generation for agent networks
- [ ] Static analysis (deadlock detection, etc.)
- [ ] Visualization tools (agent graph, message flow)

**Deliverable:** Compiled Ensemble programs from high-level specs

### Phase 6: Newroom Demonstration (Q4 2026, 3 months)

- [ ] 50-100 journalist agents
- [ ] Real news sources integration (RSS, APIs)
- [ ] Web interface for visualization
- [ ] Performance benchmarks (throughput, latency)

**Deliverable:** Full Reuters-scale demonstration

---

## Open Questions

1. **Scalability:** Can Erlang VM handle 100+ agents with low latency?
   - **Empirical:** Benchmark with realistic message rates
   - **Fallback:** Use distributed Erlang across multiple nodes

2. **Belief Convergence:** How quickly do agents reach consensus?
   - **Analysis:** Prove convergence bounds for different topologies
   - **Simulation:** Monte Carlo analysis with various scenarios

3. **Byzantine Detection:** How to detect malicious agents?
   - **Heuristic:** Flag agents whose beliefs consistently diverge from consensus
   - **Formal:** Use reputation systems (e.g., EigenTrust)

---

## References

1. **Dempster-Shafer Theory** - Glenn Shafer (1976) - Mathematical Theory of Evidence
2. **Actor Model** - Carl Hewitt (1973) - Concurrency model for distributed systems
3. **Byzantine Generals Problem** - Lamport et al. (1982) - Fault tolerance in distributed systems
4. **Erlang OTP** - Joe Armstrong (1993) - Fault-tolerant actor framework
5. **Multi-Agent Systems** - Michael Wooldridge (2009) - Agent architectures and coordination

---

## Changelog

### 2025-11-22 - Initial Draft
- Complete agent model specification
- Dempster-Shafer belief fusion semantics
- Epistemic ledger design
- 3 detailed examples (simple newsroom, Reuters-scale, BFT)
- 18-month implementation roadmap

---

**Next Steps:** Prototype Dempster-Shafer fusion in Python (already in progress), then port to Elixir for actor integration.

