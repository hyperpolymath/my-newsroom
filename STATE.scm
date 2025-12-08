;;; STATE.scm — My-newsroom Epistemic Programming Language Project
;;; CRITICAL: Download this file at end of each session!
;;;           At start of next conversation, upload it.
;;; Format: Guile Scheme (S-expressions)
;;; Spec: https://github.com/hyperpolymath/state.scm

;;;============================================================================
;;; METADATA
;;;============================================================================
(define state-metadata
  '((format-version . "2.0")
    (schema-date    . "2025-12-08")
    (created        . "2025-12-08T00:00:00Z")
    (last-modified  . "2025-12-08")
    (generator      . "claude-opus-4-5-20251101")
    (project-name   . "My-newsroom")
    (project-version . "0.1.0-alpha")))

;;;============================================================================
;;; CURRENT POSITION
;;;============================================================================
(define current-position
  '((summary . "Foundation phase complete with working Dempster-Shafer core.
                Solo compiler lexer implemented, awaiting parser/typechecker/codegen.
                Me dialect playground functional. Duet and Ensemble in spec-only phase.")

    (completion-overview
      (overall-project   . 15)  ; percent
      (julia-core        . 100) ; Dempster-Shafer fully working
      (me-dialect        . 100) ; Playground complete
      (solo-compiler     . 40)  ; Lexer done, parser/typechecker/codegen TODO
      (duet-dialect      . 5)   ; Specification only
      (ensemble-dialect  . 5)   ; Specification only
      (documentation     . 90)  ; Comprehensive but some gaps
      (infrastructure    . 60)) ; CI working, tooling incomplete

    (what-is-working
      "Dempster-Shafer belief fusion (Julia) - all 4 combination rules"
      "Test suite with 11 comprehensive tests"
      "Solo lexer - complete tokenization"
      "Me dialect HTML playground"
      "CI/CD pipeline (GitLab + GitHub)"
      "RSR Bronze compliance (7/7)"
      "Dual licensing (MIT + Palimpsest v0.8)"
      "Governance structure (TPCF model)")

    (what-is-incomplete
      "Solo parser (AST generation)"
      "Solo type checker (affine types)"
      "Solo code generator (QBE backend)"
      "Duet dialect implementation"
      "Ensemble multi-agent runtime"
      "Julia coverage reporting"
      "Reproducible builds (Nix/Docker)"
      "Cross-platform CI"
      "API documentation generation")))

;;;============================================================================
;;; ROUTE TO MVP v1
;;;============================================================================
(define mvp-v1-roadmap
  '((target . "Solo Compiler MVP with end-to-end compilation")
    (target-quarter . "Q1-Q2 2025")

    (milestone-1
      (name . "Parser Implementation")
      (status . "not-started")
      (priority . "critical")
      (tasks
        ("Define AST node types in Rust" . pending)
        ("Implement recursive descent parser" . pending)
        ("Handle operator precedence (Pratt parsing)" . pending)
        ("Parse function definitions with affine annotations" . pending)
        ("Parse belief/where epistemic constructs" . pending)
        ("Parse arena memory management syntax" . pending)
        ("Error recovery and diagnostics" . pending)
        ("Unit tests for parser" . pending)))

    (milestone-2
      (name . "Type Checker")
      (status . "not-started")
      (priority . "critical")
      (depends-on . "milestone-1")
      (tasks
        ("Implement type environment" . pending)
        ("Basic type inference" . pending)
        ("Affine type tracking (use-once semantics)" . pending)
        ("Epistemic type validation" . pending)
        ("Arena lifetime checking" . pending)
        ("Type error messages" . pending)
        ("Integration tests" . pending)))

    (milestone-3
      (name . "QBE Code Generation")
      (status . "not-started")
      (priority . "critical")
      (depends-on . "milestone-2")
      (tasks
        ("QBE IR emission for basic types" . pending)
        ("Function compilation" . pending)
        ("Control flow (if/while)" . pending)
        ("Struct layout and access" . pending)
        ("Arena allocation codegen" . pending)
        ("Link with system libraries" . pending)
        ("End-to-end compilation test" . pending)))

    (milestone-4
      (name . "MVP Integration")
      (status . "not-started")
      (priority . "high")
      (depends-on . "milestone-3")
      (tasks
        ("Compile hello_world.solo successfully" . pending)
        ("Compile belief_example.solo successfully" . pending)
        ("Basic REPL or watch mode" . pending)
        ("Error message polish" . pending)
        ("README update with usage instructions" . pending)
        ("Release v0.2.0 tag" . pending)))

    (success-criteria
      "Solo compiler can take .solo file and produce executable binary"
      "Affine types prevent use-after-move at compile time"
      "Belief types compile to runtime uncertainty tracking"
      "All existing examples compile without errors"
      "Test coverage >= 80%")))

