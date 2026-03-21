# Chapter 2: SDLC Fundamentals

> *Before we can transform the Software Development Lifecycle with AI, we need a shared vocabulary: the lifecycle’s phases, the artifacts each phase produces, the models that have governed software delivery for five decades, and — critically — the structural limitations of each model that create the opportunity for AI integration.*

---

## Overview

Chapter 1 made the case that AI is transforming every phase of the SDLC and demonstrated the contrast through the CommercialEdge Bank use case. This chapter steps back to establish the foundational knowledge that the rest of the book builds upon: what the SDLC actually is, what each phase produces, how the dominant methodologies have evolved over five decades, and — most importantly — where each methodology hits a ceiling that only AI augmentation can break through.

This is not a generic primer. Every concept is introduced through the lens of a specific question: what does this phase or model do well, where does it structurally fail, and how does AI address that failure? If you are an experienced practitioner, you may find the phase definitions familiar — but the analysis of persistent limitations and their AI solutions will be new. If you are newer to software engineering, this chapter provides the complete foundation you need to follow the AI-specific chapters that come next.

A deliberate scope boundary: this chapter covers the historical and foundational models — Waterfall through Agile and Lean. The modern practices that build on these foundations — DevOps, DevSecOps, platform engineering, continuous delivery — are covered in Chapter 3.

---

## Learning Objectives

By the end of this chapter, you will be able to:

1. Define the six canonical phases of the SDLC and the artifacts each phase produces, regardless of methodology.
2. Trace the evolution of SDLC models from Waterfall through Iterative, Spiral, and Agile/Lean, understanding what each solved and what it left unresolved.
3. Identify the five structural limitations that persist across all SDLC models — the friction points, handoff losses, and scaling constraints that no methodology has fully overcome.
4. Map each limitation to the specific AI capability that addresses it, establishing the foundation for Chapters 5–22.

---

## 2.1 The Software Development Lifecycle: Definition and Anatomy

The Software Development Lifecycle is the structured process through which software systems are conceived, designed, built, tested, deployed, and maintained. It is not a single methodology or framework — rather, it is the underlying structure that all methodologies organise around. Waterfall, Agile, Lean, and DevOps are different answers to the same question: in what order, at what pace, and with what governance should the work of creating software be performed?

This distinction matters because the SDLC’s phases persist regardless of methodology. An Agile team does not skip requirements analysis or architectural design — it interleaves these activities within sprints rather than performing them as sequential, monolithic stages. A DevOps team does not eliminate testing or deployment — it automates and accelerates them. The work is the same; the timing, granularity, and feedback loops differ.

### The Six Canonical Phases

While different textbooks enumerate the SDLC phases differently, the underlying work clusters into six categories that appear in every methodology, even when they are not explicitly named:

- **Requirements.** Determining what the system should do: the functional and non-functional requirements, the user needs, the business rules, the regulatory constraints. The output is some form of specification — a Product Requirements Document in Waterfall, user stories in Agile, or executable specs in spec-driven development.
- **Design.** Determining how the system should be structured: the architecture, the data model, the API contracts, the integration patterns, the security model. The output is a design that can guide implementation — from formal architecture documents in plan-driven methods to whiteboard sketches and ADRs in Agile teams.
- **Implementation.** Building the system: writing code, configuring infrastructure, integrating components. The output is working software — source code, configuration files, infrastructure-as-code definitions, and the unit tests that verify individual components.
- **Testing.** Verifying that the system works correctly: functional testing, integration testing, performance testing, security testing, user acceptance testing. The output is evidence of quality — test results, coverage reports, defect logs, and sign-off records.
- **Deployment.** Making the system available to users: releasing to production, configuring environments, monitoring launch, executing rollback plans if necessary. The output is a running system — along with the deployment artifacts (release notes, runbooks, rollback procedures) that support it.
- **Maintenance.** Sustaining the system over time: fixing defects, applying security patches, adapting to changing requirements, monitoring performance, and eventually decommissioning the system when it is replaced. Maintenance is the longest phase — most software spends far more time being maintained than being built.

### Mapping CommercialEdge Bank to the Six Phases

To make these phases concrete, consider how the CommercialEdge Bank onboarding platform maps to each. In the Requirements phase, the team must elicit and document the KYC document requirements for each account type, the compliance screening rules for each jurisdiction, the workflow logic for the eight onboarding stages, and the service-level targets for each stage transition. In the Design phase, the team must define the microservices architecture, the data model for clients and onboarding cases (including the nested beneficial ownership structures), the API contracts between services, and the integration patterns with the legacy core banking system.

