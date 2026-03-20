**CHAPTER 5**

**AI-Powered Product Development Lifecycle**

*The most significant gains from AI in software development may not come
from writing code faster. They come from compressing the upstream
journey — from market insight to executable specification — so that
engineering teams build the right thing, not just build things right.*

**Overview**

The previous chapters established the foundations of the Software
Development Lifecycle and surveyed the AI tools reshaping software
engineering. This chapter steps back to address a question that precedes
the SDLC entirely: how do organisations decide *what* to build, and how
does AI transform that decision-making process?

The Product Development Lifecycle (PDLC) is the broader framework within
which the SDLC operates. Where the SDLC concerns itself with the
engineering journey from requirements to deployment, the PDLC
encompasses the full arc of product creation: discovering market
opportunities, validating the viability of ideas, building and launching
the product, and iterating based on real-world feedback. The SDLC is, in
effect, the “Build” phase of the PDLC — critically important, but only
one part of a larger whole.

This distinction matters enormously in the context of AI transformation.
McKinsey’s 2025 survey of nearly 300 publicly traded companies found
that the highest-performing AI-driven software organisations — those
achieving 16 to 30 percent improvements in productivity, time to market,
and customer experience, and 31 to 45 percent improvements in software
quality — distinguished themselves not by using AI only for coding, but
by embedding it across the entire PDLC. Top performers were six to seven
times more likely than their peers to have scaled AI to four or more use
cases spanning design, coding, testing, deployment, and adoption
tracking. Most books on AI in software development focus exclusively on
the Build phase. This chapter fills the upstream gap.

**Learning Objectives**

By the end of this chapter, you will be able to:

1.  Distinguish the PDLC from the SDLC and explain why AI’s
    highest-leverage transformation opportunities often sit upstream of
    engineering.

2.  Describe McKinsey/QuantumBlack’s three-phase PDLC model (Discovery,
    Viability, Build) and articulate how AI reshapes each phase.

3.  Explain spec-driven development methodology and demonstrate how
    tools like Kiro bridge the gap between product intent and
    engineering execution.

4.  Analyse how the Product Manager role evolves in an AI-augmented
    PDLC, including the convergence of PM, PMM, and UX responsibilities.

5.  Apply PDLC concepts to the CommercialEdge Bank running use case,
    producing spec artifacts that serve as input for subsequent SDLC
    chapters.

**5.1 SDLC vs. PDLC: Why the Distinction Matters**

The terms SDLC and PDLC are sometimes used interchangeably in industry
discourse, but they describe fundamentally different scopes.
Understanding this distinction is a prerequisite for grasping where AI
can create the most value.

**Defining the PDLC**

The Product Development Lifecycle, as articulated in McKinsey’s research
on AI-enabled software development, consists of three primary phases.
The first is **Discovery**: identifying market opportunities through
customer research, competitive analysis, and trend synthesis. The second
is **Viability**: testing whether ideas can succeed through prototyping,
user testing, business case development, and technical feasibility
assessment. The third is **Build**: engineering the product through
requirements specification, design, coding, testing, and deployment —
which is the territory of the SDLC.

Traditionally, these phases were sequential and siloed. Discovery was
owned by product strategy and marketing. Viability involved product
management and UX research. Build was the domain of engineering.
Handoffs between these phases were a chronic source of information loss,
misalignment, and delay. A product manager might spend weeks
synthesising customer research into a product requirements document,
only to discover during development that critical assumptions were
flawed.

**The SDLC as a Subset**

Every software engineering methodology — Waterfall, Agile, DevOps,
DevSecOps — operates within the Build phase of the PDLC. Agile’s
iterative sprints, continuous integration pipelines, and automated
testing all address how software is constructed, verified, and deployed.
They are essential, but they do not address the upstream questions: Are
we building the right product? For the right market? Solving the right
problem? These are PDLC questions.

This distinction has practical consequences. An engineering team can
execute flawlessly — clean architecture, comprehensive test coverage,
zero-defect deployment — and still deliver a product that no one wants,
because the discovery and viability work was inadequate. McKinsey’s
research across hundreds of companies confirms that AI’s impact is
maximised when it is applied holistically across the PDLC, not confined
to the Build phase alone.

**Why Most AI-in-Development Books Get This Wrong**

