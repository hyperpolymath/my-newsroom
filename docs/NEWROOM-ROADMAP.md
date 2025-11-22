# Newroom Project: Demonstration Roadmap

**Version:** 1.0.0
**Timeline:** 24 months (Q1 2025 - Q4 2026)
**Goal:** Build Reuters-scale distributed newsroom with 50-100 AI agents using Ensemble dialect

---

## Executive Summary

**Newroom** demonstrates how the My Language family enables epistemic programming for journalism:

- **50-100 specialized agents** (reporters, fact-checkers, editors)
- **Dempster-Shafer belief fusion** for evidence combination
- **Byzantine fault tolerance** (tolerates 33% malicious agents)
- **Epistemic ledger** for audit trails and explainability
- **Offline-first** architecture (works air-gapped)

**Expected Impact:**
- Prove viability of neurosymbolic AI for journalism
- Publishable research (5 papers, 9 conference talks)
- Potential commercial deployment (if successful)

---

## Four-Phase Plan

### Phase 1: Foundation (Q1-Q2 2025, 6 months)

**Goal:** Working Dempster-Shafer implementation + Solo compiler MVP

**Deliverables:**
- ✅ Python prototype of Dempster-Shafer fusion
- ✅ Solo dialect parser + type checker
- ✅ QBE backend for code generation
- ✅ "Hello World" in Solo (compiled to native binary)

**Milestones:**
- Month 1: Dempster-Shafer math validated
- Month 3: Solo parser complete
- Month 6: Solo MVP compiling simple programs

**Team:** 1-2 people, part-time
**Budget:** £10-20k (tools, cloud resources)

---

### Phase 2: Verification (Q3-Q4 2025, 6 months)

**Goal:** Duet dialect with SPARK formal verification

**Deliverables:**
- ✅ Duet syntax finalized
- ✅ Integration with SPARK/Ada verifier
- ✅ Verified Dempster-Shafer implementation
- ✅ AI synthesis prototype (@synth holes)

**Milestones:**
- Month 9: Duet → Ada translation working
- Month 10: First verified function (Dempster fusion)
- Month 12: AI synthesis generates correct candidates

**Team:** 2-3 people (compiler, verification, AI)
**Budget:** £30-50k

---

### Phase 3: Agents (Q1-Q3 2026, 9 months)

**Goal:** Ensemble dialect runtime with 5-agent newsroom

**Deliverables:**
- ✅ Elixir actor framework for agents
- ✅ Agent types (Reporter, FactChecker, Editor)
- ✅ Belief fusion in distributed system
- ✅ Epistemic ledger with signatures
- ✅ 5-agent proof-of-concept

**Milestones:**
- Month 15: Agent runtime working
- Month 17: Belief fusion between 2 agents
- Month 19: 5-agent newsroom running end-to-end
- Month 21: Epistemic ledger with audit trails

**Team:** 3-5 people (distributed systems, AI, UI)
**Budget:** £60-100k

---

### Phase 4: Scale (Q4 2026, 3 months)

**Goal:** 50-100 agents, Reuters-scale demonstration

**Deliverables:**
- ✅ 50-100 agent deployment
- ✅ Real news sources integration (RSS, APIs)
- ✅ Web dashboard for visualization
- ✅ Performance benchmarks (throughput, latency)
- ✅ Academic paper submission (5 papers)
- ✅ Conference talks (3-5 accepted)

**Milestones:**
- Month 22: 50 agents running stably
- Month 23: 100 agents with BFT consensus
- Month 24: Public demo + paper submissions

**Team:** 5-9 people (full stack + research)
**Budget:** £100-150k

---

## Total Resources

**Timeline:** 24 months
**Team:** Grows from 1 → 9 people
**Budget:** £200k - £320k total
  - Year 1: £40-70k (foundation + verification)
  - Year 2: £160-250k (agents + scale)

**Funding Sources:**
- Academic grants (EPSRC, EU Horizon, NSF)
- News organization partnerships (Reuters, Guardian, NYT)
- Philanthropic funding (Knight Foundation, Craig Newmark)

---

## Key Milestones & Demos

| Month | Milestone | Demo |
|-------|-----------|------|
| **3** | Solo MVP | Compile "Hello World" to native binary |
| **6** | Dempster-Shafer | Fuse 2 belief masses, show conflict resolution |
| **12** | Duet AI Synthesis | AI generates verified sorting algorithm |
| **15** | Agent Runtime | 2 agents ping-pong messages |
| **19** | 5-Agent Newsroom | Verify 1 claim end-to-end with belief fusion |
| **22** | 50 Agents | Process 100 claims/hour with <1s latency |
| **24** | Reuters-Scale | 100 agents, real news, public web demo |

---

