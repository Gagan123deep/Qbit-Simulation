import numpy as np

from . import apply_single_qubit as single_qubit
from . import single_qubit_gates as sqg


def _projectors():
    p0 = np.array([[1, 0], [0, 0]], dtype=np.complex128)
    p1 = np.array([[0, 0], [0, 1]], dtype=np.complex128)
    return p0, p1


def measure_site(N, p, psi):
    """Measure qubit ``p`` in the computational basis and return outcome and post-state."""
    p0, p1 = _projectors()

    psi0 = single_qubit.Q_Operate(N, p, psi, p0)
    psi1 = single_qubit.Q_Operate(N, p, psi, p1)

    prob0 = np.vdot(psi0, psi0).real
    prob1 = max(1.0 - prob0, 0.0)

    if np.random.rand() < prob0:
        return +1, psi0 / np.sqrt(prob0)
    return -1, psi1 / np.sqrt(prob1)


def measure_siteX(N, p, psi):
    """Measure qubit ``p`` in the X basis by rotating with a Hadamard gate."""
    hadamard = sqg.Hadamard()
    rotated = single_qubit.Q_Operate(N, p, psi, hadamard)
    outcome, post_rotated = measure_site(N, p, rotated)
    post = single_qubit.Q_Operate(N, p, post_rotated, hadamard)
    return outcome, post


def measure_all_sites(psi, N):
    """Measure every qubit in sequence and return the observed computational basis index."""
    bits = []
    for p in range(1, N + 1):
        outcome, psi = measure_site(N, p, psi)
        bit = (1 - outcome) // 2
        bits.append(str(bit))
    return int("".join(bits), 2)
