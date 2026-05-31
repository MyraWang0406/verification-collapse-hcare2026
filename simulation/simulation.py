"""Illustrative simulation for:
Verification Collapse in AI-Assisted Requirements Decisions.

This script implements a minimal agent-based simulation of an AI-assisted
requirements approval workflow:

    Employee -> AI Assistant -> Manager -> Decision

Purpose:
    - mechanism probe
    - hypothesis generator
    - reproducible supplementary artifact for workshop discussion

Non-purpose:
    - not an empirical organizational model
    - not calibrated from real company logs
    - not proof that verification collapse occurs in any specific organization

Outputs:
    - outputs/results_summary.csv
    - outputs/timestep_results.csv
    - outputs/simulation_results.png
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List, Tuple
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

AI_RELIABILITIES = [0.60, 0.70, 0.80, 0.90, 0.95]
INITIAL_TRUST_LEVELS = [0.30, 0.60, 0.90]

EMPLOYEE_ERROR_RATE = 0.20
WORKLOAD_THRESHOLD = 15

TRUST_INCREASE_UNDER_WORKLOAD = 0.04
TRUST_DECAY_ON_CAUGHT_AI_ERROR = 0.08

MIN_TRUST = 0.10
MAX_TRUST = 0.95


@dataclass
class StepRecord:
    repeat: int
    step: int
    ai_reliability: float
    initial_trust: float
    trust: float
    workload: int
    task_correct: bool
    ai_view_correct: bool
    verified: bool
    final_correct: bool
    hidden_error: bool


@dataclass
class SummaryRecord:
    ai_reliability: float
    initial_trust: float
    repeats: int
    steps: int
    mean_hidden_error_rate: float
    sd_hidden_error_rate: float
    mean_verification_rate: float
    sd_verification_rate: float
    mean_final_trust: float
    sd_final_trust: float


class Employee:
    """Produces requirements, some of which contain hidden errors."""

    def __init__(self, error_rate: float = EMPLOYEE_ERROR_RATE) -> None:
        self.error_rate = error_rate

    def submit_requirement(self) -> bool:
        """Return True if the requirement is correct."""
        return random.random() > self.error_rate


class AIAssistant:
    """Summarizes the requirement and may distort the correctness signal."""

    def __init__(self, reliability: float) -> None:
        if not 0.0 <= reliability <= 1.0:
            raise ValueError("AI reliability must be between 0 and 1.")
        self.reliability = reliability

    def summarize(self, task_correct: bool) -> bool:
        """Return the AI's view of correctness.

        With probability `reliability`, the AI preserves the true correctness
        signal. Otherwise, it flips the signal.
        """
        if random.random() < self.reliability:
            return task_correct
        return not task_correct


class Manager:
    """Approves, verifies, or passively accepts AI-mediated information."""

    def __init__(self, initial_trust: float) -> None:
        if not 0.0 <= initial_trust <= 1.0:
            raise ValueError("Initial trust must be between 0 and 1.")
        self.trust = initial_trust
        self.workload = 0

    def update_workload(self) -> None:
        """Each processed requirement increases approval pressure."""
        self.workload += 1

    def maybe_increase_trust_under_workload(self) -> None:
        """Workload-sensitive trust drift.

        The rule represents an assumption that overloaded managers rely more on
        AI-mediated summaries when processing many requirements.
        """
        if self.workload > WORKLOAD_THRESHOLD:
            self.trust = min(MAX_TRUST, self.trust + TRUST_INCREASE_UNDER_WORKLOAD)

    def verification_probability(self) -> float:
        """Higher trust lowers human verification probability."""
        return max(0.0, min(1.0, 1.0 - self.trust))

    def decide(self, task_correct: bool, ai_view_correct: bool) -> Tuple[bool, bool]:
        """Return whether the manager verified and whether the final decision is correct."""
        verified = random.random() < self.verification_probability()

        if verified:
            # Verification checks against source evidence.
            final_correct = task_correct

            # If verification catches an AI error, trust decays.
            if ai_view_correct != task_correct:
                self.trust = max(MIN_TRUST, self.trust - TRUST_DECAY_ON_CAUGHT_AI_ERROR)
        else:
            # Passive acceptance of the AI-mediated view.
            final_correct = ai_view_correct

        return verified, final_correct


def run_single_simulation(
    ai_reliability: float,
    initial_trust: float,
    repeat_id: int,
    steps: int = STEPS,
) -> List[StepRecord]:
    """Run one simulation trajectory."""
    employee = Employee()
    ai = AIAssistant(ai_reliability)
    manager = Manager(initial_trust)

    records: List[StepRecord] = []

    for step in range(steps):
        manager.update_workload()
        manager.maybe_increase_trust_under_workload()

        task_correct = employee.submit_requirement()
        ai_view_correct = ai.summarize(task_correct)

        verified, final_correct = manager.decide(task_correct, ai_view_correct)
        hidden_error = not final_correct

        records.append(
            StepRecord(
                repeat=repeat_id,
                step=step,
                ai_reliability=ai_reliability,
                initial_trust=initial_trust,
                trust=manager.trust,
                workload=manager.workload,
                task_correct=task_correct,
                ai_view_correct=ai_view_correct,
                verified=verified,
                final_correct=final_correct,
                hidden_error=hidden_error,
            )
        )

    return records


def run_parameter_sweep() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Run all reliability x initial-trust combinations."""
    random.seed(SEED)
    np.random.seed(SEED)

    all_records: List[StepRecord] = []

    for ai_reliability in AI_RELIABILITIES:
        for initial_trust in INITIAL_TRUST_LEVELS:
            for repeat in range(REPEATS):
                all_records.extend(
                    run_single_simulation(
                        ai_reliability=ai_reliability,
                        initial_trust=initial_trust,
                        repeat_id=repeat,
                    )
                )

    timestep_df = pd.DataFrame([asdict(record) for record in all_records])

    summary_rows: List[SummaryRecord] = []
    grouped = timestep_df.groupby(["ai_reliability", "initial_trust"])

    for (ai_reliability, initial_trust), group in grouped:
        per_repeat = group.groupby("repeat").agg(
            hidden_error_rate=("hidden_error", "mean"),
            verification_rate=("verified", "mean"),
            final_trust=("trust", "last"),
        )

        summary_rows.append(
            SummaryRecord(
                ai_reliability=float(ai_reliability),
                initial_trust=float(initial_trust),
                repeats=REPEATS,
                steps=STEPS,
                mean_hidden_error_rate=float(per_repeat["hidden_error_rate"].mean()),
                sd_hidden_error_rate=float(per_repeat["hidden_error_rate"].std(ddof=1)),
                mean_verification_rate=float(per_repeat["verification_rate"].mean()),
                sd_verification_rate=float(per_repeat["verification_rate"].std(ddof=1)),
                mean_final_trust=float(per_repeat["final_trust"].mean()),
                sd_final_trust=float(per_repeat["final_trust"].std(ddof=1)),
            )
        )

    summary_df = pd.DataFrame([asdict(record) for record in summary_rows])
    return timestep_df, summary_df


