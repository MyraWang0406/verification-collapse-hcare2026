# Human-Centered AI Workflow for Requirements Decision Traceability

This table mirrors the workflow described in the HCARE 2026 position paper. It is provided as a reusable artifact for discussion and future tool prototyping.

The workflow is not intended to automate requirements approval. Its purpose is to make requirements decisions more inspectable by separating AI-assisted summarization from human verification and accountability.

## Workflow table

| Stage | AI support | Human gate |
|---|---|---|
| 1. Context completion | Summarizes sources, business triggers, users, stakeholders, constraints, and missing information. | Product and business stakeholders verify goals, scope boundaries, source relevance, and expected value. |
| 2. Pre-analysis | Identifies affected modules, historical dependencies, data flows, edge cases, and preliminary risks. | Product, engineering, testing, data, and business roles confirm dependencies and risk relevance. |
| 3. Admission decision | Organizes value, urgency, maturity, risk, feasibility, and unresolved assumptions. | Named human roles decide whether to proceed, clarify, reduce, split, postpone, or reject the requirement. Rationale must be recorded. |
| 4. Change control | Compares the baseline requirement with change requests; extracts rationale, affected modules, schedule impact, and release risk. | Major changes require documented human sign-off, especially for payment, settlement, risk, compliance, data, or user-impacting logic. |
| 5. Release validation | Links acceptance criteria, test evidence, monitoring indicators, and known residual risks. | Human reviewers confirm acceptance criteria, release readiness, residual risks, and rollback expectations. |
| 6. Post-hoc review | Summarizes assumptions, changes, release evidence, outcome gaps, user feedback, and lessons learned. | Participants validate the review before it enters organizational memory or is reused in future requirements work. |

## Operational trace artifacts

The workflow turns verification into four inspectable trace artifacts.

| Trace artifact | What it records | Why it matters |
|---|---|---|
| Source anchors | The source materials supporting a requirement claim, such as PRDs, tickets, meeting notes, dashboards, tests, or stakeholder statements. | Prevents AI-generated summaries from floating without evidence. |
| Uncertainty markers | Assumptions, missing evidence, unresolved dependencies, unclear rules, and unverified edge cases. | Prevents uncertainty from being hidden behind fluent AI output. |
| Sign-off records | Who approved a requirement, change, exception, or residual risk, and why. | Distinguishes formal approval from meaningful accountability. |
| Decision-owner fields | The role or person responsible for accepting remaining risk after verification. | Prevents responsibility from diffusing across tools, meetings, and teams. |

## Minimal use case

A team can use this workflow during an AI-assisted requirements decision by asking four questions:

1. What sources support this requirement?
2. What remains uncertain or unverified?
3. Who approved the current version or change?
4. Who owns the residual decision risk?

## Intended use

This workflow can be used as:

- a checklist for AI-assisted requirements review;
- a template for structuring decision records;
- a discussion artifact for expert walkthroughs;
- a starting point for future tool design.

## Boundary

This workflow does not claim to solve requirements engineering automation. It is a lightweight human-centered mechanism for making AI-assisted requirements decisions more inspectable, traceable, and accountable.