The overwhelming majority of literature on AI in software development
focuses on coding assistance, automated testing, and CI/CD optimisation.
These are valuable topics — and they occupy Chapters 6 through 12 of
this book. But by starting the AI conversation at the requirements
phase, they implicitly assume that the right product has already been
identified and validated. In reality, McKinsey’s November 2025 research
found that nearly two-thirds of top-performing organisations had scaled
AI across four or more PDLC use cases, compared with just 10 percent of
bottom performers. The differentiator was not AI adoption in coding. It
was AI adoption across the entire lifecycle, including the upstream
phases that determine what gets built.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Key Insight</strong></p>
<p>Top AI performers are 6–7x more likely than peers to scale AI to 4+
use cases across the PDLC. Nearly two-thirds of leaders report this
level of scale, versus just 10% of bottom performers. The performance
gap is 15 percentage points across productivity, quality, time to
market, and customer experience. (McKinsey, November 2025)</p></td>
</tr>
</tbody>
</table>

**5.2 AI in Discovery and Viability**

The upstream phases of the PDLC — Discovery and Viability — have
historically been the most time-consuming, resource-intensive, and
subjective stages of product development. AI is compressing both phases
and, critically, blurring the boundary between them.

**Transforming Discovery**

Traditional discovery involves weeks of manual effort: conducting
customer interviews, synthesising market research, analysing support
tickets, reviewing competitive offerings, and interpreting usage
telemetry. The output is typically a set of opportunity hypotheses that
are debated, prioritised, and eventually funnelled into the viability
phase.

AI transforms this process in three fundamental ways. First, it can
synthesise vastly larger volumes of data — customer feedback, social
media sentiment, support tickets, product telemetry, and competitive
intelligence — in a fraction of the time. What previously took a product
team weeks of manual analysis can now be accomplished in hours. Second,
AI can generate multiple competing hypotheses from the same data set,
reducing the risk of confirmation bias and the influence of what
McKinsey terms “HiPPO bias” — the Highest-Paid Person’s Opinion
dominating prioritisation decisions. Third, AI can continuously monitor
signals across these data sources, enabling discovery to become an
ongoing process rather than a periodic exercise.

McKinsey’s research found that gen AI tools have almost twice as much
positive impact on content-heavy tasks — such as synthesising
information, creating content, and brainstorming — as on content-light
tasks like data visualisation. Discovery is overwhelmingly
content-heavy, which makes it one of the highest-leverage areas for AI
application.

**Accelerating Viability**

Viability assessment has traditionally been the bottleneck of the PDLC.
Prototyping required significant design and engineering resources. A/B
testing demanded infrastructure and sufficient user traffic. Business
case development involved financial modelling and stakeholder alignment.
The cost and time required for each experiment necessarily limited the
number of ideas that could be tested.

AI fundamentally changes this economics. Rapid prototyping with AI tools
allows product teams to move from concept to functional prototype in
hours rather than weeks. Reddit’s CPO Pali Bhat has described how AI
enables teams to “dream up an idea one day and have a functional
prototype the next.” Automated A/B testing frameworks can evaluate
multiple hypotheses simultaneously. AI-generated market research
documents, press releases, and product one-pagers can accelerate the
collateral needed for stakeholder buy-in.

McKinsey’s PM study of 40 product managers found that those using gen AI
tools completed content-heavy PDLC tasks approximately 40 percent faster
than those working without AI. This acceleration translated to a roughly
5 percent reduction in overall time to market across a six-month PDLC.
While 5 percent may appear modest, it reflects the current state of
adoption. As AI tools mature and organisations rewire their processes to
take full advantage, McKinsey projects that PDLC times could compress
from months to weeks or even days.

**Blurring the Boundary**

Perhaps the most consequential shift is the blurring of the traditional
boundary between Discovery and Viability. In the pre-AI PDLC, these were
necessarily sequential: you discovered opportunities, then you tested
viability. The cost and time required for viability testing meant you
had to be relatively certain about an opportunity before committing
resources to validate it.

AI eliminates this constraint. When prototyping takes hours instead of
weeks, and when AI can generate and test multiple hypotheses
simultaneously, Discovery and Viability become parallel, iterative
processes. A product team can identify an opportunity, prototype a
solution, test it with users, and refine the hypothesis — all within a
single sprint. This shift is analogous to how Agile compressed the Build
phase from sequential waterfall stages into iterative sprints, and it
has similar implications for speed, quality, and adaptability.

