# Chapter 6: AI-Assisted Requirements & Planning

> *"The cost of fixing a defect in requirements is 100 times cheaper than fixing it in production. AI does not change this math — it amplifies it. If AI helps you get requirements right, the leverage is enormous. If AI hallucinates requirements, the damage is catastrophic."*

---

## Overview

Chapter 5 produced the initial spec artifacts for the CommercialEdge Bank onboarding platform: a product vision, viability hypotheses, and structured specifications generated through spec-driven development. But those artifacts are a starting point, not a finish line. They capture the product manager's intent. They do not yet capture the full depth of stakeholder needs, the edge cases that only compliance officers know about, the performance constraints that only the operations team can articulate, or the regulatory nuances that only the legal department understands.

This chapter transforms those initial specifications into sprint-ready, engineering-grade requirements. It covers the full requirements pipeline: eliciting requirements from stakeholders and documents, generating structured user stories, analysing specifications for gaps and contradictions, estimating effort with AI-assisted techniques, and building a prioritised backlog ready for sprint planning. At every stage, AI augments human judgment rather than replacing it.

The approach follows a principle drawn from decades of requirements engineering research: 68 percent of software projects fail due to poor requirements, not inadequate coding (Standish Group, CHAOS Report). A defect introduced in requirements and discovered in production costs 100 times more to fix than one caught during elicitation (Boehm's cost escalation model). AI that improves requirements quality has outsized return on investment. AI that hallucinates requirements creates outsized damage. This chapter shows you how to achieve the former and prevent the latter.

> **Agents in This Chapter**
>
> This chapter covers the work of three agents from the Agentic PDLC architecture (Figure 1.11):
>
> - **Project Background Agent (§6.1–6.2)** — synthesises project context from specifications, stakeholder interviews, and existing documentation into structured background artifacts (SOP, HLSD, BDD documentation)
> - **Epic Agent (§6.5)** — decomposes the product vision into structured epics with acceptance criteria, dependency maps, and priority classifications
> - **Story Agent (§6.3)** — generates user stories with EARS acceptance criteria from validated specifications, including edge cases and non-functional requirements

## Learning Objectives

By the end of this chapter, you will be able to:

1. Connect Chapter 5's spec artifacts to engineering-grade requirements through AI-augmented elicitation workflows.
2. Generate and refine user stories using structured prompting techniques (EARS notation, CPFC pattern, INVEST scoring).
3. Apply AI-driven specification analysis for gap detection, ambiguity resolution, and consistency checking.
4. Implement AI-assisted estimation that combines historical data with LLM reasoning, producing ranges rather than false-precision point estimates.
5. Build AI-powered backlog refinement workflows with WSJF prioritisation and dependency mapping.
6. Produce a complete requirements package for CommercialEdge Bank that feeds directly into Chapter 7 (Design & Architecture).

---

## 6.1  From Spec to Requirements: Picking Up Where Chapter 5 Left Off

It's Monday morning at CommercialEdge Bank. The product team has just completed the spec-driven development process described in Chapter 5. They have a requirements.md with initial user stories, a design.md with a proposed architecture, and a tasks.md with 42 implementation tasks. The product manager, Priya, is satisfied — these artifacts capture the platform's product vision clearly.

But when Priya shares the specs with Sarah, the bank's Compliance Officer, Sarah reads Story 2.3 ('Screen corporate clients against sanctions lists') and immediately spots three gaps: 'What about the beneficial owners, not just the company? What about re-screening when lists update mid-onboarding? And what's the fallback if the screening API goes down?'

Three sentences from one stakeholder just revealed three missing requirements that the spec-driven process — working from product vision and regulatory documentation — could not have captured. This is why requirements elicitation exists as a distinct discipline. The spec gives you 70 percent. Stakeholder expertise gives you the other 30 percent — the 30 percent that determines whether the system is compliant or merely functional.

Chapter 5 produced the PDLC's output: validated spec artifacts. This chapter takes those artifacts — and the raw inputs they were derived from (stakeholder interviews, regulatory documents, competitive analysis, existing process documentation) — and transforms them into sprint-ready requirements. The relationship is straightforward: Chapter 5 answers "what should we build and why?" This chapter answers "what exactly does each part need to do, for whom, under what constraints, and how will we know it's done?"

### The Requirements Pipeline

The transformation from spec to sprint-ready backlog follows six stages. Each stage is covered in a section of this chapter, and each is augmented by AI in specific, well-defined ways:

| Stage | What Happens | AI Role | Section |
|-------|-------------|---------|---------|
| 1. Elicitation | Discover requirements from stakeholders, documents, and existing systems | Transcription, extraction, stakeholder discovery, gap identification | §6.2 |
| 2. Story generation | Structure requirements as user stories with acceptance criteria | EARS-notation generation, CPFC pattern, edge case identification | §6.3 |
| 3. Spec analysis | Validate stories for gaps, ambiguity, contradictions, and completeness | Automated quality checking across the full requirement set | §6.4 |
| 4. Estimation | Predict effort for each story using historical data and AI reasoning | Analogy-based estimation, Monte Carlo simulation, range prediction | §6.5 |
| 5. Backlog refinement | Prioritise, decompose, and sequence stories into sprint-ready backlog | WSJF scoring, epic decomposition, dependency mapping | §6.6 |
| 6. Output packaging | Produce the complete requirements package for Chapter 7 | Traceability matrix, artifact consolidation | §6.8 |

> 📓 **Notebook 6.1 — The Full Pipeline**
>
> The companion notebook for this chapter runs the complete requirements pipeline end-to-end against the CommercialEdge Bank use case. Start here if you want to see the whole journey before diving into individual sections. The notebook processes actual FCA regulatory guidelines, generates structured requirements, and produces a sprint-ready backlog.

---

## 6.2  AI for Requirements Elicitation

### The Scene: A Requirements Workshop

CommercialEdge Bank's onboarding requirements workshop has five people in the room. Sarah (Compliance Officer) cares about FCA adherence and sanctions screening. David (Relationship Manager) cares about client experience and time-to-revenue. Elena (Risk Analyst) cares about credit exposure and operational risk. Raj (Operations Lead) cares about process efficiency and SLA adherence. And Priya (Product Manager) is trying to capture everything they say into requirements that engineers can implement.

In a traditional workshop, Priya would take notes, synthesise them overnight, send a draft PRD for review, incorporate feedback over two weeks, and repeat. With AI augmentation, something different happens.

### Step 1: AI Captures What Everyone Says

An AI meeting assistant (Otter.ai, Fireflies.ai, Microsoft Copilot for Teams) transcribes the workshop in real-time, identifying each speaker and timestamping every statement. But transcription is just the starting point. The AI simultaneously classifies each statement into categories:

| Statement Category | Example from the Workshop | What the AI Does |
|--------------------|---------------------------|-------------------|
| Functional requirement | Sarah: 'We need to screen all UBOs who own more than 25 percent against sanctions lists.' | Extracts, assigns ID (FR-007), classifies as Must-Have, flags as compliance-critical |
| Non-functional requirement | Raj: 'The screening has to complete within 30 seconds or the RM loses the client's attention.' | Extracts, assigns ID (NFR-003), classifies as performance SLA, links to FR-007 |
| Constraint | Elena: 'We can only use data sources approved by the FCA for sanctions screening.' | Extracts, assigns ID (CON-002), classifies as regulatory constraint, flags for legal review |
| Assumption | David: 'I'm assuming clients will upload documents through the portal, not email them.' | Extracts, flags as assumption requiring validation, creates verification task |
| Ambiguity | Sarah: 'The system should handle high-risk clients differently.' | Flags: 'differently' is undefined. Generates clarifying question: 'What specific additional checks apply to high-risk clients?' |

Notice what happened: a 90-minute workshop produced a transcript that AI transformed into 23 candidate requirements, 4 non-functional requirements, 3 constraints, 6 assumptions, and 5 ambiguities requiring clarification — all structured, categorised, and cross-referenced. Manually, this synthesis would take Priya two to three days. With AI, the structured output is available within an hour of the workshop ending.

### Step 2: AI Discovers Stakeholders You Missed

Before the workshop, AI can accelerate stakeholder discovery — a step that traditional requirements engineering handles informally and often incompletely:

| Technique | How AI Helps | CommercialEdge Bank Result |
|-----------|-------------|----------------------------|
| Organisational analysis | AI parses org charts and role descriptions to identify impacted teams | Compliance, Risk, Sales, Operations, Legal, and IT Security all touch the onboarding workflow |
| Communication mining | AI analyses email and Slack patterns to find informal stakeholders | The Fraud Operations Lead (not initially listed) is cc'd on 40% of high-risk escalations — a critical stakeholder |
| Regulatory mapping | AI identifies compliance stakeholders based on domain regulations | FCA regulations require Money Laundering Reporting Officer (MLRO) involvement — not on the original invite list |
| Integration analysis | AI maps system integrations to identify upstream and downstream teams | Core banking team, AML screening API team, and CRM team are technical stakeholders |

For CommercialEdge Bank, running AI-assisted stakeholder discovery identified two people the project sponsor had not considered: the MLRO (for FCA compliance sign-off) and the Master Data Management lead (for entity resolution downstream). Missing either would have created gaps discovered late in development — exactly the kind of expensive late-stage rework that requirements engineering exists to prevent.

### Step 3: AI Extracts Requirements from Existing Documents

The CommercialEdge Bank project has a substantial body of existing documentation: FCA regulatory guidelines, the bank's current onboarding manual (47 pages), the existing compliance screening procedure, and three years of audit findings. Manually reading and extracting requirements from this corpus would take weeks. AI processes it in hours.

The extraction follows a specific pattern: the AI reads each document, identifies statements that express requirements (using linguistic markers like 'shall,' 'must,' 'required to'), classifies each as functional, non-functional, or constraint, assigns a priority based on the document's authority level (regulatory guidelines rank higher than internal memos), and flags ambiguities and conflicts with previously extracted requirements.

For CommercialEdge Bank, processing the FCA guidelines alone yielded 31 regulatory requirements that the product team had not explicitly included in their Chapter 5 specs. Fourteen of these were genuinely new (the specs had captured the intent but missed the specific regulatory language). Seventeen were already covered but the traceability link was not explicit — which matters for audit purposes.

> 📓 **Notebook 6.2 — Requirements Extraction Pipeline**
>
> This notebook implements the full extraction pipeline against the CommercialEdge Bank regulatory documentation. You'll feed FCA guidelines and the bank's onboarding manual to the AI, see the structured requirements output, and modify the extraction prompt to adapt it to your own domain. The notebook demonstrates extraction, deduplication, and conflict detection across multiple source documents.

### The EARS Pattern: Giving AI a Grammar for Requirements

Here is a finding that changes how you prompt AI for requirements: LLMs produce significantly higher-quality requirements when given a structured template versus free-form generation. Research from Lancaster University showed that structured prompting increased requirements quality by 40 to 60 percent. The most effective template for AI-generated requirements is EARS — the Easy Approach to Requirements Syntax.

EARS provides five sentence patterns, each designed for a specific type of requirement. Let us see each one in action with the CommercialEdge Bank use case:

| EARS Pattern | Template | CommercialEdge Bank Example |
|-------------|----------|------------------------------|
| Ubiquitous (always true) | The \<system\> shall \<action\> | The onboarding platform shall encrypt all customer data at rest using AES-256 encryption. |
| Event-driven (triggered) | When \<trigger\>, the \<system\> shall \<action\> | When a client uploads a KYC document, the system shall classify the document type and begin extraction within 5 seconds. |
| Unwanted (exception handling) | If \<condition\>, then the \<system\> shall \<action\> | If the sanctions screening API is unavailable, then the system shall queue the screening request and retry every 60 seconds for up to 4 hours. |
| State-driven (during a state) | While \<state\>, the \<system\> shall \<action\> | While an onboarding case is in compliance review, the system shall prevent the case from advancing to account opening. |
| Optional (feature-dependent) | Where \<feature\>, the \<system\> shall \<action\> | Where the client has requested a Trade Finance account, the system shall require additional documentation: letter of credit terms and trade counterparty details. |

The power of EARS for AI-assisted development is not just clarity for human readers. Each EARS pattern maps directly to a testable assertion: an event-driven requirement becomes a test case ("trigger the event, verify the action"), a state-driven requirement becomes a state-transition test, and an unwanted-behaviour requirement becomes an exception-path test. When the Testing Agent (Chapter 11) generates test suites from these requirements, the EARS structure gives it unambiguous input.

> **Why EARS Matters for the Agentic PDLC**
>
> In the agentic PDLC, requirements flow from the Story Agent (this chapter) to the Architecture Agent (Chapter 7), the Coding Agent (Chapter 9), and the Testing Agent (Chapter 11). Every downstream agent consumes the requirements produced here. EARS notation ensures those requirements are unambiguous and machine-readable, reducing the handoff losses identified in Chapter 2. When you prompt AI to generate requirements, always request EARS syntax.

---

## 6.3  User Story Generation and Refinement

### The Scene: From Requirement to Story

Priya has 23 functional requirements extracted from the workshop, 31 from regulatory documents, and the initial stories from Chapter 5's requirements.md. She needs to transform this raw material into user stories that are independent, estimable, and testable — stories an engineering team can pick up in sprint planning and start implementing immediately.

She opens the Story Agent and feeds it requirement FR-007: 'The system shall screen all beneficial owners who directly or indirectly own more than 25 percent of the corporate client against global sanctions lists, with screening completing within 30 seconds.'

What comes back is not one story. It is four: the base screening story, the fuzzy-match escalation story, the re-screening trigger story, and the API failure fallback story. Each has acceptance criteria in Given/When/Then format, edge cases, non-functional requirements, and dependency declarations. FR-007 has been decomposed into implementable, testable units.

This decomposition illustrates a key principle: a requirement and a user story are not the same thing. A requirement describes what the system must do. A user story describes a slice of user value that can be independently delivered and tested. AI excels at this decomposition because it can systematically identify the personas, scenarios, edge cases, and failure modes implicit in a single requirement statement.

### The CPFC Prompt Pattern

The most effective prompting pattern for user story generation is CPFC: Context, Persona, Feature, Criteria. Let us build it step by step, explaining why each component matters:

**Context** provides the project backdrop. Without it, the AI generates generic stories. With it, the stories reflect CommercialEdge Bank's specific domain, technology stack, and constraints. Context includes the project description, the tech stack (microservices, event-driven, cloud-hosted), the sprint cadence (two weeks), and any architectural decisions from Chapter 7's design.md.

**Persona** defines who the story serves. CommercialEdge Bank has four primary personas: Sarah the Compliance Officer (approves high-risk clients, ensures FCA adherence), David the Relationship Manager (owns client relationships, needs fast time-to-revenue), Elena the Risk Analyst (assesses credit and operational risk), and the Corporate Client (submits documents, expects a frictionless digital journey). Each persona has different needs from the same system.

**Feature** describes the high-level capability being broken down. This comes directly from the epic or requirement being decomposed.

**Criteria** specifies what the output must include: user story format, acceptance criteria format (Given/When/Then), edge cases, non-functional requirements, dependencies, and complexity estimate. The more specific the criteria, the higher the quality of the output.

Here is the prompt that generated the sanctions screening stories for CommercialEdge Bank. Notice how each CPFC component shapes the output quality:

> **CPFC Prompt: Sanctions Screening User Stories**
>
> **Context:** We are building a digital corporate client onboarding platform for CommercialEdge Bank, a mid-sized commercial bank. The platform replaces a manual 4-week process with a 3–5 day digital workflow across 8 stages. Tech stack: microservices on cloud infrastructure, event-driven architecture, PostgreSQL with vector extension. Sprint cadence: 2 weeks.
>
> **Personas:** (1) Sarah, Compliance Officer — approves high-risk clients, ensures FCA/AML adherence. (2) David, Relationship Manager — owns client relationships, needs fast time-to-revenue. (3) Elena, Risk Analyst — assesses credit and operational risk. (4) Corporate Client — submits documents, expects frictionless experience.
>
> **Feature:** Automated AML/Sanctions Screening — Screen incoming corporate clients and their beneficial owners against global sanctions lists (OFAC, UN, EU) and PEP databases automatically, flagging matches for human review.
>
> **Criteria:** Generate 4–6 user stories. Each must include: user story in 'As a [persona], I want [feature], so that [benefit]' format; 3–5 acceptance criteria in Given/When/Then with EARS notation; edge cases and error scenarios; non-functional requirements (performance, security, audit); dependencies on other stories; estimated complexity (S/M/L/XL).

### What Comes Back: A Generated Story

The AI generates several stories. Here is one of them — the core sanctions screening story for CommercialEdge Bank. Examine how the CPFC context shapes every detail:

| Element | Content |
|---------|---------|
| **Story** | As a Compliance Officer, I want the system to automatically screen new corporate clients and their UBOs against global sanctions lists, so that I can prevent onboarding of prohibited entities and ensure full FCA compliance without manual lookups. |
| **Acceptance criteria 1** | Given a new client profile is submitted, When the system runs background checks, Then it screens the company name and all UBOs (>25% ownership) against OFAC, UN, and EU sanctions lists within 30 seconds. |
| **Acceptance criteria 2** | Given a screening returns a fuzzy match (confidence >80%), When the screening completes, Then the system flags the application as 'High Risk — Pending Review' and sends a notification to the assigned Compliance Officer. |
| **Acceptance criteria 3** | Given no matches are found across any watchlist, When the screening completes, Then the system updates the AML status to 'Cleared' and advances the case to the next onboarding stage. |
| **Acceptance criteria 4** | Given multiple partial matches exist, When the system identifies candidates, Then it presents the top 3 matches ranked by confidence score with matching criteria highlighted. |
| **Edge cases** | (1) Sanctions API temporarily unavailable; (2) Entity name in non-Latin characters; (3) UBO matches but parent company does not; (4) Entity recently removed from sanctions list |
| **NFR: Performance** | Screening must complete within 30 seconds for 95th percentile. System must handle 500+ screenings per hour at peak. |
| **NFR: Audit** | All screening results and confidence scores must be immutably logged (FCA audit requirement). |
| **Dependencies** | Requires: Entity Resolution Service (Story 4.1), Sanctions API Integration (Story 4.2) |
| **Complexity** | M (Medium) — API integration is well-defined; complexity is in fuzzy matching logic and escalation workflow |

### Evaluating Story Quality: The INVEST Framework

Not every AI-generated story is good. The INVEST framework provides six criteria for evaluating user story quality. Here is how AI-generated stories perform against each, and what to watch for:

| INVEST Criterion | What It Means | AI Tendency | What to Watch For |
|-----------------|---------------|-------------|-------------------|
| **Independent** | Can be delivered without other stories | AI often generates coupled stories that share data or logic | Check that each story can be implemented and deployed independently. If not, split or resequence. |
| **Negotiable** | Details can be discussed; not a contract | AI generates precise language that feels final | Review for over-specification — the story should define WHAT, not HOW. |
| **Valuable** | Provides value to a stakeholder | AI may generate technically-driven stories with no user benefit | Every story must answer: which persona benefits, and how? |
| **Estimable** | Team can estimate effort | AI generally produces well-scoped stories | Verify the scope is clear enough for the team to estimate without asking 10 questions. |
| **Small** | Fits in a single sprint | AI may generate epics disguised as stories | If the story has 8+ acceptance criteria, it's probably too large. Decompose further. |
| **Testable** | Has clear, measurable acceptance criteria | AI excels here — Given/When/Then is its sweet spot | Validate against actual business rules, not just plausible-sounding criteria. |

> ⚠️ **The Hallucination Risk in Story Generation**
>
> AI can generate stories that sound perfect but contain hallucinated business rules. For example, an AI might generate 'Given a UBO owns more than 10% of the entity' when the actual regulatory threshold is 25%. Or it might invent an approval workflow that doesn't match the bank's actual compliance procedures. Every AI-generated acceptance criterion must be validated against the source requirement and confirmed by the relevant domain expert. For CommercialEdge Bank, Sarah (Compliance) validates all compliance stories, Elena (Risk) validates all risk stories, and David (RM) validates all client-facing stories. This validation loop is non-negotiable.

> 📓 **Notebook 6.3 — User Story Generation and Quality Scoring**
>
> This notebook generates the full set of user stories for CommercialEdge Bank's onboarding platform using the CPFC prompt pattern. You'll see the AI generate stories for each of the 8 onboarding stages, score them against INVEST criteria, and flag stories that need human refinement. Modify the personas and context to generate stories for your own project.

---

## 6.4  Specification Analysis and Validation

### The Scene: Finding What's Missing

The Story Agent has generated 47 user stories across 6 epics for the CommercialEdge Bank onboarding platform. Priya is pleased — the coverage looks comprehensive. But she knows from experience that the most dangerous requirements are not the wrong ones. They are the missing ones. The requirement nobody thought to write. The edge case nobody imagined. The contradiction between two stories that nobody noticed because they were written three weeks apart.

She feeds the entire 47-story set to the AI for specification analysis. Within minutes, the AI returns a report that makes her glad she checked.

Specification analysis is where AI delivers some of its highest value in requirements engineering. The AI can hold all 47 stories in context simultaneously — something no human can do without extensive note-taking — and systematically check for seven categories of quality issues. Let us walk through each category with what the AI actually found in the CommercialEdge Bank requirements:

### What the AI Found: The Quality Report

**Contradictions found: 2**

Story 3.1 specifies that compliance screening must complete within 30 seconds. But Story 3.4 (Enhanced Due Diligence for high-risk clients) requires checking against 12 additional data sources for clients with complex ownership structures. The AI flags: 'The 30-second SLA in Story 3.1 may be unachievable for high-risk clients processed under Story 3.4 when corporate structures exceed 5 layers. Consider tiered SLAs: 30 seconds for standard-risk, 120 seconds for high-risk.'

Story 6.1 states that account opening is fully automated for low-risk clients. Story 6.3 states that all account openings require a final human approval from the Relationship Manager. The AI flags: 'These stories contradict each other. Clarify: is human approval required for ALL account openings, or only for medium/high-risk? If Story 6.1's automation is correct, Story 6.3 should be scoped to medium and high-risk only.'

**Gaps identified: 5**

The AI identified five categories of requirements that are typically present in banking onboarding platforms but missing from the current set: no requirement for session timeout on the client portal (security gap); no requirement for data backup and recovery (operational gap); no accessibility requirements for the client-facing portal (compliance gap — Equality Act 2010); no requirement for what happens when a client's onboarding is abandoned mid-process (workflow gap); and no requirement for rate limiting on the document upload API (security gap).

**Ambiguities flagged: 7**

The AI identified seven instances of vague or multi-interpretable language across the stories. For example: Story 2.1 says 'the system shall validate uploaded documents.' The AI flags: 'Validate against what criteria? Format validity (is it a PDF)? Content completeness (does it contain the required fields)? Authenticity (is it a genuine document, not forged)? This single word 'validate' conceals at least three distinct requirements.'

This is the specification quality funnel in action. The AI took 47 stories as input and produced a structured analysis that would have taken a senior BA three to four days of careful reading. The analysis is not perfect — AI may flag false positives (contradictions that are actually deliberate design choices) or miss domain-specific gaps (requirements that only someone with banking experience would think of). But as a first-pass quality gate before human review, it is transformatively efficient.

| Quality Dimension | AI Detection Strength | What AI Catches | What Humans Must Verify |
|------------------|----------------------|-----------------|-------------------------|
| **Completeness** | ★★★★ | Missing requirement categories (security, accessibility, error handling, ops) | Domain-specific gaps that require industry expertise |
| **Consistency** | ★★★★★ | Contradictions between stories (conflicting SLAs, conflicting workflows) | Intentional design trade-offs that look like contradictions |
| **Ambiguity** | ★★★★★ | Vague terms ('fast,' 'user-friendly,' 'validate'), undefined references | Context-dependent terms that are actually well-understood internally |
| **Verifiability** | ★★★★ | Requirements that cannot be tested ('the system should be intuitive') | Whether proposed metrics are actually measurable in practice |
| **Traceability** | ★★★ | Missing links between requirements and their sources | Whether the source documents are authoritative and current |
| **Feasibility** | ★★ | Obvious impossibilities ('process 1M records in 1 second') | Whether the requirement is achievable given the team's tech stack and skills |

> 📓 **Notebook 6.4 — Specification Analysis and Gap Detection**
>
> This notebook runs the full specification analysis against CommercialEdge Bank's 47 user stories. You'll see the AI detect contradictions, flag ambiguities, and identify missing requirement categories. The notebook also demonstrates AI-generated traceability — linking each requirement back to its stakeholder source and forward to its test coverage. Modify the input stories to analyse your own requirements.

---

## 6.5  Estimation and Planning

### The Scene: How Long Will This Take?

Sprint planning is Thursday. The team has 47 stories to estimate. In a traditional session, they would spend 3–4 hours in Planning Poker, discussing each story one by one, debating whether the sanctions screening integration is a 5 or an 8. With 47 stories, that's at least two sessions.

This time, the AI has done preparatory work. Before the session, it has analysed each story, found 3 analogous completed stories from the team's Jira history, and produced an initial estimate with a confidence range and a rationale. The team doesn't start from zero — they start from an informed position.

Software estimation is notoriously unreliable. The Standish Group reports that 66 percent of software projects experience cost overruns, with the average overrun at 189 percent of the original estimate. AI offers a genuinely useful improvement — not by producing magical accurate estimates, but by providing structured, evidence-based starting points that make the team's estimation conversations faster and better informed.

### The AI-Augmented Estimation Process

The most effective approach combines AI analysis with human judgment. AI provides the data; the team provides the context. Here is how it works for CommercialEdge Bank:

**Before the session:** the AI analyses each story and produces a pre-analysis card. For the sanctions screening story (Story 3.1), the AI retrieves three analogous completed stories from the team's history — all involving third-party API integrations with sensitive compliance data. Historical actuals: 5, 8, and 8 story points. The AI suggests: 'Likely 5–8 points. Primary uncertainty: World-Check API integration complexity and rate limiting behaviour. Secondary uncertainty: fuzzy matching logic for non-Latin character sets.'

**During the session:** the product owner presents the story. The AI's pre-analysis is displayed as reference — not as authority. The team discusses. A backend developer notes that the sanctions API's rate limiting documentation is incomplete, adding uncertainty. A QA engineer points out that testing fuzzy matching across character sets will require synthetic test data from the Data Agent (Chapter 8). The team votes: 8 points.

**After the session:** the AI records the team's estimate alongside the historical analogies and its own suggestion. Over time, this builds a calibration dataset: how accurate were the AI's initial suggestions compared to the team's final estimates and actual effort? This feedback loop makes the AI's suggestions more accurate with each sprint.

> ⚠️ **The Estimation Trap: Beware False Precision**
>
> AI estimation is most dangerous when it appears confident. An AI that says 'this is a 5-point story' with no uncertainty is less trustworthy than one that says 'this is likely 3–8 points; the main uncertainty is the third-party API integration.' Always demand ranges and rationale, not point estimates. Never use AI estimates as final estimates. They are inputs to human judgment, not substitutes for it.

> 📓 **Notebook 6.5 — AI-Assisted Estimation and Sprint Planning**
>
> This notebook implements the AI-augmented estimation process for CommercialEdge Bank. You'll see the AI analyse stories, retrieve historical analogies, generate confidence ranges, and produce a sprint capacity plan with risk factors. The notebook also runs a Monte Carlo simulation showing the probability distribution of sprint completion outcomes.

---

## 6.6  Backlog Refinement with AI

### The Scene: 47 Stories, Which Ones First?

Priya now has 47 validated, estimated user stories. But the team can only deliver approximately 30 story points per sprint. The MVP must cover onboarding stages 1 through 6. Post-MVP covers stages 7 and 8. She needs to prioritise the backlog, map dependencies, identify the stories that must come first, and produce a sprint plan.

Manually, this is a half-day workshop with sticky notes on a whiteboard. With AI, it takes an hour of focused review.

### Epic Decomposition

The Epic Agent decomposes the CommercialEdge Bank onboarding platform into six epics aligned with the onboarding stages. Each epic is classified as Must-Have (MVP), Should-Have, or Nice-to-Have, and dependencies between epics are explicitly mapped:

| Epic | Onboarding Stages | Stories | Points | Priority | Dependencies |
|------|-------------------|---------|--------|----------|-------------|
| 1. Client Intake & KYC | Stages 01–02 | 8 stories | 34 pts | Must-Have (MVP) | None — start here |
| 2. Compliance Screening | Stage 03 | 6 stories | 38 pts | Must-Have (MVP) | Epic 1 (KYC data feeds screening) |
| 3. Due Diligence & Review | Stages 04–05 | 7 stories | 28 pts | Must-Have (MVP) | Epic 2 (screening results inform DD) |
| 4. Account Opening | Stage 06 | 5 stories | 22 pts | Must-Have (MVP) | Epic 3 (DD approval gates opening) |
| 5. Document Issuance | Stage 07 | 4 stories | 16 pts | Should-Have | Epic 4 (account must exist) |
| 6. Handover & Activation | Stage 08 | 3 stories | 12 pts | Should-Have | Epic 5 (documents must be issued) |

### WSJF Prioritisation

Within each epic, stories are prioritised using Weighted Shortest Job First (WSJF) from the Scaled Agile Framework. The AI scores each story across three dimensions (business value, time criticality, risk reduction) and divides by job size to produce a priority ranking. Let us see how this works for three stories from the Compliance Screening epic:

| Story | Business Value | Time Criticality | Risk Reduction | Job Size | WSJF Score | Rank |
|-------|---------------|-----------------|----------------|----------|-----------|------|
| 3.1 Base sanctions screening | 9 (core compliance) | 9 (regulatory deadline) | 9 (blocks all onboarding) | 5 | 5.4 | 1st |
| 3.2 Fuzzy match escalation | 7 (accuracy improvement) | 6 (can ship basic first) | 8 (false negatives are dangerous) | 3 | 7.0 | 2nd |
| 3.3 Re-screening on list update | 8 (regulatory requirement) | 5 (quarterly list updates) | 7 (compliance gap without it) | 5 | 4.0 | 3rd |

Notice that Story 3.2 (Fuzzy match escalation) ranks second despite having lower business value than Story 3.1, because its smaller job size gives it a higher WSJF score. This is WSJF's strength: it prioritises value delivered per unit of effort, not just absolute value. The AI calculates these scores consistently across all 47 stories, giving Priya a defensible, data-informed priority ranking that she can review and adjust based on business judgment.

> 📓 **Notebook 6.6 — Backlog Prioritisation and Dependency Mapping**
>
> This notebook implements WSJF scoring, epic decomposition, and dependency mapping for the full CommercialEdge Bank backlog. You'll see the AI score all 47 stories, generate a visual dependency graph, detect hidden dependencies between stories, and produce a sprint allocation plan across 5 MVP sprints.

---

## 6.7  The Tools Landscape

The tooling landscape for AI-assisted requirements engineering has matured rapidly. Rather than providing an exhaustive product review — which would date within months — this section maps the tool categories to the pipeline stages covered in this chapter.

### The Spec-Driven Development Paradigm

The most significant shift in requirements tooling is the emergence of spec-driven development — the idea that specifications are not documentation artifacts but executable contracts that bridge requirements to code. AWS Kiro (covered in depth in Chapter 5) and GitHub Spec Kit represent this paradigm. The key insight for requirements teams: these tools make the specification the source of truth, not the prompt. Code derives from specs, not from ad-hoc natural language instructions. This aligns perfectly with everything discussed in this chapter: structured requirements (EARS) feeding structured specs feeding structured code.

### Tools by Pipeline Stage

| Pipeline Stage | Tool Category | What They Do |
|---------------|---------------|--------------|
| Stakeholder discovery & elicitation (§6.2) | Meeting AI (Otter.ai, Fireflies.ai, Copilot for Teams) | Transcribe, summarise, extract requirements from meetings |
| Requirements documentation (§6.2) | AI documentation (Notion AI, Confluence AI) | Draft PRDs, structure requirements, summarise feedback |
| User story generation (§6.3) | General-purpose LLMs + spec-driven tools | Generate stories from descriptions or specs; CPFC pattern |
| Specification analysis (§6.4) | Code-aware AI (Kiro, Copilot Workspace) | Analyse specs against codebase, identify gaps |
| Estimation & planning (§6.5) | AI project management (Jira AI, ZenHub AI) | Story point prediction, velocity forecasting, capacity planning |
| Backlog management (§6.6) | AI-native PM (Linear AI, Shortcut AI, Jira AI) | Duplicate detection, prioritisation, epic decomposition |

### The Convergence Trend

The most important trend to watch is convergence: tools that historically served only developers (IDEs, code assistants) are moving upstream into requirements and planning, while tools that served only project managers (Jira, Linear) are adding AI capabilities that touch code. The boundary between "requirements phase" and "development phase" is dissolving. Specs-as-code tools like Kiro and Copilot Workspace make requirements living artifacts that evolve with the codebase — exactly what standards like IEEE 830 always envisioned, but now achievable through AI.

> 💡 **Tool Selection: What Matters Most for Enterprise Adoption**
>
> Don't choose tools based on feature lists alone. The four criteria that matter most for enterprise adoption:
>
> 1. **Data residency and privacy** — Where does your requirements data go? Can you use a private LLM deployment? For CommercialEdge Bank, unreleased product plans and regulatory strategy are highly confidential.
> 2. **Integration with existing workflows** — Does the tool connect to your Jira/Azure DevOps/GitHub ecosystem?
> 3. **Auditability** — Can you trace AI-generated artifacts back to their inputs for compliance? This is a regulatory requirement, not a nice-to-have.
> 4. **Team adoption** — Will BAs, POs, and developers actually use it? The best tool is the one your team will consistently apply.

---

## 6.8  Running Use Case: The CommercialEdge Bank Requirements Package

Let us consolidate everything produced in this chapter into the complete requirements package that Chapter 7 (AI-Powered Design & Architecture) will consume. This packaging step mirrors real-world practice: the output of requirements engineering is not individual stories but a coherent, validated, prioritised collection of artifacts.

### What This Chapter Produced

| Artifact | Content | Produced By | Feeds Into |
|----------|---------|-------------|-----------|
| 47 user stories | Across 6 epics, covering all 8 onboarding stages. Each with EARS acceptance criteria, edge cases, NFRs, and complexity estimates. | Story Agent + human review | Ch 7 (Architecture), Ch 9 (Coding), Ch 11 (Testing) |
| Specification analysis report | 2 contradictions resolved, 5 gaps filled, 7 ambiguities clarified. All issues traced to resolution. | AI specification analysis + Sarah/Elena/David review | Ch 7 (informs architectural constraints) |
| Traceability matrix | Every story linked to: source requirement, stakeholder source, regulatory reference. Forward links to design components (populated in Ch 7). | AI-generated, human-validated | Ch 7 (Design), Ch 11 (Testing), Ch 18 (Governance) |
| Estimation baseline | All 47 stories estimated with confidence ranges. Sprint velocity: 30 pts/sprint. MVP: 4 sprints (Epics 1–4). Post-MVP: 2 sprints (Epics 5–6). | AI-assisted estimation + team Planning Poker | Ch 7 (sprint allocation), Ch 12 (release planning) |
| Prioritised backlog | WSJF-scored, dependency-mapped, sprint-allocated. MVP stories sequenced for implementation. | Epic Agent + AI WSJF scoring + Priya's business judgment | Ch 7 (Architecture Agent consumes for design) |
| Stakeholder sign-off record | Sarah (compliance stories), Elena (risk stories), David (client-facing stories), Raj (operations stories) — all reviewed and approved. | Human sign-off (non-delegable) | Ch 18 (Governance audit trail) |

### The Handoff to Chapter 7

The Architecture Agent (Chapter 7) will consume these artifacts to generate the system design. Specifically, it will use the 47 user stories to identify the microservices boundaries (which stories cluster into which services), the acceptance criteria to define API contracts between services, the non-functional requirements to inform infrastructure decisions (the 30-second screening SLA drives the choice of synchronous vs. asynchronous architecture for the compliance screening service), and the dependency map to sequence the implementation plan.

This is the artifact chain introduced in Chapter 1: the PDLC's output (Chapter 5) becomes the requirements engineering input (this chapter), which produces the architecture input (Chapter 7), which produces the data engineering input (Chapter 8), and so on through the lifecycle. The chain is unbroken because each chapter explicitly declares what it consumes and what it produces.

> 📓 **Notebook 6.7 — End-to-End Pipeline: Spec to Sprint-Ready Backlog**
>
> The capstone notebook for this chapter runs the complete pipeline end-to-end: it takes the Chapter 5 spec artifacts as input, runs requirements extraction, generates user stories, performs specification analysis, produces estimates, and outputs a prioritised, sprint-allocated backlog for CommercialEdge Bank. This is the notebook to run if you want to see the full journey in one execution.

---

## Governance Considerations

Requirements engineering is where AI governance is most critical. A hallucinated requirement that survives to production can be 100 times more expensive to fix than one caught during elicitation. The risks specific to this phase, and their mitigations, are summarised below:

| Risk | Description | Mitigation |
|------|------------|-----------|
| **Hallucinated requirements** | AI generates plausible-sounding requirements that don't reflect actual stakeholder needs or regulatory rules | Every AI-generated requirement must trace to a stakeholder source via the traceability matrix. Domain experts (Sarah, Elena, David) validate their respective areas. |
| **Bias amplification** | AI trained on historical data may perpetuate biases (e.g., accessibility overlooked if prior projects ignored it) | Use AI gap analysis (§6.4) to explicitly check for missing categories: accessibility, internationalisation, compliance. |
| **Confidentiality exposure** | Sensitive business requirements, competitive strategy, and unreleased plans fed to LLMs | Use enterprise-grade LLM deployments with data retention guarantees. Never paste confidential requirements into public AI tools. |
| **Over-reliance on AI prioritisation** | Teams defer to AI-generated WSJF scores without applying business judgment | AI scores are inputs to human decisions. Final prioritisation involves the Product Owner and stakeholders. |
| **False confidence in completeness** | AI produces well-formatted, comprehensive-looking specs that mask gaps | Always run specification analysis (§6.4) as a second pass on AI-generated requirements. |

> 📊 **Figure 1.11: The Agentic Product Development Lifecycle** — In the Agentic PDLC architecture, the Governance Agent monitors this entire pipeline in parallel — validating that every AI-generated requirement traces to a stakeholder source, flagging compliance gaps in real-time, and ensuring regulatory requirements are not hallucinated or misinterpreted. Chapter 18 covers the Governance Agent's full capability in detail.

---

## Key Takeaways

1. **Requirements are where AI has the highest leverage in the PDLC.** A defect caught in requirements costs 100x less than one caught in production. AI that improves requirements quality has outsized ROI.

2. **Structured prompting transforms output quality.** EARS notation, CPFC pattern, and INVEST scoring produce 40–60% higher quality than free-form prompting. Give AI a grammar, not just a question.

3. **AI excels at specification analysis.** Gap detection, ambiguity identification, and consistency checking are AI's strongest requirements capabilities. Use AI as your first-pass quality gate before human review.

4. **AI estimation should augment, not replace, human judgment.** The best approach: AI provides historical analogies and confidence ranges; the team discusses and decides. Never accept AI estimates uncritically.

5. **AI is a breadth tool for backlog management.** Humans deeply analyse 20–30 items per session. AI scans 500 items in minutes. Use AI for duplicate detection, dependency mapping, and gap analysis; use humans for value judgment.

6. **The human validation loop is non-negotiable.** Every AI-generated requirement must be traced to a stakeholder source and validated by the relevant domain expert. For regulated industries, this is a compliance requirement, not a best practice.

7. **This chapter's outputs feed directly into Chapter 7.** 47 user stories, a validated traceability matrix, and a prioritised backlog become the Architecture Agent's primary input for system design.

---

## Further Reading

- Mavin, A. et al., "Easy Approach to Requirements Syntax (EARS)," *IEEE RE '09* (2009). The foundational paper on structured requirements notation that underpins AI-generated requirements throughout this chapter.
- Lucassen, G. et al., "Improving Agile Requirements: The Quality User Story Framework and Tool," *Requirements Engineering* 21(3) (2016). The INVEST-based quality scoring framework adapted for AI evaluation in this chapter.
- Standish Group, *CHAOS Report 2024: Decision Latency Theory*, standishgroup.com (2024). The definitive industry data on requirements-driven project failure rates.
- Berry, D.M. et al., "The Role of Ambiguity in Requirements Engineering," *IEEE RE '03* (2003). Foundational taxonomy of ambiguity types in natural-language requirements.
- Femmer, H. et al., "Rapid Quality Assurance with Requirements Smells," *JSS* 123 (2017). Automated detection of requirements quality issues — the precursor to AI-driven specification analysis.
- Choetkiertikul, M. et al., "A Deep Learning Model for Estimating Story Points," *IEEE TSE* 45(7) (2019). Research on AI-based estimation from user story text.
- Jørgensen, M., "A Review of Studies on Expert Estimation of Software Development Effort," *JSS* 70(1–2) (2004). The meta-analysis that demonstrates estimation unreliability and the need for structured approaches.
- Leffingwell, D., *SAFe 6.0 Reference Guide*, Scaled Agile Press (2024). The WSJF prioritisation framework used in this chapter's backlog management section.
- AWS Kiro, *Spec-Driven Development Documentation*, kiro.dev (2025–2026). The spec-driven development paradigm that bridges requirements to code.
- GitHub, *Copilot Workspace: From Issue to Code*, githubnext.com (2025). The issue-to-implementation pipeline that makes requirements living artifacts.