def plot_results(
    timestep_df: pd.DataFrame,
    summary_df: pd.DataFrame,
    output_path: Path,
) -> None:
    """Create one two-panel figure matching the paper's mechanism story."""
    figure, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Panel A: trust drift trajectory at one modeled AI reliability.
    target_reliability = 0.90
    trust_df = timestep_df[timestep_df["ai_reliability"] == target_reliability]
    trust_curve = (
        trust_df.groupby(["initial_trust", "step"])["trust"]
        .mean()
        .reset_index()
    )

    ax = axes[0]
    for initial_trust, group in trust_curve.groupby("initial_trust"):
        ax.plot(group["step"], group["trust"], label=f"Initial trust = {initial_trust:.2f}")
    ax.set_title("(a) Trust drift")
    ax.set_xlabel("Step")
    ax.set_ylabel("Manager trust")
    ax.set_ylim(0, 1.0)
    ax.legend(fontsize=8)

    # Panel B: verification rate as AI reliability changes.
    ax = axes[1]
    for initial_trust, group in summary_df.groupby("initial_trust"):
        group_sorted = group.sort_values("ai_reliability")
        ax.plot(
            group_sorted["ai_reliability"],
            group_sorted["mean_verification_rate"],
            marker="o",
            label=f"Initial trust = {initial_trust:.2f}",
        )
    ax.set_title("(b) Verification rate")
    ax.set_xlabel("Modeled AI reliability")
    ax.set_ylabel("Human verification rate")
    ax.set_ylim(0, max(0.35, summary_df["mean_verification_rate"].max() + 0.05))
    ax.legend(fontsize=8)

    figure.tight_layout()
    figure.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(figure)


def print_paper_relevant_checks(summary_df: pd.DataFrame) -> None:
    """Print key numbers used for quick sanity checks."""
    low_trust = summary_df[summary_df["initial_trust"] == 0.30].sort_values(
        "ai_reliability"
    )

    first = low_trust.iloc[0]
    last = low_trust.iloc[-1]

    print("\nSanity checks:")
    print(
        f"- Low initial trust verification rate at AI reliability {first.ai_reliability:.2f}: "
        f"{first.mean_verification_rate:.3f}"
    )
    print(
        f"- Low initial trust verification rate at AI reliability {last.ai_reliability:.2f}: "
        f"{last.mean_verification_rate:.3f}"
    )
    print(
        f"- Mean final trust range: "
        f"{summary_df['mean_final_trust'].min():.3f} to "
        f"{summary_df['mean_final_trust'].max():.3f}"
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output_dir = root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestep_df, summary_df = run_parameter_sweep()

    timestep_df.to_csv(output_dir / "timestep_results.csv", index=False)
    summary_df.to_csv(output_dir / "results_summary.csv", index=False)

    plot_results(timestep_df, summary_df, output_dir / "simulation_results.png")
    print_paper_relevant_checks(summary_df)

    print("\nDone.")
    print(f"Saved: {output_dir / 'timestep_results.csv'}")
    print(f"Saved: {output_dir / 'results_summary.csv'}")
    print(f"Saved: {output_dir / 'simulation_results.png'}")


if __name__ == "__main__":
    main()
