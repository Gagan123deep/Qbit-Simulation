import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from python_workflows.core import random_circuit


def main():
    output_dir = PROJECT_ROOT / "figures" / "python"
    output_dir.mkdir(parents=True, exist_ok=True)

    nqubits = 10
    nsteps = 24
    measurement_probability = 0.1
    seed = 7

    result = random_circuit.run_random_circuit(
        N=nqubits,
        nsteps=nsteps,
        measurement_probability=measurement_probability,
        seed=seed,
    )
    entropies = result.entropies

    print("Random circuit entropy trajectory")
    print("N =", nqubits)
    print("nsteps =", nsteps)
    print("measurement_probability =", measurement_probability)
    print("seed =", seed)
    print("entropies =", entropies.tolist())
    print("measurements_per_step =", result.measurements_per_step.tolist())

    try:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(range(1, nsteps + 1), entropies, marker="o", linewidth=1.5)
        ax.set_xlabel("Step")
        ax.set_ylabel("Entropy")
        ax.set_title("Random circuit entropy trajectory")
        ax.grid(alpha=0.25)
        fig.tight_layout()
        plot_path = output_dir / "random_circuit_entropy.png"
        fig.savefig(plot_path, dpi=150)
        plt.close(fig)
        print(f"Saved figure to {plot_path}")
    except ImportError:
        print("matplotlib is not installed; skipped PNG export.")


if __name__ == "__main__":
    main()
