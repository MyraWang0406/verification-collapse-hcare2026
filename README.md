# Verification Collapse in AI-Assisted Requirements Decisions

Supplementary artifacts for the HCARE 2026 position paper:

**Verification Collapse in AI-Assisted Requirements Decisions: Toward Human-Centered Decision Traceability**

This repository contains lightweight, anonymized materials that make the paper's proposed mechanism and workflow easier to inspect, reproduce, and extend.

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
├── .gitignore
├── LICENSE
└── README.md
```

## Scope

This repository is **not** an empirical dataset. It does **not** contain organizational logs, private business data, internal PRDs, meeting recordings, customer tickets, source code, production metrics, or company-identifying materials.

The simulation is intended as a **mechanism probe** and **hypothesis generator**, not as an empirical validation of real organizational behavior. It formalizes how workload-sensitive trust dynamics could suppress meaningful human verification in AI-assisted requirements approval workflows.

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

**Requirements decision traceability** refers to the ability to connect a requirement decision with its source context, assumptions, stakeholders, alternatives, risks, approval rationale, change history, release evidence, and post-release learning.

## Repository status

This repository supports a workshop position paper. It should be read as supplementary material for conceptual inspection, not as evidence of a completed field deployment or expert evaluation.

## Suggested citation

```bibtex
@misc{wang2026verificationcollapseartifact,
  title        = {Supplementary Artifacts for Verification Collapse in AI-Assisted Requirements Decisions},
  author       = {Zhimin Wang},
  year         = {2026},
  howpublished = {\url{https://github.com/MyraWang0406/verification-collapse-hcare2026}},
  note         = {Supplementary artifact repository for an HCARE 2026 submission}
}
```

## License

Code and templates are provided for academic discussion and replication of the illustrative mechanism. Do not use this repository to infer or identify any specific organization.