In the Implementation phase, the team builds the KYC document upload portal, the compliance screening engine, the account provisioning service, and the client-facing progress dashboard. In the Testing phase, the team must verify that compliance screening correctly identifies sanctioned entities, that the document processing pipeline handles the full range of document types, and that end-to-end onboarding completes within the 3–5 day target. In Deployment, the team releases the platform to production with appropriate monitoring, rollback capability, and regulatory sign-off. And in Maintenance, the team must continuously update sanctions lists, adapt to regulatory changes, and respond to incidents — indefinitely.

This mapping is not academic. It reveals that the CommercialEdge Bank project exercises every SDLC phase substantively, which is precisely why it serves as an effective running use case for the entire book.

---

## 2.2 Artifacts and Deliverables Across Phases

Every SDLC phase produces artifacts — the documents, code, configurations, and records that carry information from one phase to the next. These artifacts are the connective tissue of the development process, and they are also the primary targets for AI augmentation.

The following table maps each phase to its key artifacts, identifies who consumes them, and previews the AI augmentation opportunity that subsequent chapters will address in detail:

| SDLC Phase | Key Artifacts | Primary Consumer | AI Augmentation Opportunity |
|------------|---------------|------------------|---------------------------|
| Requirements | User stories, PRD, acceptance criteria, backlog | Design team, architects | AI-generated stories from specs (Ch 5–6), continuous regulatory monitoring |
| Design | Architecture docs, ADRs, API specs, data models, sequence diagrams | Development team | AI-recommended architectures, auto-generated design docs (Ch 7), AI-assisted data models (Ch 8) |
| Implementation | Source code, unit tests, code comments, pull requests | QA team, reviewers | Agentic coding, AI-assisted review, auto-generated tests (Ch 9–10) |
| Testing | Test plans, test cases, defect reports, coverage reports | Dev team (fixes), release mgmt | AI-generated test suites, mutation testing, security scanning (Ch 11) |
| Deployment | Release notes, deployment scripts, runbooks, rollback plans | Operations team | Intelligent CI/CD, predictive builds, automated rollback (Ch 12–13) |
| Maintenance | Incident reports, monitoring dashboards, patch records, updated docs | All teams | AIOps, self-healing, living documentation, legacy modernisation (Ch 13, 17, 21) |

### The Handoff Problem

Every artifact transition between phases is a potential point of information loss. When a business analyst writes a requirements document that an architect interprets into a design, some context is inevitably lost or misunderstood. When a developer implements code based on the design, further context may be lost. When a tester writes test cases based on the requirements, they may not have visibility into design decisions that affect testability. These handoff losses compound across the lifecycle.

To make this concrete, consider tracing a single requirement through the CommercialEdge Bank lifecycle: “The system shall verify beneficial ownership by identifying all individuals who directly or indirectly own more than 25 percent of the corporate client.” In a traditional SDLC, this requirement is documented in a PRD, interpreted by an architect into a data model (which must support nested ownership structures), implemented by a developer as a recursive ownership resolution algorithm, and tested by a QA engineer who must generate test data with multi-layered corporate structures. At each handoff, the original intent becomes more distant from the implementation.

This is not a process failure that better meetings can fix. It is a structural property of any system where different humans interpret and re-express information across phase boundaries. It is also one of the most powerful arguments for AI augmentation: an AI system that maintains a continuous, machine-readable link from requirement through design, code, and test — as spec-driven development does (Chapter 5) — can eliminate the handoff losses that no methodology has been able to resolve through process alone.

> **The Handoff Principle**
>
> Every artifact transition between SDLC phases is a potential information loss point. The cumulative effect of these losses — requirements misunderstood in design, design assumptions lost in code, test coverage gaps from incomplete requirement traceability — is one of the most persistent and expensive problems in software engineering. AI-driven traceability, where a machine-readable chain links every requirement to its design, code, and test, offers the first structural solution.

---

## 2.3 Waterfall and Plan-Driven Models

The earliest formalised SDLC models were plan-driven: they assumed that the full scope of the system could be defined upfront, that phases could be executed sequentially, and that comprehensive documentation at each phase gate was both possible and desirable.

### Waterfall