;;;============================================================================
;;; PROJECTS CATALOG
;;;============================================================================
(define projects
  '((project-solo-compiler
      (name . "Solo Dialect Compiler")
      (status . in-progress)
      (completion . 40)
      (category . language)
      (phase . "lexer-complete")
      (blocking . ())
      (next-actions
        "Implement parser module with AST types"
        "Add affine type annotations to grammar"
        "Write parser tests for each construct"))

    (project-julia-core
      (name . "Julia Dempster-Shafer Core")
      (status . complete)
      (completion . 100)
      (category . AI)
      (phase . "production-ready")
      (blocking . ())
      (next-actions
        "Consider package registry publication"
        "Add more fusion rule variants if needed"))

    (project-me-dialect
      (name . "Me Dialect Playground")
      (status . complete)
      (completion . 100)
      (category . language)
      (phase . "demo-ready")
      (blocking . ())
      (next-actions
        "Maintain for demonstration purposes"))

    (project-duet-dialect
      (name . "Duet Human-AI Co-programming")
      (status . paused)
      (completion . 5)
      (category . formal-verification)
      (phase . "specification")
      (blocking . ("solo-compiler-complete"))
      (next-actions
        "Finalize specification"
        "Design SPARK/Ada integration"
        "Plan verification contract syntax"))

    (project-ensemble-dialect
      (name . "Ensemble Multi-Agent Orchestration")
      (status . paused)
      (completion . 5)
      (category . AI)
      (phase . "specification")
      (blocking . ("solo-compiler-complete" "duet-prototype"))
      (next-actions
        "Research Elixir actor model"
        "Design epistemic ledger structure"
        "Plan Byzantine fault tolerance"))

    (project-newroom-demo
      (name . "Newroom 50-100 Agent Demonstration")
      (status . paused)
      (completion . 0)
      (category . AI)
      (phase . "planning")
      (blocking . ("ensemble-runtime"))
      (next-actions
        "Wait for Ensemble dialect"
        "Design agent topology"
        "Plan Reuters-scale scenario"))

    (project-infrastructure
      (name . "CI/CD and Tooling")
      (status . in-progress)
      (completion . 60)
      (category . infrastructure)
      (phase . "bronze-compliant")
      (blocking . ())
      (next-actions
        "Add Julia coverage reporting (Coverage.jl)"
        "Configure Julia formatter"
        "Create Nix flake for reproducibility"
        "Add Dockerfile"
        "Expand to macOS/Windows CI"))

    (project-documentation
      (name . "Documentation & Specifications")
      (status . in-progress)
      (completion . 90)
      (category . education)
      (phase . "comprehensive")
      (blocking . ())
      (next-actions
        "Generate rustdoc for Solo compiler"
        "Generate Documenter.jl API docs"
        "Fill in dialect/ specification gaps"))))

