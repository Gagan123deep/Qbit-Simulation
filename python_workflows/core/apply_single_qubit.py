import numpy as np


def Q_Operate(N, p, psi, U):
    """Apply a single-qubit operator ``U`` to qubit ``p`` of an ``N``-qubit state."""
    psi_1 = np.zeros(2**N, dtype=np.complex128)
    a = 2 ** (N - p)
    for r in range(2**N):
        q = int(int(a & r) / a)
        q1 = int(1 ^ q)
        r1 = int(r ^ a)
        psi_1[r] = U[q, q] * psi[r] + U[q, q1] * psi[r1]
    return psi_1

