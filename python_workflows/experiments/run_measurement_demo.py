import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from python_workflows.core import measurements


def basis_terms(state, nqubits, cutoff=1e-10):
    terms = []
    for index, amp in enumerate(state):
        if abs(amp) < cutoff:
            continue
        terms.append(f"{amp:.4g} |{index:0{nqubits}b}>")
    return " + ".join(terms) if terms else "0"


def main():
    output_dir = PROJECT_ROOT / "figures" / "python"
    output_dir.mkdir(parents=True, exist_ok=True)

    nqubits = 2
    psi = np.zeros(2**nqubits, dtype=np.complex128)
    psi[0] = 1 / np.sqrt(2)
    psi[3] = 1 / np.sqrt(2)

    z_outcome, post_z = measurements.measure_site(nqubits, 1, psi.copy())
    x_outcome, post_x = measurements.measure_siteX(nqubits, 2, psi.copy())

    print("Input Bell state:")
    print(basis_terms(psi, nqubits))
    print("\nProjective Z measurement on qubit 1:")
    print("Outcome:", z_outcome)
    print(basis_terms(post_z, nqubits))
    print("\nProjective X measurement on qubit 2:")
    print("Outcome:", x_outcome)
    print(basis_terms(post_x, nqubits))

    output_path = output_dir / "measurement_demo.txt"
    output_path.write_text(
        "Input Bell state:\n"
        + basis_terms(psi, nqubits)
        + "\n\nProjective Z measurement on qubit 1:\nOutcome: "
        + str(z_outcome)
        + "\n"
        + basis_terms(post_z, nqubits)
        + "\n\nProjective X measurement on qubit 2:\nOutcome: "
        + str(x_outcome)
        + "\n"
        + basis_terms(post_x, nqubits)
        + "\n",
        encoding="utf-8",
    )
    print(f"\nSaved summary to {output_path}")


if __name__ == "__main__":
    main()
