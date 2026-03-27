from pathlib import Path

from python_workflows.core import random_circuit


def main():
    output_dir = Path(__file__).resolve().parents[2] / "figures" / "python"
    output_dir.mkdir(parents=True, exist_ok=True)

    nqubits = 4
    nsteps = 24
    measurement_probability = 0.2

    entropies = random_circuit.random_state(
        N=nqubits,
        nsteps=nsteps,
        measurement_probability=measurement_probability,
    )

    print("Random circuit entropy trajectory")
    print("N =", nqubits)
    print("nsteps =", nsteps)
    print("measurement_probability =", measurement_probability)
    print("entropies =", entropies.tolist())

    csv_path = output_dir / "random_circuit_entropy.csv"
    with csv_path.open("w", encoding="utf-8") as handle:
        handle.write("step,entropy\n")
        for step, value in enumerate(entropies, start=1):
            handle.write(f"{step},{value}\n")

    print(f"Saved data to {csv_path}")

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
