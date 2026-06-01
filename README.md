# Verification Collapse in AI-Assisted Requirements Decisions

Supplementary artifacts for the HCARE 2026 position paper:

**Verification Collapse in AI-Assisted Requirements Decisions: Toward Human-Centered Decision Traceability**

This repository contains lightweight, anonymized materials that support the paper's conceptual argument and make the proposed mechanism and workflow easier to inspect.

The repository is intended to support transparency and reproducibility of the conceptual mechanism, not to claim empirical validation.

## Repository structure

```text
verification-collapse-hcare2026/
├── simulation/
│   └── simulation.py
├── artifacts/
│   ├── decision_trace_template.md
│   └── workflow_table.md
├── protocols/
│   └── expert_walkthrough_protocol.md
├── requirements.txt
└── README.md
```

## Scope

This repository is not an empirical dataset and does not contain organizational logs, private business data, or company-identifying materials.

The simulation is intended as a mechanism probe and hypothesis generator, not as an empirical validation of real organizational behavior. It formalizes how workload, perceived AI reliability, context quality, role clarity, implementation evidence, and verification effort could interact in AI-assisted requirements approval workflows.

The workflow table, decision-trace template, and expert walkthrough protocol are provided as research artifacts for discussion, replication, and future evaluation.

## How to run the simulation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python simulation/simulation.py
```

The script creates an `outputs/` folder containing:

```text
outputs/results_summary.csv
outputs/timestep_results.csv
outputs/simulation_results.png
```

## What the simulation models

The simulation compares two workflow policies.

| Policy | Meaning |
|---|---|
| `approval_only` | A formal approval workflow where managers mainly rely on perceived AI confidence under workload pressure. Voluntary verification declines as trust increases. |
| `trace_gated` | A workflow where source checks, uncertainty checks, role checks, sign-off records, and repository-level reproduction checks can interrupt passive acceptance. |

The revised model separates **perceived AI reliability** from **substantive correctness**. This distinction is important because fluent AI output can sound reliable even when implementation details, source evidence, role boundaries, or historical code context are missing.

The simulation includes four hidden failure modes:

1. **Source gaps**: source evidence is missing, fragmented, or weak.
2. **Prompt abstraction gaps**: the prompt contains business rationale or design intent but not enough implementation detail, acceptance criteria, or code context.
3. **Role-context mismatch**: long or multi-person AI conversations mix stakeholder roles, responsibilities, or decision authority.
4. **Implementation-claim gaps**: an AI coding agent claims that something is implemented, but the repository or test evidence does not reproduce that claim.

## Key concepts

**Approval** refers to a formal workflow act granting permission.

**Verification** refers to the cognitive and procedural act of checking facts, assumptions, implementation evidence, and uncertainties against source materials.

**Verification collapse** refers to a candidate workflow-level failure mode in which formal human approval degrades into passive acceptance without meaningful verification.

**Requirements decision traceability** refers to the ability to connect a requirement decision with its source context, assumptions, stakeholders, alternatives, risks, approval rationale, change history, implementation evidence, release evidence, and post-release learning.

## Artifact overview

| Artifact | Path | Purpose |
|---|---|---|
| Simulation script | `simulation/simulation.py` | Illustrates how perceived AI reliability, workload, context gaps, role confusion, and implementation-claim gaps may affect verification behavior. |
| Workflow table | `artifacts/workflow_table.md` | Converts the position paper's workflow into inspectable AI-support and human-gate stages. |
| Decision trace template | `artifacts/decision_trace_template.md` | Provides a reusable template for recording source anchors, uncertainty markers, sign-off records, decision-owner fields, and implementation evidence. |
| Expert walkthrough protocol | `protocols/expert_walkthrough_protocol.md` | Provides a planned protocol for future expert review of the workflow and template. |

## Core trace fields

The proposed workflow centers on four verifiable trace fields:

1. **Source anchors**: which PRD, ticket, meeting note, test record, dashboard, repository commit, or stakeholder statement supports each requirement claim.
2. **Uncertainty markers**: which assumptions, dependencies, edge cases, implementation details, or business rules remain unverified.
3. **Sign-off records**: which major changes were accepted, by whom, why, and with what schedule, risk, or implementation implications.
4. **Decision-owner fields**: which human role accepted the residual risk behind the requirement decision.

## Suggested citation

```bibtex
@misc{wang2026verificationcollapseartifact,
  title = {Supplementary Artifacts for Verification Collapse in AI-Assisted Requirements Decisions},
  author = {Wang, Zhimin},
  year = {2026},
  howpublished = {GitHub repository},
  url = {https://github.com/MyraWang0406/verification-collapse-hcare2026},
  note = {Supplementary artifact repository for an HCARE 2026 submission}
}
```

## License

Code and templates are provided for academic discussion and replication of the illustrative mechanism. Do not use this repository to infer or identify any specific organization.