The Waterfall model, first described by Winston Royce in 1970 and widely adopted in government and defence contracting throughout the 1970s and 1980s, organises the SDLC as a linear sequence: Requirements → Design → Implementation → Testing → Deployment → Maintenance. Each phase must be completed and formally approved before the next begins. There is no mechanism for returning to a previous phase once it has been signed off.

It is worth noting that Royce’s original paper is widely misunderstood. He presented the pure sequential model as a starting point and then explicitly argued that it was “risky and invites failure” without iteration. His paper actually proposed iterative refinement and prototyping as necessary additions. The industry adopted the simplified version and ignored the caveats — a cautionary tale about the gap between academic recommendation and industry practice.

What Waterfall got right was documentation discipline and phase-gate governance. A Waterfall project produces comprehensive requirements documents, detailed design specifications, and formal test plans. Every decision is documented, every approval is recorded, and every phase transition has a defined quality gate. For regulated industries — banking, healthcare, defence — this audit trail is not optional; it is a regulatory requirement.

What Waterfall got wrong was the assumption of perfect foresight. In practice, requirements are never fully known at the start, user needs evolve as they see early implementations, and the cost of late-discovered design errors is catastrophic. The most damaging property of Waterfall is that testing occurs at the end: defects introduced in the Requirements phase are not discovered until the Testing phase, months or years later, when they are orders of magnitude more expensive to fix.

### The V-Model and Spiral

The V-Model addressed one of Waterfall’s weaknesses by explicitly linking each development phase to a corresponding verification phase: requirements are verified by acceptance testing, high-level design by integration testing, and detailed design by unit testing. This creates traceability between what is built and what is tested, which is particularly valuable in safety-critical systems (aerospace, medical devices, automotive).

Barry Boehm’s Spiral Model (1986) introduced risk-driven iteration. Rather than planning the entire project upfront, each “spiral” involves identifying the highest-risk elements, prototyping or analysing them, and using the findings to plan the next spiral. This model was ahead of its time in recognising that uncertainty, not scope, should drive the development process. However, its flexibility made it difficult to apply in organisations that required predictable schedules and fixed budgets.

### Why Plan-Driven Models Persist

Despite their well-documented limitations, plan-driven models persist in regulated industries — and for good reason. Banking regulators, healthcare authorities, and defence procurement agencies require evidence that systematic processes were followed, that requirements were documented before design began, that design was reviewed before implementation started, and that testing was planned and executed according to a defined strategy. These requirements map naturally to Waterfall’s phase-gate structure.

For CommercialEdge Bank, this is not hypothetical. The onboarding platform must satisfy six compliance checkpoints, each of which requires documented evidence of what was built, why it was built, and how it was verified. The bank’s regulators do not accept “we used Agile” as evidence of compliance. They require traceable artifacts.

### AI Opportunity

Here is the critical insight for this book: the choice between documentation discipline and development agility is a false dilemma that AI resolves. AI can provide Waterfall’s documentation discipline — comprehensive, traceable, auditable artifacts at every phase gate — without Waterfall’s rigidity. Spec-driven development (Chapter 5) generates requirements documents, design documents, and implementation plans that are machine-readable and automatically traceable. The Documentation Agent (Chapter 17) maintains living architecture decision records that update as the system evolves. The Governance Agent (Chapter 18) monitors compliance continuously rather than at periodic phase gates.

In other words, AI makes it possible to have Waterfall’s compliance properties and Agile’s adaptive speed simultaneously — a combination that no purely human-driven process has achieved.

> **What Plan-Driven Models Teach Us**
>
> Waterfall’s contribution was not the sequential process (which was its weakness) but the documentation culture (which was its strength). The lesson for AI-augmented SDLC: preserve the discipline of comprehensive, traceable artifacts while eliminating the rigidity of sequential phase gates. This is exactly what spec-driven development, living documentation, and continuous governance deliver.

---

## 2.4 Agile and Lean

The Agile Manifesto, published in 2001 by seventeen software practitioners, was a direct response to the failures of plan-driven development. Its four values — individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan — defined a philosophy that prioritised adaptability, speed, and direct feedback over the predictability and formality of Waterfall.

### The Dominant Implementations

**Scrum** is the most widely adopted Agile framework. It organises work into fixed-length sprints (typically one to four weeks), with a prioritised product backlog, daily standups for coordination, sprint reviews for feedback, and sprint retrospectives for process improvement. A cross-functional team of seven (plus or minus two) members commits to a sprint goal and delivers a potentially shippable increment at the end of each sprint.