;;;============================================================================
;;; KNOWN ISSUES
;;;============================================================================
(define issues
  '((critical-issues
      ())  ; None currently blocking development

    (high-priority-issues
      ((id . "ISS-001")
       (title . "Solo parser not implemented")
       (description . "Lexer outputs tokens but no parser to create AST")
       (location . "solo-compiler/src/lib.rs:41")
       (workaround . "None - manual testing only"))

      ((id . "ISS-002")
       (title . "RSR Silver compliance degraded")
       (description . "Python→Julia migration broke 5 of 8 Silver requirements")
       (location . "docs/RSR-COMPLIANCE.md")
       (workaround . "Operating at Bronze level")))

    (medium-priority-issues
      ((id . "ISS-003")
       (title . "No Julia test coverage reporting")
       (description . "Coverage.jl not configured")
       (impact . "Cannot verify 80% coverage target"))

      ((id . "ISS-004")
       (title . "PGP key not generated")
       (description . "Security policy references TODO placeholder")
       (location . "SECURITY.md"))

      ((id . "ISS-005")
       (title . "No fuzzing strategy")
       (description . "cargo-fuzz not set up for Solo compiler")
       (impact . "Potential security gaps in parser")))

    (low-priority-issues
      ((id . "ISS-006")
       (title . "Missing dialect specification files")
       (description . "Some docs/dialects/*.md files incomplete or missing"))

      ((id . "ISS-007")
       (title . "CVE placeholders in SECURITY.md")
       (description . "Example CVEs show XXXXX placeholders")))))

;;;============================================================================
;;; QUESTIONS FOR USER
;;;============================================================================
(define questions-for-user
  '((architectural-questions
      ((q . "What's the priority order: Solo compiler completion vs infrastructure improvements?")
       (context . "Both need work - compiler is critical path but infra affects velocity"))

      ((q . "Should Solo target LLVM instead of QBE for broader platform support?")
       (context . "QBE is simpler but less mature; LLVM is complex but production-proven"))

      ((q . "Is Julia the final choice for the Dempster-Shafer core, or should it be rewritten in Rust?")
       (context . "Current split: Julia for math, Rust for compiler. Consider unifying?")))

    (scope-questions
      ((q . "What's the minimum viable feature set for Solo v0.2.0 release?")
       (context . "Full affine types? Or just basic compilation without advanced features?"))

      ((q . "Is the 24-month roadmap to Reuters-scale demo still realistic?")
       (context . "Solo compiler alone is significant work; timeline may need adjustment")))

    (process-questions
      ((q . "Do you want CI to block on test coverage thresholds?")
       (context . "80% coverage target mentioned but not enforced"))

      ((q . "Should we set up GitHub Issues for tracking these items?")
       (context . "Currently tracking via docs; formal issue tracking might help"))

      ((q . "Are there other contributors or is this solo development?")
       (context . "Affects planning, review process, and communication needs")))))

;;;============================================================================
;;; LONG-TERM ROADMAP
;;;============================================================================
(define long-term-roadmap
  '((phase-1
      (name . "Solo MVP")
      (timeline . "Q1-Q2 2025")
      (status . "in-progress")
      (objectives
        "Complete Solo compiler (parser, typechecker, codegen)"
        "Achieve RSR Silver compliance"
        "Validate Dempster-Shafer implementation against literature"
        "Publish Julia package to registry")
      (deliverables
        "solo-compiler v0.2.0 release"
        "Executable binaries from .solo files"
        "Nix flake for reproducible builds"
        "80%+ test coverage"))

    (phase-2
      (name . "Duet Prototype")
      (timeline . "Q3-Q4 2025")
      (status . "not-started")
      (depends-on . "phase-1")
      (objectives
        "Implement Duet dialect specification"
        "Integrate SPARK/Ada formal verification"
        "Build human-AI co-programming demo"
        "Publish first academic paper")
      (deliverables
        "Duet compiler with intent/verify/synth"
        "SPARK proof integration"
        "Research paper draft"))

    (phase-3
      (name . "Ensemble Runtime")
      (timeline . "Q1-Q3 2026")
      (status . "not-started")
      (depends-on . "phase-2")
      (objectives
        "Build multi-agent orchestration runtime"
        "Implement epistemic ledger"
        "Achieve Byzantine fault tolerance"
        "5-agent newsroom prototype")
      (deliverables
        "Elixir/Haskell agent runtime"
        "Belief fusion across agents"
        "5-agent demo scenario"))

    (phase-4
      (name . "Newroom Demonstration")
      (timeline . "Q4 2026")
      (status . "not-started")
      (depends-on . "phase-3")
      (objectives
        "Scale to 50-100 agents"
        "Reuters-scale journalistic verification"
        "Publish flagship research papers"
        "Open-source release")
      (deliverables
        "Full Newroom system"
        "Academic publications (3-5 papers)"
        "Conference presentations"
        "Production deployment guide"))

    (research-papers-planned
      ("Epistemic Programming: A New Paradigm for Uncertain Computation" . 2025)
      ("Dempster-Shafer Belief Fusion for Multi-Agent Journalism" . 2025)
      ("Affine Types Meet Epistemic Logic: The Solo Language" . 2026)
      ("Human-AI Co-Programming with Formal Verification" . 2026)
      ("Politically Autonomous Software: The Newroom Architecture" . 2026))))