**Traditional vs. AI-Enabled PDLC**

| **PDLC Phase** | **Traditional Approach** | **AI-Enabled Approach** |
|----|----|----|
| Discovery | Manual market research, stakeholder interviews, competitive analysis. Weeks of synthesis before hypotheses emerge. | AI synthesises customer research, market data, support tickets, and social sentiment in hours. Multiple hypotheses generated and ranked by evidence strength. |
| Viability | Sequential: plan first, then prototype. High cost per experiment limits the number of ideas tested. HiPPO bias in prioritisation. | Parallel: AI enables rapid prototyping and automated A/B testing simultaneously. More experiments at lower cost. Data-driven prioritisation reduces subjective bias. |
| Build | Linear handoffs: PM writes PRD, designer creates mockups, engineer implements. Multiple translation losses. Compliance bolted on late. | Spec-driven: AI transforms PM intent into executable specs. Engineers collaborate with coding agents. Quality, compliance, and accessibility embedded from the start. |
| Launch & Iterate | Post-launch feedback collected manually. Slow iteration cycles. Value realisation measured months later. | AI-integrated telemetry provides real-time adoption signals. Continuous feedback loops. Outcome-based metrics from day one. |

**5.3 Spec-Driven Development: Bridging PDLC to SDLC**

If AI is transforming how organisations discover opportunities and
validate ideas, the next question is: how does that upstream work
translate into engineering execution? This is the critical handoff point
between the PDLC and the SDLC, and it is where a new methodology —
spec-driven development — is emerging as a transformative practice.

**The Problem with the Traditional Handoff**

In traditional product development, the handoff from product management
to engineering is one of the most error-prone transitions in the entire
lifecycle. A product manager synthesises customer research, stakeholder
input, and business strategy into a product requirements document (PRD)
or a set of user stories. This document is then interpreted by
engineers, who translate it into technical specifications, system
design, and implementation plans. Each translation step introduces the
possibility of misunderstanding, lost context, and implicit assumptions.

The problem is compounded in the age of AI-assisted coding. When
engineering teams use AI coding agents to implement features, the
quality of the output is directly proportional to the quality of the
input specification. An ambiguous or incomplete requirement that a
senior engineer might resolve through experience and intuition becomes a
source of hallucinated or incorrect behaviour when processed by an AI
agent. The garbage-in, garbage-out principle applies with particular
force in AI-assisted development.

**What Is Spec-Driven Development?**

Spec-driven development (SDD) is a methodology in which specifications
become executable, first-class artifacts that directly drive
implementation, rather than serving merely as documentation that quickly
becomes outdated. The fundamental principles are straightforward.
Specifications are the source of truth: development begins with precise,
machine-understandable specs rather than vague notes or informal
conversations. Specifications are executable: they drive the generation
of implementation plans, task breakdowns, code scaffolding, and tests.
Changes are traceable: modifications to specs ripple through to tasks
and implementations. Drift is minimised: the gap between intent and
execution is systematically reduced.

SDD is explicitly contrasted with what practitioners call “vibe coding”
— the ad-hoc, prompt-driven approach to AI-assisted development in which
a developer describes what they want in natural language and an AI
generates code directly. Vibe coding can be remarkably effective for
simple, self-contained tasks. But for complex, multi-stakeholder systems
— precisely the kind of system our CommercialEdge Bank use case
represents — it breaks down. The AI lacks the accumulated context of
upstream product decisions, compliance requirements, and architectural
constraints that a specification captures.

**Kiro: Spec-Driven Development in Practice**

Kiro, developed by AWS, is the most fully realised implementation of
spec-driven development in the current tool landscape. Launched in 2025
and rapidly adopted for production use by early 2026, Kiro is an agentic
AI that operates as both an IDE and a CLI, designed to take development
teams from prototype to production through structured specification
artifacts.

Kiro’s workflow follows a disciplined five-step progression from
natural-language intent to working code:

| **Step** | **Kiro Artifact** | **Description** |
|----|----|----|
| 1\. Prompt | Natural language input | PM or developer describes the feature in plain English. Kiro interprets intent, constraints, and context. |
| 2\. Requirements | requirements.md | Kiro generates user stories and acceptance criteria in EARS (Easy Approach to Requirements Syntax) notation. Human reviews and iterates. |
| 3\. Design | design.md | Kiro analyses the existing codebase and proposes architecture, system design, data flow diagrams, and tech stack decisions. |
| 4\. Tasks | tasks.md | Kiro creates a sequenced implementation plan with discrete, dependency-ordered tasks. Each task is trackable and executable. |
| 5\. Implement | Code + tests | Kiro’s agent executes tasks, generating code, tests, and documentation. Human reviews at each checkpoint. |