**Kanban** takes a different approach, eschewing fixed-length iterations in favour of continuous flow. Work items move through a series of columns (To Do, In Progress, Review, Done) with explicit Work-in-Progress (WIP) limits that prevent the team from overcommitting. Kanban’s strength is its ability to optimise throughput by identifying and eliminating bottlenecks in the flow.

**Extreme Programming (XP)** contributed practices that have become industry standards even outside XP teams: test-driven development (TDD), pair programming, continuous integration, and small, frequent releases. XP’s emphasis on technical discipline complements Scrum’s project management structure.

**Lean software development**, inspired by Toyota’s manufacturing principles, contributed seven principles: eliminate waste, build quality in, create knowledge, defer commitment, deliver fast, respect people, and optimise the whole. Lean’s focus on value stream mapping — identifying and eliminating activities that do not create customer value — has been particularly influential in shaping modern development practices.

### What Agile Solved

Agile’s impact on software development has been transformative. By delivering working software in short cycles, teams receive genuine user feedback weeks into a project rather than months. By embracing changing requirements, Agile accommodates the reality that stakeholders rarely know exactly what they need until they see it. By organising cross-functional teams, Agile reduces the handoff losses that plague siloed organisations. And by valuing individuals and interactions, Agile fosters a culture of collaboration and ownership that improves both productivity and job satisfaction.

For two decades, Agile and its derivatives have been the dominant paradigm for software delivery. The vast majority of professional software organisations today describe themselves as Agile (or aspire to be), and the framework’s influence extends well beyond software into product management, marketing, and even executive strategy.

### What Agile Left Unsolved

Agile’s success, however, has obscured several structural problems that it either created or failed to resolve:

- **Documentation debt.** The Agile Manifesto’s preference for “working software over comprehensive documentation” was intended to prioritise outcomes over bureaucracy. In practice, many teams interpreted this as “documentation is optional.” The result is what practitioners call “the Agile tax”: systems with minimal architecture documentation, outdated API specs, missing onboarding guides, and tribal knowledge that lives in the heads of senior engineers. When those engineers leave, the knowledge goes with them. The CAST technical debt study found that documentation debt is a significant component of the 61 billion workdays of global technical debt.
- **The user-story-is-not-a-requirement problem.** User stories (“As a [role], I want [feature], so that [benefit]”) are excellent for expressing user intent, but they are not specifications. They lack the precision needed for complex regulatory logic, the structure needed for automated test generation, and the traceability needed for compliance audits. For a system like CommercialEdge Bank’s onboarding platform, where compliance rules must be implemented exactly as specified by regulators, user stories alone are insufficient. This is the gap that spec-driven development (Chapter 5) addresses.
- **Scaling challenges.** Agile was designed for small, co-located teams working on a single product. Scaling it to large organisations with multiple teams, shared platforms, and complex dependencies has proven difficult. Frameworks like SAFe (Scaled Agile Framework) attempt to solve this problem, but they add significant process overhead that can undermine the agility they claim to preserve. A common criticism is that SAFe is “Waterfall in Agile clothing” — reimposing sequential planning at the portfolio level while allowing Agile at the team level.
- **Cross-team coordination.** When multiple Agile teams work on the same system, coordination becomes a major challenge. Teams may make conflicting architectural decisions, create duplicate functionality, or introduce integration defects that neither team catches until system testing. The absence of a shared, living design document that reflects the current state of the system — not the state as of the last architecture review — is at the root of this problem.
- **Compliance tension.** For regulated industries, Agile creates a fundamental tension. Agile teams produce working software in short cycles but often struggle to produce the comprehensive documentation that regulators require. The result is a painful dual process: teams run Agile sprints for development while maintaining a parallel Waterfall-style documentation track for compliance. This dual process is expensive, error-prone, and defeats much of Agile’s efficiency advantage. For CommercialEdge Bank, this tension is not theoretical — it is one of the primary motivations for adopting AI-augmented SDLC practices.

### AI Opportunity

AI resolves Agile’s structural weaknesses without sacrificing its strengths. AI can give Agile teams the documentation and traceability they sacrificed for speed. Spec-driven development (Chapter 5) restores structure without sacrificing agility: the specification is a living, machine-readable artifact that evolves with the software, not a static document that falls behind on day one. The Documentation Agent (Chapter 17) automatically generates and maintains API docs, runbooks, and architecture records. The Governance Agent (Chapter 18) continuously produces compliance evidence as a by-product of normal development, eliminating the need for a parallel documentation track.