## Technical Architecture

### Agent Types (50-100 total)

```
├── Reporters (40-60 agents)
│   ├── Domain specialists (politics, science, tech, etc.)
│   └── Geographic coverage (US, EU, Asia, etc.)
│
├── Fact-Checkers (10-15 agents)
│   ├── Source verification
│   ├── Cross-reference checking
│   └── Bias detection
│
├── Editors (5-10 agents)
│   ├── Belief fusion
│   ├── Consensus decisions
│   └── Publishing approval
│
└── Publishers (5-10 agents)
    ├── Web formatting
    ├── Mobile optimization
    └── Social media distribution
```

### Belief Fusion Pipeline

```
1. Reporters gather evidence
     ↓
2. Evidence → Belief masses (Dempster-Shafer)
     ↓
3. Fact-checkers verify sources
     ↓
4. Editors fuse all belief masses
     ↓
5. Consensus check (≥85% confidence)
     ↓
6. Publish article OR request more evidence
     ↓
7. Log to epistemic ledger
```

### Performance Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| **Throughput** | 100 claims/hour | Realistic news volume |
| **Latency** | <1s per claim | Real-time verification |
| **Consensus Time** | <10s for 100 agents | Acceptable wait for editors |
| **Uptime** | 99.9% (8.76 hours/year downtime) | Production-grade |
| **Byzantine Tolerance** | 33% malicious agents | Standard BFT assumption |

---

## Research Outputs

### 5 Academic Papers

1. **"My Language: Epistemic Programming for Journalism"** (ICSE 2026)
   - Language design, 4 dialects, Newroom case study

2. **"Dempster-Shafer Belief Fusion in Multi-Agent Systems"** (PLDI 2026)
   - Formal semantics, correctness proofs, performance analysis

3. **"Byzantine Fault Tolerance for Newsroom Agents"** (Middleware 2026)
   - BFT consensus, epistemic ledger, attack resistance

4. **"Human-AI Verification with Duet Dialect"** (CHI 2026)
   - User study: @synth holes improve productivity by 40%

5. **"Emotional Temperature Metrics in Epistemic Systems"** (CHASE 2026)
   - Developer well-being when using formal verification

### 9 Conference Talks

- FOSDEM 2025: "Post-JavaScript Liberation" (30 min)
- RustConf 2025: "Beyond Rust: Epistemic Systems Programming" (45 min)
- ElixirConf 2025: "Distributed Belief Fusion with Actors" (45 min)
- DEF CON 2026: "10+ Dimensions of Security in Newsroom AI" (60 min)
- Strange Loop 2026: "Dempster-Shafer for Distributed Consensus" (45 min)

---

## Success Criteria

### Technical Success

- ✅ **100 agents** running concurrently
- ✅ **<1s latency** for claim verification
- ✅ **99.9% uptime** over 1 month
- ✅ **33% Byzantine tolerance** demonstrated
- ✅ **Zero memory leaks** (Rust/Elixir safety)

### Research Success

- ✅ **≥3 papers accepted** at top-tier venues (ICSE, PLDI, CHI)
- ✅ **≥5 talks accepted** at conferences
- ✅ **≥100 citations** within 2 years (ambitious)

### Impact Success

- ✅ **≥1 news organization** pilots Newroom
- ✅ **≥10,000 GitHub stars** (community adoption)
- ✅ **≥50 contributors** (TPCF Perimeter 3)

---

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Solo compiler delays** | High | High | Prototype in Python first, port later |
| **SPARK verification too slow** | Medium | Medium | Allow proofs to be skipped in dev mode |
| **AI synthesis unreliable** | Medium | Low | Human fallback for @synth holes |
| **BFT consensus fails** | Low | High | Extensive testing with adversarial scenarios |
| **Funding shortfall** | Medium | High | Bootstrap with academic grants first |

---

## Open Questions

1. **Can Dempster-Shafer scale to 100 agents?**
   - **Test:** Benchmark fusion with N=10, 50, 100, 1000
   - **Fallback:** Hierarchical fusion (fuse within domains first)

2. **Will news organizations adopt this?**
   - **Validate:** User interviews with journalists and editors
   - **Pivot:** If not adopted, publish as research contribution only

3. **Is 24 months realistic?**
   - **Conservative:** Add 6-month buffer (30 months total)
   - **Aggressive:** Parallelize work with larger team

---

## Next Steps (This Week)

1. **Duet spec review** - Finalize syntax decisions
2. **Ensemble spec review** - Agent protocol details
3. **Dempster-Shafer Python** - Implement fusion rules
4. **Solo parser fix** - Get "Hello World" compiling

---

**Questions?** Contact project lead or open GitLab issue.

**Want to contribute?** See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to join the team!
