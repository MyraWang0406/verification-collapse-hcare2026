# Expert Walkthrough Protocol

This file defines a planned expert walkthrough protocol for future evaluation. It is **not** an executed study and does **not** report empirical results.

## Purpose

Evaluate whether the proposed decision trace workflow helps reviewers distinguish **formal approval** from **meaningful verification** in AI-assisted requirements engineering.

The walkthrough focuses on three questions:

1. Does the decision trace help reviewers detect missing business context, assumptions, dependencies, and risks?
2. Does the workflow make human verification more observable than a generic AI-generated requirement summary?
3. Which human control points are perceived as useful, burdensome, unclear, or difficult to implement in real RE workflows?

## Intended participants

Future participants may include practitioners familiar with software requirements decisions:

- product managers
- requirements engineers
- software engineers or architects
- QA / test leads
- engineering managers
- business stakeholders involved in requirements approval

A small pilot can use 3–5 experts before a larger evaluation.

## Materials

Each participant reviews the same anonymized or synthetic requirement scenario.

No private company data, internal PRDs, chat logs, meeting recordings, customer tickets, source code, production data, or company-identifying materials should be used.

Each participant reviews two artifacts:

1. **Generic AI-generated requirement summary**  
   A fluent summary of the requirement, written as if produced by an AI meeting summarizer or PRD assistant.

2. **AI-structured decision trace**  
   A structured trace based on the proposed decision trace template, including source context, assumptions, affected systems, change rationale, sign-off information, release evidence, and post-hoc review fields.

## Procedure

1. Introduce the study purpose without revealing the expected outcome.
2. Ask the participant to review the generic AI-generated requirement summary.
3. Ask the participant to complete Task Set A.
4. Ask the participant to review the AI-structured decision trace.
5. Ask the participant to complete Task Set B.
6. Conduct a short reflection interview.
7. Record qualitative comments and structured ratings.

Estimated duration: 30–45 minutes per participant.

## Task Set A: Generic AI Summary Review

After reading the generic AI-generated requirement summary, participants answer:

1. What information appears missing or uncertain?
2. Which assumptions would you verify before approving development?
3. Which systems, roles, or downstream processes may be affected?
4. Would you allow this requirement to proceed? Why or why not?
5. How confident are you in this decision?

## Task Set B: Decision Trace Review

After reading the AI-structured decision trace, participants answer:

1. What additional missing information did the trace reveal?
2. Which assumptions now appear most important to verify?
3. Which human role should own the admission decision?
4. Which change requests would require formal sign-off?
5. Which risks should trigger mandatory re-verification?
6. Would you allow this requirement to proceed? Why or why not?
7. Did your confidence change compared with Task Set A?

## Measures

| Measure | Meaning |
|---|---|
| Missing-context detection | Number and quality of missing assumptions, dependencies, or risks identified |
| Verification intent | Whether the participant would inspect source evidence before approval |
| Source-inspection depth | Number of source materials the participant wants to check |
| Decision confidence | Confidence before and after reviewing the structured trace |
| Accountability clarity | Whether the participant can identify a decision owner |
| Change-control awareness | Whether the participant identifies changes requiring sign-off |
| Perceived usefulness | Whether the trace helps decision-making |
| Perceived burden | Whether the trace feels too heavy for daily RE work |
| Adoption feasibility | Whether the workflow is realistic in the participant's organization |

Suggested rating scale:

| Score | Meaning |
|---:|---|
| 1 | Strongly disagree / not useful |
| 2 | Disagree / slightly useful |
| 3 | Neutral / moderately useful |
| 4 | Agree / useful |
| 5 | Strongly agree / very useful |

## Analysis plan

Future analysis should compare responses before and after exposure to the structured decision trace.

Suggested analysis:

1. Compare the number of missing assumptions detected in Task Set A vs Task Set B.
2. Compare decision confidence before and after reviewing the trace.
3. Identify whether participants shift from approval-oriented reasoning to verification-oriented reasoning.
4. Code qualitative comments into recurring themes, such as missing context, unclear decision ownership, hidden dependency, sign-off need, workflow burden, adoption barrier, and value of uncertainty marking.
5. Summarize which control points are considered most useful and which are hardest to implement.

## Expected output

A future evaluation report should include:

- participant profile
- scenario description
- artifacts used
- comparison of generic summary vs structured trace
- quantitative rating summary
- qualitative themes
- examples of participant comments
- limitations
- implications for refining the workflow

## Ethical and data-handling notes

This protocol should use only anonymized or synthetic scenarios.

Do not collect or publish:

- company names
- internal PRDs
- meeting recordings
- chat logs
- customer-identifiable complaints
- production incidents
- source code
- private business metrics

All participant comments should be anonymized before reporting.

## Status

Planned protocol only.  
No expert walkthrough has been conducted yet.  
No empirical findings are claimed in the current paper.