Several aspects of Kiro’s approach merit closer examination. First,
requirements are generated in EARS (Easy Approach to Requirements
Syntax) notation, which provides a structured grammar for expressing
behavioural requirements: “When \[trigger\], the system shall
\[behaviour\]” or “While \[state\], the system shall \[behaviour\].”
This structure makes requirements unambiguous and testable — properties
that both human reviewers and AI agents benefit from.

Second, the design phase analyses the existing codebase before proposing
architecture. This means Kiro’s architectural recommendations are
grounded in the actual state of the system, not an idealised greenfield
assumption. For a project like CommercialEdge Bank’s onboarding
platform, which must integrate with legacy core banking systems, this
contextual awareness is essential.

Third, Kiro supports “steering files” — persistent markdown documents
that encode project conventions, tech stack decisions, API standards,
testing requirements, and security policies. These files provide ambient
context to the AI agent, ensuring that every generated artifact conforms
to organisational standards without requiring the developer to
re-specify them in every prompt.

Fourth, Kiro integrates the Model Context Protocol (MCP), which connects
the agent to external enterprise resources: documentation, databases,
APIs, incident tracking systems, and more. For CommercialEdge Bank, this
would mean connecting Kiro to the bank’s regulatory compliance database,
its core banking API specifications, and its internal architecture
decision records.

**Complementary Frameworks**

Kiro is not the only implementation of spec-driven development
principles. GitHub’s open-source Spec Kit, released in September 2024,
provides a CLI-based framework that implements a four-phase workflow:
Specify (define what and why), Plan (technical design), Tasks
(implementation breakdown), and Implement (execute). Spec Kit is
designed to work with multiple AI coding assistants, including GitHub
Copilot, Claude Code, Gemini CLI, and Cursor, making it a tool-agnostic
complement to Kiro’s integrated approach.

The convergence of these tools around a common pattern — structured
specification as the bridge between product intent and AI-assisted
engineering — signals that spec-driven development is becoming a
foundational practice for the AI era, not merely one vendor’s approach.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>Spec-Driven Development vs. Vibe Coding</strong></p>
<p>Vibe coding: developer prompts AI with informal description → AI
generates code immediately → works for simple tasks, breaks down at
scale. Spec-driven development: structured spec (requirements → design →
tasks) → AI generates code within defined boundaries → traceable,
auditable, scalable for complex systems. For regulated industries like
banking, where auditability and compliance traceability are
non-negotiable, spec-driven development is not optional — it is a
prerequisite.</p></td>
</tr>
</tbody>
</table>

**5.4 The Evolving Role of the Product Manager**

AI’s transformation of the PDLC has profound implications for the
product management profession. The long-standing aspiration for PMs to
operate as “mini-CEOs” — with end-to-end ownership from market insight
to value realisation — is becoming operationally feasible for the first
time.

**Shifting Right: End-to-End Ownership**

In the traditional PDLC, PMs relied on a team of specialised roles to
fulfil essential tasks: product marketing managers for positioning and
collateral, UX designers for prototypes and usability testing, technical
product managers for engineering liaison, and product owners for backlog
management. Each handoff introduced delay and information loss.

AI enables PMs to “shift right” — taking on responsibilities that
previously required specialist support. With AI tools, a PM can
independently synthesise customer research, generate product one-pagers
and pitch decks, create functional prototypes, draft product
requirements documents, and build product backlogs. McKinsey’s study
found that PMs using gen AI completed content-heavy tasks 40 percent
faster and reported doubled job satisfaction. These are not minor
efficiency gains; they represent a fundamental expansion of the PM’s
effective bandwidth.

The implication, as noted by Adobe’s Varun Parmar, is that historically
separate roles — Product Marketing Manager (PMM), Product Owner (PO),
Technical Product Manager (TPM), and even some UX functions — may
converge under a single, AI-augmented product management role. The PM
becomes a true end-to-end owner, capable of running discovery,
prototyping solutions, validating with customers, specifying
requirements, and monitoring post-launch adoption — all with AI support.

