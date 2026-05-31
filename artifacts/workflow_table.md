# Human-Centered AI Workflow for Requirements Decision Traceability

This table mirrors the workflow described in the HCARE 2026 position paper. It is provided as a reusable artifact for discussion and future tool prototyping.

| Stage | AI support | Human gate |
|---|---|---|
| 1. Context completion | Summarizes sources, business triggers, users, stakeholders, and constraints; explicitly flags missing fields. | Product and business stakeholders verify goals, scope boundaries, and expected value. |
| 2. Pre-analysis | Identifies affected modules, historical dependencies, data flows, and preliminary risks. | Product, engineering, testing, and business roles confirm dependencies and risk relevance. |
| 3. Admission decision | Organizes value, urgency, maturity, risk, and feasibility evidence; marks unconfirmed assumptions. | Named human roles decide: proceed, clarify, reduce, split, postpone, or reject. Rationale recorded. |
| 4. Change control | Compares baseline with change requests; extracts rationale, affected modules, schedule impact, and release risk. | Major changes require documented sign-off, especially for payment, settlement, risk, or data logic. |
| 5. Release validation | Links acceptance criteria, test evidence, and monitoring indicators; generates preliminary outcome summary. | Human reviewers confirm acceptance criteria, residual risks, and release readiness. |
| 6. Post-hoc review | Summarizes assumptions, changes, release evidence, outcome gaps, and lessons. | Participants validate the review before it enters organizational memory. |

## Operational trace artifacts

The workflow turns verification into four inspectable trace artifacts:

1. **Source anchors**: which PRD, ticket, meeting note, test record, dashboard, or stakeholder statement supports each requirement claim.
2. **Uncertainty markers**: which assumptions, dependencies, edge cases, or business rules remain unverified.
3. **Sign-off records**: which major changes were accepted, by whom, why, and with what schedule or risk implications.
4. **Decision-owner fields**: which human role accepted the residual risk behind the requirement decision.