In this framing, AI does not replace Agile — it completes it. Agile gave us adaptive speed. AI gives us the discipline and traceability that Agile teams have always needed but could never maintain manually.

> **The Agile Paradox**
>
> Agile was designed to prioritise responsiveness over formality. But in regulated industries, formality (documentation, traceability, audit trails) is not optional — it is legally required. This creates a paradox: Agile teams must choose between the agility that makes them effective and the documentation that makes them compliant. AI resolves this paradox by generating compliant documentation as a by-product of development, not as a parallel burden.

### Model Comparison

The following table compares the key characteristics of the SDLC models discussed in this chapter:

| Characteristic | Waterfall | V-Model | Spiral | Agile (Scrum) | Lean/Kanban |
|----------------|-----------|---------|--------|---------------|-------------|
| **Feedback timing** | End of project | End of each V-phase | End of each spiral | Every 1–4 week sprint | Continuous |
| **Change tolerance** | Very low | Low | Medium | High (embraced) | High |
| **Documentation** | Heavy, comprehensive | Heavy, test-focused | Medium, risk-focused | Light (“just enough”) | Minimal |
| **Planning horizon** | Full project upfront | Full project upfront | Per-spiral | Per-sprint + release plan | Just-in-time |
| **Risk management** | Implicit | Test-linked | Explicit | Retrospective-driven | Flow-based (WIP) |
| **Team structure** | Specialised silos | Specialised silos | Small core team | Cross-functional (7±2) | Cross-functional, flexible |
| **Compliance fit** | Strong (audit trail) | Strong (V&V mapping) | Medium | Weak without adaptation | Weak without adaptation |
| **Typical project size** | Large, stable-scope | Safety-critical | High-risk, innovative | Small–medium, evolving | Continuous flow |

---

## 2.5 The Artifact Gap: Why Every Model Leaves the Same Problems

Sections 2.3 and 2.4 traced the evolution of SDLC models from Waterfall through Agile and Lean. Each model solved real problems introduced by its predecessors. Waterfall provided structure and documentation discipline. Agile provided speed and adaptability. Lean provided efficiency and waste elimination. Yet despite these improvements, five structural limitations persist across every model. They are not failures of any particular methodology — they are fundamental constraints of human-driven software development.

### The Five Persistent Limitations

| Persistent Limitation | How It Manifests | Why It Persists | AI Solution (Chapter) |
|-----------------------|------------------|-----------------|-----------------------|
| Traceability decay | Requirements drift from code. Nobody knows which test covers which requirement. Audits take weeks. | Maintaining traceability is manual, tedious, and yields no immediate reward. | Spec-driven development creates machine-readable traceability (Ch 5–6). Governance Agent monitors it (Ch 18). |
| Tribal architecture knowledge | Design lives in heads. ADRs are written months late. Onboarding takes 3–4 months. | Docs compete with feature work and always lose. | Architecture Agent maintains living ADRs (Ch 7). Documentation Agent syncs codebase (Ch 17). |
| Test coverage plateau | Coverage stalls at 60–70%. Complex path tests are tedious to write. | Human creativity for test generation is finite. Diminishing returns make 85%+ coverage unviable manually. | Testing Agent generates tests from acceptance criteria, including edge cases (Ch 11). |
| Documentation debt | API docs, runbooks, and onboarding guides outdated within weeks. | No immediate consequence/pipeline failure when docs are wrong. | Documentation Agent updates docs from code/configs automatically (Ch 17). |
| Retrospective compliance | Audit evidence assembled retroactively, scattered across Jira, Slack. | Compliance treated as an event, not a continuous process. | Governance Agent captures evidence continuously during development (Ch 18). |

### Why These Are Not Methodology Failures

It is tempting to view these limitations as evidence that current methodologies are inadequate and need to be replaced. This is the wrong conclusion. The limitations persist not because Waterfall is too rigid or Agile is too informal, but because all of them ultimately depend on human bandwidth for activities that are repetitive, tedious, and unrewarding: maintaining traceability matrices, updating architecture documents, writing tests for edge cases, keeping API docs current, and compiling compliance evidence.