;;;============================================================================
;;; CRITICAL NEXT ACTIONS (Top 5)
;;;============================================================================
(define critical-next
  '(((priority . 1)
     (action . "Implement Solo parser with AST types")
     (project . "solo-compiler")
     (rationale . "Blocks all subsequent compiler work")
     (files . ("solo-compiler/src/parser.rs" "solo-compiler/src/ast.rs")))

    ((priority . 2)
     (action . "Add affine type checker to Solo")
     (project . "solo-compiler")
     (rationale . "Core language feature for memory safety")
     (files . ("solo-compiler/src/typechecker.rs")))

    ((priority . 3)
     (action . "Implement QBE code generation")
     (project . "solo-compiler")
     (rationale . "Needed for end-to-end compilation")
     (files . ("solo-compiler/src/codegen.rs")))

    ((priority . 4)
     (action . "Set up Julia coverage reporting")
     (project . "infrastructure")
     (rationale . "Required for RSR Silver compliance")
     (files . (".gitlab-ci.yml" "test/runtests.jl")))

    ((priority . 5)
     (action . "Create Nix flake for reproducible builds")
     (project . "infrastructure")
     (rationale . "RSR Silver requirement; enables reliable CI")
     (files . ("flake.nix" "flake.lock")))))

;;;============================================================================
;;; SESSION FILES (Modified this session)
;;;============================================================================
(define session-files
  '((created
      "STATE.scm")
    (modified
      ())))

;;;============================================================================
;;; HISTORY / SNAPSHOTS
;;;============================================================================
(define history
  '((snapshots
      ((date . "2025-12-08")
       (overall-completion . 15)
       (notes . "Initial STATE.scm creation. Foundation phase complete.")))

    (velocity-data
      (commits-last-30-days . 13)
      (lines-added . "~1500")
      (primary-language . "Julia"))

    (time-estimates
      (solo-parser . "2-4 weeks")
      (solo-typechecker . "3-5 weeks")
      (solo-codegen . "2-3 weeks")
      (mvp-total . "8-12 weeks from now"))))

;;;============================================================================
;;; TECH STACK SUMMARY
;;;============================================================================
(define tech-stack
  '((languages
      (Julia . "1.9+ (Dempster-Shafer core)")
      (Rust . "1.75+ Edition 2021 (Solo compiler)")
      (TypeScript . "Me playground")
      (Elixir . "planned - Ensemble runtime")
      (Haskell . "planned - type system research")
      (Ada . "planned - SPARK formal verification"))

    (tools
      (build . "Justfile + Cargo")
      (ci . "GitLab CI + GitHub Actions")
      (docs . "Markdown + planned Documenter.jl")
      (security . "CodeQL + planned Semgrep"))

    (frameworks
      (belief-fusion . "Dempster-Shafer theory")
      (type-system . "Affine types + Epistemic types")
      (verification . "planned SPARK")
      (actors . "planned OTP/Elixir"))))

;;;============================================================================
;;; QUERY HELPERS (for programmatic access)
;;;============================================================================

;; Get current focus project
(define (current-focus)
  "Solo Dialect Compiler - Parser Implementation")

;; Get all blocked projects
(define (blocked-projects)
  (filter (lambda (p) (eq? (assoc-ref p 'status) 'blocked))
          (cdr projects)))

;; Get completion percentage
(define (overall-completion)
  15)  ; percent

;; End of STATE.scm
