# Verification Collapse in AI-Assisted Requirements Decisions

Supplementary artifacts for an HCARE 2026 submission:

**Verification Collapse in AI-Assisted Requirements Decisions: Toward Human-Centered Decision Traceability**

This repository contains lightweight, anonymized materials that make the proposed mechanism and workflow easier to inspect and run.

## What this repository contains

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
├── LICENSE
└── README.md
```

## Scope

This repository is not an empirical dataset.

It does not contain organizational logs, private business data, internal PRDs, meeting recordings, source code, production metrics, customer-identifying materials, or company-identifying materials.

The simulation is intended as a **mechanism probe** and **hypothesis generator**, not as empirical validation of real organizational behavior.

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

## Included artifacts

### 1. Simulation

Path:

```text
simulation/simulation.py
```

The simulation models a minimal AI-assisted requirements approval workflow:

```text
Employee → AI Assistant → Manager → Decision
```

It explores how workload-sensitive trust dynamics may reduce human verification when modeled AI reliability appears high.

### 2. Workflow table

Path:

```text
artifacts/workflow_table.md
```

This file summarizes the six-stage human-centered AI workflow proposed in the paper:

1. Context completion
2. Pre-analysis
3. Admission decision
4. Change control
5. Release validation
6. Post-hoc review

### 3. Decision trace template

Path:

```text
artifacts/decision_trace_template.md
```

This template shows how a requirements decision can be recorded through source anchors, uncertainty markers, sign-off records, and decision-owner fields.

### 4. Expert walkthrough protocol

Path:

```text
protocols/expert_walkthrough_protocol.md
```

This protocol describes a planned future evaluation. It is not an executed study and does not report empirical findings.

## Suggested citation

```bibtex
@misc{wang2026verificationcollapseartifact,
  title        = {Supplementary Artifacts for Verification Collapse in AI-Assisted Requirements Decisions},
  author       = {Zhimin Wang},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/MyraWang0406/verification-collapse-hcare2026},
  note         = {Supplementary artifact repository for an HCARE 2026 submission}
}
```

## License

Code and templates are provided for academic discussion and replication of the illustrative mechanism. Do not use this repository to infer or identify any specific organization.
