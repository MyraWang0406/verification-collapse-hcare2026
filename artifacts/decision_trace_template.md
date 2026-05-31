# Decision Trace Template

This template provides a lightweight structure for recording AI-assisted requirements decisions.

It is designed to preserve four kinds of trace evidence:

1. Source anchors
2. Uncertainty markers
3. Sign-off records
4. Decision-owner fields

The template is not intended to replace existing requirement tools. It can be attached to a PRD, ticket, design review, release record, or post-hoc review.

---

## 1. Requirement decision summary

| Field | Content |
|---|---|
| Requirement / decision name |  |
| Decision ID |  |
| Date |  |
| Product / system area |  |
| Decision status | proposed / accepted / rejected / postponed / changed / released |
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

## 4. Key assumptions

Record assumptions that influence the decision.

| Assumption | Evidence source | Confidence | Needs verification? | Owner |
|---|---|---|---|---|
|  |  | low / medium / high | yes / no |  |
|  |  | low / medium / high | yes / no |  |
|  |  | low / medium / high | yes / no |  |

---

## 5. Uncertainty markers

Record what remains unclear, risky, or under-verified.

| Uncertainty | Why it matters | Current evidence | Next verification step | Owner |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

## 6. Affected systems and dependencies

| System / module | Expected impact | Dependency owner | Risk level | Notes |
|---|---|---|---|---|
|  |  |  | low / medium / high |  |
|  |  |  | low / medium / high |  |
|  |  |  | low / medium / high |  |

---

## 7. Alternatives considered

| Alternative | Reason considered | Reason accepted or rejected | Evidence |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |

---

## 8. Sign-off record

| Decision item | Approved by | Role | Date | Rationale | Conditions |
|---|---|---|---|---|---|
| Initial admission |  |  |  |  |  |
| Major change |  |  |  |  |  |
| Release readiness |  |  |  |  |  |
| Residual risk acceptance |  |  |  |  |  |

---

## 9. Change-control record

Use this section when the requirement changes after initial admission.

| Change | Reason | Requested by | Approved by | Risk introduced | Schedule impact |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |

---

## 10. Release validation

| Acceptance criterion | Evidence | Verified by | Status |
|---|---|---|---|
|  |  |  | not checked / passed / failed |
|  |  |  | not checked / passed / failed |
|  |  |  | not checked / passed / failed |

---

## 11. Post-release review

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

## 12. Verification checklist

Before closing the decision trace, check the following items.

| Check item | Status |
|---|---|
| Source anchors are recorded. | yes / no |
| Unverified assumptions are marked. | yes / no |
| Major changes have sign-off records. | yes / no |
| A human decision owner is named. | yes / no |
| Residual risks are explicitly accepted or escalated. | yes / no |
| Release validation evidence is linked. | yes / no |
| Post-release learning is recorded. | yes / no |

---

## 13. Notes

Use this section for additional comments, unresolved questions, or contextual details that do not fit the tables above.

```text

```