**New Skill Requirements**

This expanded role demands new competencies. McKinsey/QuantumBlack’s
research on the gen AI skills revolution identifies several critical
shifts. PMs must develop strong prompt engineering skills to effectively
direct AI tools toward high-quality outputs. They need data literacy to
evaluate AI-generated analyses and recommendations critically. They
require technical fluency — not at the level of a software engineer, but
sufficient to understand architectural trade-offs, evaluate technical
feasibility, and communicate effectively with AI coding agents through
structured specifications.

Perhaps most importantly, PMs need what QuantumBlack terms “trust
calibration” skills — the ability to neither over-trust nor under-trust
AI outputs. McKinsey’s PM study found that output quality was highly
contingent on PM experience: more experienced PMs produced significantly
better results when using AI tools, because they had the domain
knowledge to evaluate and refine AI-generated artifacts. Junior PMs, by
contrast, sometimes accepted suboptimal AI outputs that a more
experienced practitioner would have challenged.

This finding has direct implications for talent strategy. Organisations
cannot simply provide AI tools and expect uniform improvement. They must
invest in structured, role-specific upskilling that builds the judgment
needed to use AI effectively. McKinsey’s research found that 57 percent
of top-performing organisations invested in hands-on workshops and
one-on-one coaching, compared with just 20 percent of bottom performers.
Static documentation and annual training sessions are insufficient.

**From Individual Contributor to Orchestrator**

Looking forward, the PM role is evolving from individual contributor to
orchestrator of AI agents. As Cursor CEO Michael Truell has observed,
individual contributors may increasingly spend part of their time
directing a team of asynchronous AI agents — a new type of work that
demands entirely new skill sets. In this model, the PM does not
personally perform every task but defines intent, sets quality
standards, and reviews AI-generated outputs across the entire PDLC.

For our CommercialEdge Bank use case, this means the product manager
responsible for the onboarding platform would use AI to synthesise
regulatory requirements and customer pain points (Discovery), rapidly
prototype potential workflows and test them with bank relationship
managers (Viability), and generate structured specifications that AI
coding agents can execute (Build). The PM becomes the connective tissue
between business strategy and engineering execution, with AI handling
the mechanical work at every stage.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><p><strong>The AI-Augmented PM: By the Numbers</strong></p>
<p>40% faster completion of content-heavy PDLC tasks (McKinsey PM Study,
2024) • 2x higher job satisfaction when using gen AI tools • ~5%
acceleration in time to market across a 6-month PDLC • 57% of top
performers invest in hands-on AI coaching vs. 20% of bottom performers
(McKinsey, 2025) • 90%+ of surveyed software teams now use AI for core
engineering tasks, saving 6 hours/week on average (McKinsey,
2025)</p></td>
</tr>
</tbody>
</table>

**5.5 Running Use Case: From Product Vision to Spec for CommercialEdge
Bank**

Let us now apply the PDLC concepts introduced in this chapter to our
running use case: the CommercialEdge Bank corporate client onboarding
platform. This section walks through the upstream PDLC journey — from
market insight through spec generation — producing the artifacts that
will feed into the SDLC chapters that follow.

**Discovery: Understanding the Problem Space**

CommercialEdge Bank’s product team begins by using AI to synthesise
multiple data sources: internal metrics showing a 4-week average
onboarding cycle for corporate clients, customer satisfaction surveys
revealing that 35 percent of prospective clients abandon the process
before completion, compliance team reports documenting an average of 2.3
manual touchpoints per compliance check, and competitive intelligence
showing that digital-first competitors offer onboarding experiences
measured in days rather than weeks.

An AI-assisted discovery synthesis produces several key insights. The
primary bottleneck is not any single stage but the cumulative effect of
manual handoffs between stages — particularly between KYC collection
(Stage 02), compliance screening (Stage 03), and transaction due
diligence (Stage 04). The 35 percent drop-off rate is concentrated in
the KYC document collection phase, where corporate clients are asked to
provide documents through email and physical courier. Regulatory
requirements are well-defined and stable, making them suitable for
automated compliance checking. Competitors who have digitised onboarding
report cycle times of 3–5 business days with equivalent compliance
coverage.

**Viability: Testing Hypotheses**

