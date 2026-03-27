import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from python_workflows.core import qft


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
    state = np.zeros(2**nqubits, dtype=np.complex128)
    state[0] = 1 / np.sqrt(2)
    state[1] = 1 / np.sqrt(2)

    qft_state = qft.QFT_M_qubits_br(state.copy(), nqubits)
    dft_state = np.fft.fft(state, norm="ortho")

    print("Initial state:")
    print(basis_terms(state, nqubits))
    print("\nQFT circuit output:")
    print(basis_terms(qft_state, nqubits))
    print("\nReference DFT output:")
    print(basis_terms(dft_state, nqubits))

    output_path = output_dir / "unitary_qft_demo.txt"
    output_path.write_text(
        "Initial state:\n"
        + basis_terms(state, nqubits)
        + "\n\nQFT circuit output:\n"
        + basis_terms(qft_state, nqubits)
        + "\n\nReference DFT output:\n"
        + basis_terms(dft_state, nqubits)
        + "\n",
        encoding="utf-8",
    )
    print(f"\nSaved summary to {output_path}")


if __name__ == "__main__":
    main()
