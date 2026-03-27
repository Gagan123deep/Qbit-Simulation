import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from python_workflows.core import random_circuit


def main():
    output_dir = PROJECT_ROOT / "figures" / "python"
    output_dir.mkdir(parents=True, exist_ok=True)

    nqubits = 4
    nsteps = 24
    ntrajectories = 12
    measurement_probabilities = [0.0, 0.1, 0.2, 0.4]
    seed = 21

    summaries = []
    for probability in measurement_probabilities:
        result = random_circuit.average_entropy_trajectories(
            N=nqubits,
            nsteps=nsteps,
            measurement_probability=probability,
            ntrajectories=ntrajectories,
            seed=seed,
        )
        summaries.append(result)

    print("Random circuit measurement-probability comparison")
    print("N =", nqubits)
    print("nsteps =", nsteps)
    print("ntrajectories =", ntrajectories)
    print("probabilities =", measurement_probabilities)

    try:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(6.5, 4.5))
        for probability, summary in zip(measurement_probabilities, summaries):
            ax.plot(
                range(1, nsteps + 1),
                summary["mean_entropy"],
                linewidth=1.7,
                label=f"p = {probability:.2f}",
            )
        ax.set_xlabel("Step")
        ax.set_ylabel("Average entropy")
        ax.set_title("Random circuit entropy for different measurement probabilities")
        ax.grid(alpha=0.25)
        ax.legend()
        fig.tight_layout()

        plot_path = output_dir / "random_circuit_probability_comparison.png"
        fig.savefig(plot_path, dpi=150)
        plt.close(fig)
        print(f"Saved figure to {plot_path}")
    except ImportError:
        print("matplotlib is not installed; skipped PNG export.")


if __name__ == "__main__":
    main()
