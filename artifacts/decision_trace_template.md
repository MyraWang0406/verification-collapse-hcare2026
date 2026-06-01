# Decision Trace Template

This template provides a lightweight structure for recording AI-assisted requirements decisions.

It is designed to preserve four kinds of trace evidence:

1. Source anchors
2. Uncertainty markers
3. Sign-off records
4. Decision-owner fields

The template is not intended to replace existing requirement tools. It can be attached to a PRD, ticket, design review, release record, implementation review, or post-hoc review.

---

## 1. Requirement decision summary

| Field | Content |
|---|---|
| Requirement / decision name |  |
| Decision ID |  |
| Date |  |
| Product / system area |  |
| Decision status | proposed / accepted / rejected / postponed / changed / implemented / released |
| Short description |  |
| AI tool used |  |
| Human decision owner |  |
| Review participants |  |

---

## 2. Source anchors

List the source materials used to support the requirement claim.

| Source type | Source description | Link / ID | Checked by | Status |
|---|---|---|---|---|
| PRD / document |  |  |  | unchecked |
| Meeting note |  |  |  | unchecked |
| Ticket / issue |  |  |  | unchecked |
| Data / dashboard |  |  |  | unchecked |
| Test / QA record |  |  |  | unchecked |
| Repository / commit / PR |  |  |  | unchecked |
| Stakeholder statement |  |  |  | unchecked |
| User feedback |  |  |  | unchecked |

---

## 3. Requirement claim

Write the requirement claim in one or two sentences.

| Field | Content |
|---|---|
| Requirement claim |  |
| Claimed user / business value |  |
| Target users or stakeholders |  |
| Expected outcome |  |
| Scope boundary |  |

---

## 4. Prompt and context quality

Use this section when AI output is used to generate analysis, specifications, code, or implementation plans.

| Check item | Evidence | Status |
|---|---|---|
| Prompt includes concrete user task, not only background or motivation. |  | yes / no / unclear |
| Prompt includes acceptance criteria or expected output. |  | yes / no / unclear |
| Prompt includes historical code / repository context when implementation is requested. |  | yes / no / unclear |
| Prompt separates business rationale from implementation instruction. |  | yes / no / unclear |
| Prompt separates emotional context from actionable task. |  | yes / no / unclear |

---

## 5. Role and responsibility context

Use this section when multiple people or roles interact with AI outputs.

| Role / actor | Responsibility in this decision | What AI should do for this role | What AI should not do for this role | Confirmed by |
|---|---|---|---|---|
| Product / PM |  |  |  |  |
| Operations / business |  |  |  |  |
| Engineering |  |  |  |  |
| QA / testing |  |  |  |  |
| Manager / approver |  |  |  |  |

---

## 6. Key assumptions

Record assumptions that influence the decision.

| Assumption | Evidence source | Confidence | Needs verification? | Owner |
|---|---|---|---|---|
|  |  | low / medium / high | yes / no |  |
|  |  | low / medium / high | yes / no |  |
|  |  | low / medium / high | yes / no |  |

---

## 7. Uncertainty markers

Record what remains unclear, risky, or under-verified.

| Uncertainty | Why it matters | Current evidence | Next verification step | Owner |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

## 8. Affected systems and dependencies

| System / module | Expected impact | Dependency owner | Risk level | Notes |
|---|---|---|---|---|
|  |  |  | low / medium / high |  |
|  |  |  | low / medium / high |  |
|  |  |  | low / medium / high |  |

---

## 9. Implementation evidence and reproduction check

Use this section when AI claims that code, configuration, workflow, or data-processing logic has been implemented.

| Check item | Evidence link / command | Checked by | Status |
|---|---|---|---|
| Repository branch / commit / PR exists. |  |  | not checked / passed / failed |
| Claimed files or modules changed. |  |  | not checked / passed / failed |
| Installation or build command runs. |  |  | not checked / passed / failed |
| Core workflow can be reproduced locally or in CI. |  |  | not checked / passed / failed |
| Output matches the requirement or acceptance criteria. |  |  | not checked / passed / failed |
| Known limitations are documented. |  |  | not checked / passed / failed |

---

## 10. Alternatives considered

| Alternative | Reason considered | Reason accepted or rejected | Evidence |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |

---

## 11. Sign-off record

| Decision item | Approved by | Role | Date | Rationale | Conditions |
|---|---|---|---|---|---|
| Initial admission |  |  |  |  |  |
| Major change |  |  |  |  |  |
| Implementation claim |  |  |  |  |  |
| Release readiness |  |  |  |  |  |
| Residual risk acceptance |  |  |  |  |  |

---

## 12. Change-control record

Use this section when the requirement changes after initial admission.

| Change | Reason | Requested by | Approved by | Risk introduced | Schedule impact |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |

---

## 13. Release validation

| Acceptance criterion | Evidence | Verified by | Status |
|---|---|---|---|
|  |  |  | not checked / passed / failed |
|  |  |  | not checked / passed / failed |
|  |  |  | not checked / passed / failed |

---

## 14. Post-release review

| Field | Content |
|---|---|
| Actual outcome |  |
| Unexpected issue |  |
| User / stakeholder feedback |  |
| Gap between expectation and outcome |  |
| Lessons learned |  |
| Should this decision pattern be reused? | yes / no / uncertain |
| Follow-up owner |  |

---

## 15. Verification checklist

Before closing the decision trace, check the following items.

| Check item | Status |
|---|---|
| Source anchors are recorded. | yes / no |
| Unverified assumptions are marked. | yes / no |
| Role and responsibility boundaries are confirmed. | yes / no |
| Prompt and context quality are checked. | yes / no |
| Major changes have sign-off records. | yes / no |
| A human decision owner is named. | yes / no |
| Implementation claims are backed by repository, test, or reproduction evidence. | yes / no / not applicable |
| Residual risks are explicitly accepted or escalated. | yes / no |
| Release validation evidence is linked. | yes / no |
| Post-release learning is recorded. | yes / no |

---

## 16. Notes

Use this section for additional comments, unresolved questions, or contextual details that do not fit the tables above.

```text

```
