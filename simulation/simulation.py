"""Illustrative simulation for:
Verification Collapse in AI-Assisted Requirements Decisions.

This script implements a small agent-based mechanism probe of an
AI-assisted requirements approval workflow.

The model is intentionally minimal. It is not an empirical organizational
model and is not calibrated from real company logs. Its purpose is to make
several plausible failure mechanisms inspectable:

1. Source gaps: AI summaries may sound complete even when source evidence is
   missing or weak.
2. Prompt-abstraction gaps: high-level prompts may contain background,
   business rationale, and design intent but not enough task-level detail,
   acceptance criteria, or repository context.
3. Role-context mismatches: long or multi-person AI conversations may mix the
   role, responsibility, and decision authority of different actors.
4. Implementation-claim gaps: an AI coding agent may claim completion even
   when the implementation is not reproducible from the repository.

The simulation compares two workflow policies:

- approval_only: managers mainly rely on perceived AI reliability and formal
  approval; voluntary verification declines as trust and workload increase.
- trace_gated: source anchors, uncertainty markers, role/owner checks, sign-off
  records, and reproduction checks are required with high compliance. These
  gates do not make the process perfect, but they make verification observable
  and can block passive acceptance.

Important boundary:
The simulation does not prove that verification collapse occurs in real
organizations. It encodes assumptions about workload, trust, and trace gates so
that readers can inspect and challenge the mechanism.

Outputs:
- outputs/results_summary.csv
- outputs/timestep_results.csv
- outputs/simulation_results.png
- outputs/simulation_results.pdf
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Tuple
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ----------------------------
# Configuration
# ----------------------------

SEED = 2026
STEPS = 200
REPEATS = 30
PERCEIVED_AI_RELIABILITIES = [0.60, 0.70, 0.80, 0.90, 0.95]
INITIAL_TRUST_LEVELS = [0.30, 0.60, 0.90]
WORKFLOWS = ["approval_only", "trace_gated"]

# Workload-sensitive trust dynamics.
WORKLOAD_THRESHOLD = 15
TRUST_INCREASE_UNDER_WORKLOAD = 0.03
TRUST_INCREASE_WHEN_NO_ISSUE_SEEN = 0.01
TRUST_DECAY_WHEN_ISSUE_CAUGHT = 0.08
MIN_TRUST = 0.10
MAX_TRUST = 0.95

# Requirement/context complexity. These are illustrative assumptions, not
# empirical rates.
SOURCE_GAP_RATE = 0.25
PROMPT_ABSTRACTION_GAP_RATE = 0.30
ROLE_COMPLEXITY_RATE = 0.25
IMPLEMENTATION_REQUIRED_RATE = 0.55
CODE_CONTEXT_GAP_RATE = 0.35

# Trace-gate behavior. A gate is "required" when the workflow should leave an
# inspectable record before approval. Compliance is high but imperfect to avoid
# assuming the proposed workflow fully solves the problem.
BASE_GATE_COMPLIANCE = 0.88
WORKLOAD_GATE_FRICTION = 0.08
MIN_GATE_COMPLIANCE = 0.74
GATE_ENFORCEMENT = 0.82  # probability that a missing required gate blocks approval

# Detection quality when the relevant gate is performed. These values represent
# imperfect human/tool review: a check can happen but still miss an issue.
SOURCE_CHECK_DETECTION = 0.80
UNCERTAINTY_CHECK_DETECTION = 0.68
ROLE_CHECK_DETECTION = 0.76
REPRODUCTION_CHECK_DETECTION = 0.90


@dataclass
class RequirementTask:
    source_gap: bool
    prompt_abstraction_gap: bool
    role_complexity: bool
    implementation_required: bool
    code_context_gap: bool


@dataclass
class AIOutput:
    summary_correct: bool
    role_assignment_correct: bool
    implementation_actual: bool
    claims_done: bool
    perceived_confidence: float


@dataclass
class StepRecord:
    workflow: str
    repeat: int
    step: int
    perceived_ai_reliability: float
    initial_trust: float
    trust: float
    workload: int
    source_gap: bool
    prompt_abstraction_gap: bool
    role_complexity: bool
    implementation_required: bool
    code_context_gap: bool
    summary_correct: bool
    role_assignment_correct: bool
    implementation_actual: bool
    claims_done: bool
    verified: bool
    all_required_gates_checked: bool
    caught_issue: bool
    accepted: bool
    false_acceptance: bool
    implementation_gap: bool
    role_context_failure: bool
    abstraction_failure: bool
    source_failure: bool


@dataclass
class SummaryRecord:
    workflow: str
    perceived_ai_reliability: float
    initial_trust: float
    repeats: int
    steps: int
    mean_verification_rate: float
    sd_verification_rate: float
    mean_gate_completion_rate: float
    sd_gate_completion_rate: float
    mean_false_acceptance_rate: float
    sd_false_acceptance_rate: float
    mean_implementation_gap_acceptance_rate: float
    sd_implementation_gap_acceptance_rate: float
    mean_role_context_failure_acceptance_rate: float
    sd_role_context_failure_acceptance_rate: float
    mean_final_trust: float
    sd_final_trust: float


class Employee:
    """Submits requirements whose context may be incomplete or mixed."""

    def submit_requirement(self) -> RequirementTask:
        implementation_required = random.random() < IMPLEMENTATION_REQUIRED_RATE
        return RequirementTask(
            source_gap=random.random() < SOURCE_GAP_RATE,
            prompt_abstraction_gap=random.random() < PROMPT_ABSTRACTION_GAP_RATE,
            role_complexity=random.random() < ROLE_COMPLEXITY_RATE,
            implementation_required=implementation_required,
            code_context_gap=implementation_required
            and random.random() < CODE_CONTEXT_GAP_RATE,
        )


class AIAssistant:
    """Produces fluent requirement summaries and implementation claims.

    perceived_ai_reliability is not empirical correctness. It represents how
    reliable the AI appears in the workflow. Actual correctness also depends on
    source evidence, prompt specificity, role clarity, and repository context.
    """

    def __init__(self, perceived_ai_reliability: float) -> None:
        if not 0.0 <= perceived_ai_reliability <= 1.0:
            raise ValueError("Reliability must be between 0 and 1.")
        self.perceived_ai_reliability = perceived_ai_reliability

    @staticmethod
    def _clip_probability(value: float) -> float:
        return max(0.02, min(0.98, value))

    def process(self, task: RequirementTask) -> AIOutput:
        # Fluent output can remain confident even when context is incomplete.
        perceived_confidence = self._clip_probability(
            self.perceived_ai_reliability
            + (0.08 if task.prompt_abstraction_gap else 0.0)
            + (0.05 if task.source_gap else 0.0)
        )

        # Actual task success improves only modestly with perceived reliability.
        # This separates "looks reliable" from "is grounded in context".
        substantive_base = 0.65 + 0.15 * ((self.perceived_ai_reliability - 0.60) / 0.35)
        summary_accuracy = self._clip_probability(
            substantive_base
            - (0.24 if task.source_gap else 0.0)
            - (0.20 if task.prompt_abstraction_gap else 0.0)
            - (0.12 if task.role_complexity else 0.0)
        )
        summary_correct = random.random() < summary_accuracy

        role_accuracy = self._clip_probability(
            substantive_base - (0.35 if task.role_complexity else 0.0)
        )
        role_assignment_correct = random.random() < role_accuracy

        if task.implementation_required:
            implementation_success = self._clip_probability(
                substantive_base
                - (0.34 if task.prompt_abstraction_gap else 0.0)
                - (0.40 if task.code_context_gap else 0.0)
                - (0.12 if task.source_gap else 0.0)
            )
            implementation_actual = random.random() < implementation_success
            if implementation_actual:
                claims_done = True
            else:
                # Over-confident completion claims are more likely when the AI appears
                # reliable but has weak prompt/repository context.
                false_done_claim_probability = self._clip_probability(
                    0.18
                    + 0.55 * self.perceived_ai_reliability
                    + (0.22 if task.prompt_abstraction_gap else 0.0)
                    + (0.25 if task.code_context_gap else 0.0)
                )
                claims_done = random.random() < false_done_claim_probability
        else:
            implementation_actual = True
            claims_done = False

        return AIOutput(
            summary_correct=summary_correct,
            role_assignment_correct=role_assignment_correct,
            implementation_actual=implementation_actual,
            claims_done=claims_done,
            perceived_confidence=perceived_confidence,
        )


class Manager:
    """Approves, verifies, or sends a requirement back for clarification."""

    def __init__(self, initial_trust: float, workflow: str) -> None:
        if not 0.0 <= initial_trust <= 1.0:
            raise ValueError("Initial trust must be between 0 and 1.")
        if workflow not in WORKFLOWS:
            raise ValueError(f"Unknown workflow: {workflow}")
        self.trust = initial_trust
        self.workflow = workflow
        self.workload = 0

    def update_workload(self) -> None:
        self.workload += 1

    def update_trust_after_step(self, caught_issue: bool) -> None:
        if self.workload > WORKLOAD_THRESHOLD:
            self.trust = min(MAX_TRUST, self.trust + TRUST_INCREASE_UNDER_WORKLOAD)
        if caught_issue:
            self.trust = max(MIN_TRUST, self.trust - TRUST_DECAY_WHEN_ISSUE_CAUGHT)
        else:
            self.trust = min(MAX_TRUST, self.trust + TRUST_INCREASE_WHEN_NO_ISSUE_SEEN)

    def approval_only_check(
        self,
        task: RequirementTask,
        ai_output: AIOutput,
        failures: Dict[str, bool],
    ) -> Tuple[bool, bool, bool, bool]:
        """Return verified, all_required_gates_checked, caught_issue, accepted."""
        # Higher trust and workload reduce voluntary verification.
        voluntary_verification_probability = max(
            0.02, min(0.90, 1.0 - self.trust - 0.001 * self.workload)
        )
        verified = random.random() < voluntary_verification_probability
        caught_issue = False
        if verified and any(failures.values()):
            # A voluntary review may still miss role/context or implementation gaps.
            caught_issue = random.random() < 0.55

        if caught_issue:
            accepted = False
        else:
            accepted_probability = max(
                0.10,
                min(0.98, 0.45 + 0.45 * ai_output.perceived_confidence + 0.20 * self.trust),
            )
            accepted = random.random() < accepted_probability
        return verified, False, caught_issue, accepted

    def _gate_compliance_probability(self) -> float:
        penalty = WORKLOAD_GATE_FRICTION if self.workload > WORKLOAD_THRESHOLD else 0.0
        return max(MIN_GATE_COMPLIANCE, BASE_GATE_COMPLIANCE - penalty)

    def trace_gated_check(
        self,
        task: RequirementTask,
        ai_output: AIOutput,
        failures: Dict[str, bool],
    ) -> Tuple[bool, bool, bool, bool]:
        """Return verified, all_required_gates_checked, caught_issue, accepted.

        The trace-gated policy is modeled as a procedural requirement, not as a
        low-probability voluntary review. Each applicable gate is required with
        high compliance. Missing required gates usually block approval, but the
        model still allows process slippage.
        """
        p = self._gate_compliance_probability()

        # Applicable gates. Source anchoring is always required; the other gates
        # are required when the task creates that kind of verification burden.
        source_required = True
        uncertainty_required = task.source_gap or task.prompt_abstraction_gap or task.code_context_gap
        role_required = task.role_complexity
        reproduction_required = task.implementation_required and ai_output.claims_done

        source_checked = source_required and random.random() < p
        uncertainty_checked = (not uncertainty_required) or random.random() < p
        role_checked = (not role_required) or random.random() < p
        reproduction_checked = (not reproduction_required) or random.random() < p

        required_gate_results = [source_checked]
        if uncertainty_required:
            required_gate_results.append(uncertainty_checked)
        if role_required:
            required_gate_results.append(role_checked)
        if reproduction_required:
            required_gate_results.append(reproduction_checked)

        all_required_gates_checked = all(required_gate_results)
        verified = any(required_gate_results)

        caught_issue = False
        if failures["source_failure"] and source_checked:
            caught_issue = caught_issue or (random.random() < SOURCE_CHECK_DETECTION)
        if failures["abstraction_failure"] and uncertainty_checked:
            caught_issue = caught_issue or (random.random() < UNCERTAINTY_CHECK_DETECTION)
        if failures["role_context_failure"] and role_checked:
            caught_issue = caught_issue or (random.random() < ROLE_CHECK_DETECTION)
        if failures["implementation_gap"] and reproduction_checked:
            caught_issue = caught_issue or (random.random() < REPRODUCTION_CHECK_DETECTION)

        missing_required_gate = not all_required_gates_checked
        if caught_issue:
            accepted = False
        elif missing_required_gate and random.random() < GATE_ENFORCEMENT:
            accepted = False
        else:
            # If required gates were completed and no issue was detected, acceptance can
            # proceed. If the gate process slipped, a lower residual probability remains.
            base = 0.72 if all_required_gates_checked else 0.28
            accepted_probability = max(
                0.05,
                min(0.88, base + 0.10 * ai_output.perceived_confidence + 0.04 * self.trust),
            )
            accepted = random.random() < accepted_probability
        return verified, all_required_gates_checked, caught_issue, accepted

    def decide(
        self,
        task: RequirementTask,
        ai_output: AIOutput,
        failures: Dict[str, bool],
    ) -> Tuple[bool, bool, bool, bool]:
        if self.workflow == "approval_only":
            verified, all_required_gates_checked, caught_issue, accepted = self.approval_only_check(
                task, ai_output, failures
            )
        else:
            verified, all_required_gates_checked, caught_issue, accepted = self.trace_gated_check(
                task, ai_output, failures
            )
        self.update_trust_after_step(caught_issue)
        return verified, all_required_gates_checked, caught_issue, accepted


def classify_failures(task: RequirementTask, ai_output: AIOutput) -> Dict[str, bool]:
    implementation_gap = (
        task.implementation_required and ai_output.claims_done and not ai_output.implementation_actual
    )
    role_context_failure = task.role_complexity and not ai_output.role_assignment_correct
    abstraction_failure = task.prompt_abstraction_gap and (
        not ai_output.summary_correct or implementation_gap
    )
    source_failure = task.source_gap and not ai_output.summary_correct
    return {
        "implementation_gap": implementation_gap,
        "role_context_failure": role_context_failure,
        "abstraction_failure": abstraction_failure,
        "source_failure": source_failure,
    }


def run_single_simulation(
    workflow: str,
    perceived_ai_reliability: float,
    initial_trust: float,
    repeat_id: int,
    steps: int = STEPS,
) -> List[StepRecord]:
    employee = Employee()
    ai = AIAssistant(perceived_ai_reliability)
    manager = Manager(initial_trust, workflow)
    records: List[StepRecord] = []

    for step in range(steps):
        manager.update_workload()
        task = employee.submit_requirement()
        ai_output = ai.process(task)
        failures = classify_failures(task, ai_output)
        verified, all_required_gates_checked, caught_issue, accepted = manager.decide(
            task, ai_output, failures
        )
        false_acceptance = accepted and any(failures.values()) and not caught_issue

        records.append(
            StepRecord(
                workflow=workflow,
                repeat=repeat_id,
                step=step,
                perceived_ai_reliability=perceived_ai_reliability,
                initial_trust=initial_trust,
                trust=manager.trust,
                workload=manager.workload,
                source_gap=task.source_gap,
                prompt_abstraction_gap=task.prompt_abstraction_gap,
                role_complexity=task.role_complexity,
                implementation_required=task.implementation_required,
                code_context_gap=task.code_context_gap,
                summary_correct=ai_output.summary_correct,
                role_assignment_correct=ai_output.role_assignment_correct,
                implementation_actual=ai_output.implementation_actual,
                claims_done=ai_output.claims_done,
                verified=verified,
                all_required_gates_checked=all_required_gates_checked,
                caught_issue=caught_issue,
                accepted=accepted,
                false_acceptance=false_acceptance,
                implementation_gap=failures["implementation_gap"],
                role_context_failure=failures["role_context_failure"],
                abstraction_failure=failures["abstraction_failure"],
                source_failure=failures["source_failure"],
            )
        )
    return records


def run_parameter_sweep() -> Tuple[pd.DataFrame, pd.DataFrame]:
    random.seed(SEED)
    np.random.seed(SEED)
    all_records: List[StepRecord] = []
    for workflow in WORKFLOWS:
        for perceived_ai_reliability in PERCEIVED_AI_RELIABILITIES:
            for initial_trust in INITIAL_TRUST_LEVELS:
                for repeat in range(REPEATS):
                    all_records.extend(
                        run_single_simulation(
                            workflow=workflow,
                            perceived_ai_reliability=perceived_ai_reliability,
                            initial_trust=initial_trust,
                            repeat_id=repeat,
                        )
                    )

    timestep_df = pd.DataFrame([asdict(record) for record in all_records])
    summary_rows: List[SummaryRecord] = []

    grouped = timestep_df.groupby(["workflow", "perceived_ai_reliability", "initial_trust"])
    for (workflow, perceived_ai_reliability, initial_trust), group in grouped:
        per_repeat = group.groupby("repeat").agg(
            verification_rate=("verified", "mean"),
            gate_completion_rate=("all_required_gates_checked", "mean"),
            false_acceptance_rate=("false_acceptance", "mean"),
            implementation_gap_acceptance_rate=(
                "implementation_gap",
                lambda s: float(((s) & group.loc[s.index, "false_acceptance"]).mean()),
            ),
            role_context_failure_acceptance_rate=(
                "role_context_failure",
                lambda s: float(((s) & group.loc[s.index, "false_acceptance"]).mean()),
            ),
            final_trust=("trust", "last"),
        )
        summary_rows.append(
            SummaryRecord(
                workflow=str(workflow),
                perceived_ai_reliability=float(perceived_ai_reliability),
                initial_trust=float(initial_trust),
                repeats=REPEATS,
                steps=STEPS,
                mean_verification_rate=float(per_repeat["verification_rate"].mean()),
                sd_verification_rate=float(per_repeat["verification_rate"].std(ddof=1)),
                mean_gate_completion_rate=float(per_repeat["gate_completion_rate"].mean()),
                sd_gate_completion_rate=float(per_repeat["gate_completion_rate"].std(ddof=1)),
                mean_false_acceptance_rate=float(per_repeat["false_acceptance_rate"].mean()),
                sd_false_acceptance_rate=float(per_repeat["false_acceptance_rate"].std(ddof=1)),
                mean_implementation_gap_acceptance_rate=float(
                    per_repeat["implementation_gap_acceptance_rate"].mean()
                ),
                sd_implementation_gap_acceptance_rate=float(
                    per_repeat["implementation_gap_acceptance_rate"].std(ddof=1)
                ),
                mean_role_context_failure_acceptance_rate=float(
                    per_repeat["role_context_failure_acceptance_rate"].mean()
                ),
                sd_role_context_failure_acceptance_rate=float(
                    per_repeat["role_context_failure_acceptance_rate"].std(ddof=1)
                ),
                mean_final_trust=float(per_repeat["final_trust"].mean()),
                sd_final_trust=float(per_repeat["final_trust"].std(ddof=1)),
            )
        )

    summary_df = pd.DataFrame([asdict(record) for record in summary_rows])
    return timestep_df, summary_df


def plot_results(summary_df: pd.DataFrame, output_path: Path) -> None:
    """Create a two-panel figure for the paper and README."""
    pooled = (
        summary_df.groupby(["workflow", "perceived_ai_reliability"])
        .agg(
            verification_rate=("mean_verification_rate", "mean"),
            false_acceptance_rate=("mean_false_acceptance_rate", "mean"),
            gate_completion_rate=("mean_gate_completion_rate", "mean"),
        )
        .reset_index()
    )

    figure, axes = plt.subplots(1, 2, figsize=(10, 4))

    labels = {"approval_only": "Approval only", "trace_gated": "Trace-gated"}

    ax = axes[0]
    for workflow, group in pooled.groupby("workflow"):
        group = group.sort_values("perceived_ai_reliability")
        ax.plot(
            group["perceived_ai_reliability"],
            group["verification_rate"],
            marker="o",
            label=labels[workflow],
        )
    ax.set_title("(a) Human verification rate")
    ax.set_xlabel("Perceived AI reliability")
    ax.set_ylabel("Verification rate")
    ax.set_ylim(0, 1.0)
    ax.legend(fontsize=8)

    ax = axes[1]
    for workflow, group in pooled.groupby("workflow"):
        group = group.sort_values("perceived_ai_reliability")
        ax.plot(
            group["perceived_ai_reliability"],
            group["false_acceptance_rate"],
            marker="o",
            label=labels[workflow],
        )
    ax.set_title("(b) False acceptance rate")
    ax.set_xlabel("Perceived AI reliability")
    ax.set_ylabel("Invalid decision accepted")
    ax.set_ylim(0, max(0.35, pooled["false_acceptance_rate"].max() + 0.05))
    ax.legend(fontsize=8)

    figure.tight_layout()
    figure.savefig(output_path, dpi=300, bbox_inches="tight")
    figure.savefig(output_path.with_suffix(".pdf"), bbox_inches="tight")
    plt.close(figure)


def print_paper_relevant_checks(summary_df: pd.DataFrame) -> None:
    pooled = (
        summary_df.groupby(["workflow", "perceived_ai_reliability"])
        .agg(
            verification_rate=("mean_verification_rate", "mean"),
            gate_completion_rate=("mean_gate_completion_rate", "mean"),
            false_acceptance_rate=("mean_false_acceptance_rate", "mean"),
            implementation_gap_acceptance_rate=("mean_implementation_gap_acceptance_rate", "mean"),
        )
        .reset_index()
    )
    print("\nPaper-relevant checks:")
    for workflow in WORKFLOWS:
        subset = pooled[pooled["workflow"] == workflow].sort_values("perceived_ai_reliability")
        first = subset.iloc[0]
        last = subset.iloc[-1]
        print(
            f"- {workflow}: verification {first.verification_rate:.3f} -> "
            f"{last.verification_rate:.3f}; gate completion "
            f"{first.gate_completion_rate:.3f} -> {last.gate_completion_rate:.3f}; "
            f"false acceptance {first.false_acceptance_rate:.3f} -> "
            f"{last.false_acceptance_rate:.3f}; implementation-gap acceptance "
            f"{first.implementation_gap_acceptance_rate:.3f} -> "
            f"{last.implementation_gap_acceptance_rate:.3f}"
        )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output_dir = root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestep_df, summary_df = run_parameter_sweep()
    timestep_df.to_csv(output_dir / "timestep_results.csv", index=False)
    summary_df.to_csv(output_dir / "results_summary.csv", index=False)
    plot_results(summary_df, output_dir / "simulation_results.png")
    print_paper_relevant_checks(summary_df)

    print("\nDone.")
    print(f"Saved: {output_dir / 'timestep_results.csv'}")
    print(f"Saved: {output_dir / 'results_summary.csv'}")
    print(f"Saved: {output_dir / 'simulation_results.png'}")
    print(f"Saved: {output_dir / 'simulation_results.pdf'}")


if __name__ == "__main__":
    main()