Based on discovery findings, the product team formulates three viability
hypotheses. First, that a digital KYC collection portal with real-time
document validation can reduce the KYC stage from 1–2 days to under 4
hours. Second, that automated compliance screening against sanctions
lists, PEP databases, and adverse media can eliminate manual review for
80 percent of standard-risk applications. Third, that straight-through
processing for low-risk account types (Corporate Current, Cash
Management) can achieve automated approval rates of 80 percent or
higher.

Using AI-assisted rapid prototyping, the team creates a clickable
prototype of the client-facing KYC portal in a single day. This
prototype is tested with five relationship managers and three corporate
clients in structured usability sessions. Feedback reveals that the
document upload experience must support bulk upload of multiple files
per requirement (e.g., three years of financial statements as separate
PDFs) and must provide immediate feedback on document quality and
completeness. These findings are incorporated before any engineering
work begins — a concrete example of how AI-compressed viability testing
prevents costly downstream rework.

**Spec Generation: Bridging to Engineering**

With discovery validated and viability hypotheses tested, the product
team uses spec-driven development principles to generate the artifacts
that will guide engineering execution. In this walkthrough, we
demonstrate the Kiro methodology, though the same principles apply using
GitHub Spec Kit or any structured specification approach.

The following table maps each spec artifact to its CommercialEdge Bank
content and the subsequent chapter where it is consumed:

| **Spec Artifact** | **CommercialEdge Bank Content** | **Feeds Into** |
|----|----|----|
| Discovery Brief | Market analysis of digital onboarding in mid-tier commercial banking. Pain points: 4-week manual cycle, 35% drop-off rate, compliance bottlenecks. Competitive benchmarking against neobank onboarding times (same-day). | Viability hypotheses |
| Viability Hypotheses | H1: Digital KYC collection can reduce Stage 02 from 2 days to 4 hours. H2: Automated compliance screening can eliminate Stage 03 manual review. H3: Straight-through processing can achieve 80%+ auto-approval for low-risk accounts. | Prototype scope |
| Product Vision (PRD) | Transform corporate onboarding from 4-week manual process to 3–5 day digital platform. 8 stages, 6 compliance checks. Account types: Corporate Current, Trade Finance, FCY, Cash Management, Credit Facility. | Kiro spec input |
| requirements.md | User stories for each of the 8 onboarding stages with EARS acceptance criteria. Example: “When a Relationship Manager logs a prospect, the system shall create a case record in the origination system and assign an onboarding case ID within 30 seconds.” | Chapter 6 |
| design.md | Microservices architecture: KYC Service, Compliance Engine, Account Provisioning, Document Issuance. Event-driven integration via message queue. API gateway for client portal. | Chapter 7 |
| tasks.md | 42 implementation tasks across 8 stages, dependency-sequenced. Example: Task 1.1: Implement prospect capture API endpoint. Task 1.2: Build account type selection UI. Task 2.1: Create KYC document upload service. | Chapter 8 |

The critical property of these artifacts is traceability. Every
implementation task in tasks.md traces back to a specific requirement in
requirements.md, which traces back to a user story validated during
viability testing, which traces back to a discovery insight grounded in
data. When a coding agent implements Task 2.1 (Create KYC document
upload service), it does so within the full context of why this feature
exists, what acceptance criteria it must satisfy, and how it fits into
the broader system architecture. This is the operational difference
between spec-driven development and vibe coding at enterprise scale.

**Steering Files for CommercialEdge Bank**

In addition to the core spec artifacts, the product team creates a set
of steering files that encode persistent project context. These include
a product steering file documenting the platform’s purpose, target
users, account types, and success metrics; a technology steering file
specifying the approved tech stack (microservices on cloud
infrastructure, event-driven architecture, specific API standards); a
compliance steering file encoding regulatory requirements for KYC, AML,
and sanctions screening; and a security steering file defining data
encryption standards, access control requirements, and audit logging
specifications.

These steering files persist across the entire development lifecycle,
ensuring that every AI-generated artifact — whether a requirement, a
design document, or a code implementation — conforms to the
organisational and regulatory standards that govern the CommercialEdge
Bank platform. They are the AI-age equivalent of architectural decision
records, but machine-readable and continuously enforced.

**What Happens Next**

