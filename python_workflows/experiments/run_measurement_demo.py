import numpy as np

from python_workflows.core import measurements


def basis_terms(state, nqubits, cutoff=1e-10):
    terms = []
    for index, amp in enumerate(state):
        if abs(amp) < cutoff:
            continue
        terms.append(f"{amp:.4g} |{index:0{nqubits}b}>")
    return " + ".join(terms) if terms else "0"


def main():
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


if __name__ == "__main__":
    main()