No process improvement can overcome the fundamental constraint of finite human attention applied to a system of increasing complexity. Every hour a developer spends updating documentation is an hour not spent building features. Every hour spent writing tests for obscure edge cases is an hour not spent on the tests that catch real production defects. The economics of human attention create a ceiling that methodology alone cannot break through.

This is the structural argument for AI in the SDLC. AI does not replace the methodology — it augments the human practitioners within it. AI can maintain traceability continuously (Chapters 5–6). AI can generate and update architecture documentation as the system evolves (Chapters 7, 17). AI can write tests for the edge cases that humans never get to (Chapter 11). AI can produce compliance evidence as a natural by-product of development (Chapter 18). In each case, AI addresses a limitation that every methodology has acknowledged but none has solved.

> **The AI Augmentation Thesis**
>
> The five persistent limitations of the SDLC — traceability decay, tribal architecture knowledge, test coverage plateaus, documentation debt, and retrospective compliance — are not methodology failures. They are human bandwidth constraints. AI addresses them not by replacing the methodology but by augmenting human capacity for the activities that every team knows are important but cannot sustainably perform: maintaining living documentation, generating comprehensive tests, and producing continuous compliance evidence.

### Looking Ahead

Chapter 3 will examine the modern SDLC models — DevOps, DevSecOps, platform engineering, and continuous delivery — that partially address some of these limitations through automation and cultural change. Chapters 5 through 22 will then systematically demonstrate how AI augmentation completes the picture, using the CommercialEdge Bank onboarding platform as the concrete demonstration at every phase.

---

## Key Takeaways

- **The SDLC’s six phases persist regardless of methodology.** Requirements, Design, Implementation, Testing, Deployment, and Maintenance are universal. Agile interleaves them; DevOps automates parts of them; but no methodology eliminates them.
- **Artifacts are the connective tissue of the SDLC — and the target for AI augmentation.** Every phase produces artifacts that carry information. Every handoff is a potential information loss point. AI can generate, validate, and maintain traceability across these artifacts automatically.
- **Waterfall provides documentation discipline but resists change.** Its contribution was the audit trail; its limitation was the assumption of perfect foresight. Regulated industries still require its documentation properties.
- **Agile provides adaptive speed but sacrifices documentation.** The “Agile tax” — documentation debt, scaling challenges, compliance tension — is the structural cost of prioritising working software over comprehensive artifacts.
- **Five structural limitations persist across all models.** Traceability decay, tribal architecture knowledge, test coverage plateaus, documentation debt, and retrospective compliance are human bandwidth constraints, not methodology failures.
- **AI completes the methodology rather than replacing it.** AI can deliver Waterfall’s documentation discipline and Agile’s adaptive speed simultaneously — a combination that no human-driven process has achieved.

---

## Further Reading

1. Winston W. Royce, *"Managing the Development of Large Software Systems,"* Proceedings of IEEE WESCON (1970). The original Waterfall paper.
2. Barry Boehm, *"A Spiral Model of Software Development and Enhancement,"* IEEE Computer (1986). Risk-driven iterative development.
3. Kent Beck et al., *Manifesto for Agile Software Development*, agilemanifesto.org (2001). The four values and twelve principles of Agile.
4. Mary & Tom Poppendieck, *Lean Software Development: An Agile Toolkit*, Addison-Wesley (2003). Lean principles adapted for software.
5. Ken Schwaber & Jeff Sutherland, *The Scrum Guide*, scrumguides.org (2020 edition). The definitive reference to Scrum.
6. David Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*, Blue Hole Press (2010). Foundational work on Kanban.
7. Dean Leffingwell, *SAFe 6.0 Reference Guide: Scaled Agile Framework for Lean Enterprises*, Addison-Wesley (2023). Guide to scaling Agile in enterprise contexts.
8. CAST, *"Coding in the Red: The State of Global Technical Debt 2025,"* castsoftware.com (2025). Quantitative analysis of documentation debt.
9. Ciolkowski, Diebold, Janes & Lenarduzzi, *"The Right Amount of Technical Debt in an Agile Context,"* XP 2024 Conference Proceedings, Springer (2025). Academic analysis of the Agile–technical-debt paradox.
10. McKinsey/QuantumBlack, *"Unlocking the Value of AI in Software Development,"* mckinsey.com (2025). Data on AI capabilities across the PDLC/SDLC.

---

*Next: [Chapter 3 — Modern SDLC Models](../03-modern-sdlc-models/chapter.md)*