The spec artifacts generated in this chapter become the primary inputs
for the SDLC chapters that follow. Chapter 6 (AI-Assisted Requirements &
Planning) will take the requirements.md and expand the user stories with
detailed acceptance criteria, edge cases, and estimation. Chapter 7
(AI-Powered Design & Architecture) will elaborate the design.md into a
full system architecture with service boundaries, data models, and
integration patterns. Chapter 8 (Coding Agents & AI Pair Programming)
will use the tasks.md to demonstrate how AI coding agents implement the
compliance screening service. This continuity mirrors how real
product-to-engineering workflows operate — the PDLC produces the specs,
and the SDLC consumes them.

**Key Takeaways**

- **The PDLC is the broader framework within which the SDLC operates.**
  The SDLC addresses how software is built. The PDLC addresses what gets
  built and why. AI’s highest-leverage impact often comes from
  compressing the upstream Discovery and Viability phases, not just the
  Build phase.

- **Top AI performers embed AI across the entire PDLC.** McKinsey’s 2025
  research shows top performers are 6–7x more likely to scale AI to four
  or more PDLC use cases, driving 16–45 percent improvements in
  productivity, quality, time to market, and customer experience.

- **AI blurs the boundary between Discovery and Viability.** When
  prototyping takes hours instead of weeks, these phases become parallel
  and iterative rather than sequential, enabling more experiments and
  reducing the risk of building the wrong product.

- **Spec-driven development is the critical PDLC-to-SDLC bridge.** Tools
  like Kiro and GitHub Spec Kit transform natural-language product
  intent into structured, executable specifications that AI coding
  agents can consume. For regulated industries, this traceability is not
  optional.

- **The PM role is expanding from specialist to end-to-end
  orchestrator.** AI enables PMs to shift right, absorbing
  responsibilities previously distributed across PMM, PO, TPM, and UX
  roles. This demands new competencies: prompt engineering, trust
  calibration, and technical fluency.

- **This chapter’s spec artifacts become the foundation for subsequent
  chapters.** The CommercialEdge Bank requirements.md, design.md, and
  tasks.md produced here feed directly into Chapters 6–12, mirroring how
  real product-to-engineering workflows operate.

**Further Reading**

1.  McKinsey, *“How an AI-Enabled Software Product Development Life
    Cycle Will Fuel Innovation,”* mckinsey.com (February 2025).
    Foundational article on AI’s five critical shifts for the PDLC,
    including faster time to market, customer value delivery, and PM
    role expansion.

2.  McKinsey/QuantumBlack, *“Unlocking the Value of AI in Software
    Development,”* mckinsey.com (November 2025). Survey of ~300
    companies identifying the two key shifts and three enablers that
    distinguish top AI performers.

3.  McKinsey, *“How Generative AI Could Accelerate Software Product Time
    to Market,”* mckinsey.com (May 2024). The PM study: 40 product
    managers tested across Discovery, Viability, and Build phases with
    varying levels of AI access.

4.  McKinsey/QuantumBlack, *“The Gen AI Skills Revolution: A New Talent
    Strategy,”* mckinsey.com (August 2024). Analysis of how gen AI
    reshapes every PDLC phase and the skill implications for PMs and
    engineers.

5.  QuantumBlack Labs, *“Transforming the Software Development Cycle
    with Generative AI,”* Medium (April 2025). QuantumBlack’s R&D team
    on integrating gen AI into development workflows with practical case
    studies.

6.  AWS / Kiro, *Spec-Driven Development Documentation,* kiro.dev
    (2025–2026). Official documentation for Kiro’s spec-driven
    methodology, including steering files, hooks, and MCP integration.

7.  GitHub, *Spec Kit — Open-Source Spec-Driven Development Framework,*
    github.com (September 2024). CLI and templates for the Specify →
    Plan → Tasks → Implement workflow, compatible with multiple AI
    coding assistants.

8.  Brian Hammons (AWS), *“Spec-Driven Development: Building Better
    Software, Faster with Kiro,”* Medium (January 2026). Practitioner’s
    account of applying spec-driven development on a real project,
    including lessons from an initial vibe-coding failure.

9.  Atal Upadhyay, *“Spec-Driven Development with Kiro on AWS,”*
    WordPress (March 2026). Detailed technical guide covering the
    philosophy, tooling, and hands-on patterns of SDD with Kiro.

10. Vishal Mysore, *“Comprehensive Guide to Spec-Driven Development:
    Kiro, GitHub Spec Kit, and BMAD-METHOD,”* Medium (September 2025).
    Comparative analysis of three SDD frameworks and their design
    philosophies.
