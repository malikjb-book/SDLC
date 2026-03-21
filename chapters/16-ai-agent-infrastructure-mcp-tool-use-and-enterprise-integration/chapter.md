# Chapter 16: AI Agent Infrastructure: MCP, Tool Use & Enterprise Integration

> *This chapter dives into the enterprise context layer that powers every agent in the pipeline — the Model Context Protocol (MCP), tool-use patterns, custom extensions, and secure integrations with corporate systems.*

To understand why the enterprise context layer matters, consider the agentic SDLC architecture from Chapter 1, this time with attention directed to the blue infrastructure bar at the bottom and the connections flowing upward from it. Every agent in the architecture depends on enterprise context — coding standards, architectural guidelines, compliance databases, existing codebases — to produce correct and consistent output. Without the MCP infrastructure layer, each agent would need its own bespoke integration with each data source, creating an N×M integration problem that does not scale.

> 📊 **Figure 16.1: The Enterprise Context Layer — how MCP serves every agent in the SDLC.**
>
> ![Agentic SDLC Architecture — Infrastructure Focus](../../diagrams/agentic-sdlc-v2-infrastructure.png)

The diagram reveals a critical architectural property: the MCP layer is not a convenience — it is the connective tissue that makes the multi-agent architecture functional. The following table maps each MCP server to the agents that consume it and the enterprise system it exposes:

| MCP Server | Enterprise System | Consuming Agents | Purpose |
|------------|------------------|------------------|---------|
| Core Banking API | Mainframe account management | Coding Agent, Release Agent | Expose account creation and enquiry APIs for integration development and deployment verification |
| Compliance DB | Sanctions, PEP, adverse media databases | Data Agent, Architecture Agent, Governance Agent | Provide real-time compliance data for screening logic, architecture constraints, and governance validation |
| Document Store | KYC document repository (object storage + vector DB) | Data Agent, Testing Agent | Enable document processing pipeline development and test data access |
| Regulatory Docs | Compliance requirements, regulatory guidelines | Epic Agent, Story Agent, Governance Agent | Ensure requirements and governance artifacts reflect current regulatory requirements |
| Code Standards | Linting rules, coding conventions, style guides | Coding Agent | Enforce organisational coding standards in AI-generated code |
| Architecture Guidelines | ADRs, design patterns, approved architectures | Architecture Agent, Coding Agent | Ground architectural decisions and code in approved patterns |
| Approved Libraries | Package registry, licence-cleared dependencies | Coding Agent | Restrict AI-generated code to approved and licence-compliant libraries |
| Existing Codebase | Git repositories (monorepo or multi-repo) | Architecture Agent, Coding Agent, Data Agent | Provide full codebase context for architecture analysis, code generation, and data model understanding |

Without this infrastructure layer, the promise of multi-agent SDLC automation cannot be realised at enterprise scale. The agents are only as good as the context they receive, and MCP is the mechanism that delivers that context reliably, securely, and governably.


