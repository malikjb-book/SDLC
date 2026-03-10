# Appendix C: Prompt Library

A collection of ready-to-use prompts organized by SDLC phase. See the `prompts/` directory for the full, structured prompt library.

## Requirements & Planning

```
Analyze the following requirements document and identify:
1. Ambiguous requirements
2. Missing non-functional requirements
3. Conflicting requirements
4. Suggested acceptance criteria for each requirement

[Paste requirements here]
```

## Design & Architecture

```
Given the following requirements, suggest three architecture options with trade-offs:
- Requirements: [describe requirements]
- Constraints: [describe constraints]
- Scale: [expected scale]

For each option, provide: architecture style, components, pros, cons, and when to choose it.
```

## Coding

```
You are a senior [language] developer. Implement the following:
- Feature: [describe feature]
- Existing code context: [paste relevant code]
- Requirements: [list requirements]
- Follow these patterns: [describe patterns]

Include error handling, logging, and unit tests.
```

## Testing

```
Generate comprehensive test cases for the following function:
- Function: [paste function]
- Include: unit tests, edge cases, error cases, boundary values
- Framework: [e.g., pytest, Jest]
- Include both positive and negative test scenarios
```

## DevOps

```
Review this CI/CD pipeline configuration and suggest improvements for:
1. Build time optimization
2. Security hardening
3. Reliability improvements
4. Cost optimization

[Paste pipeline config]
```

*TODO: Expand with more prompts as chapters are written. See `prompts/` for the full library.*
