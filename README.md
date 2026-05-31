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

The simulation is intended as a mechanism probe and hypothesis generator, not as an empirical validation of real organizational behavior. It formalizes how workload-sensitive trust dynamics could suppress meaningful human verification in AI-assisted requirements approval workflows.

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

## Key concepts

**Approval** refers to a formal workflow act granting permission.

**Verification** refers to the cognitive act of checking facts, assumptions, and uncertainties against source evidence.

**Verification collapse** refers to a candidate workflow-level failure mode in which formal human approval degrades into passive acceptance without meaningful verification.

**Requirements decision traceability** refers to the ability to connect a requirements decision with its source context, assumptions, stakeholders, alternatives, risks, approval rationale, change history, release evidence, and post-release learning.

## Artifact overview

| Artifact | Path | Purpose |
|---|---|---|
| Simulation script | `simulation/simulation.py` | Illustrates how workload-sensitive trust dynamics may lead to reduced human verification. |
| Workflow table | `artifacts/workflow_table.md` | Converts the position paper's workflow into inspectable AI-support and human-gate stages. |
| Decision trace template | `artifacts/decision_trace_template.md` | Provides a reusable template for recording source anchors, uncertainty markers, sign-off records, and decision-owner fields. |
| Expert walkthrough protocol | `protocols/expert_walkthrough_protocol.md` | Provides a planned protocol for future expert review of the workflow and template. |

## Core trace fields

The proposed workflow centers on four verifiable trace fields:

1. **Source anchors**: which PRD, ticket, meeting note, test record, dashboard, or stakeholder statement supports each requirement claim.
2. **Uncertainty markers**: which assumptions, dependencies, edge cases, or business rules remain unverified.
3. **Sign-off records**: which major changes were accepted, by whom, why, and with what schedule or risk implications.
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
