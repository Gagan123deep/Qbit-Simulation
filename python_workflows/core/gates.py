"""Compatibility layer exposing common gate matrices from ``single_qubit_gates``."""

import numpy as np

from . import single_qubit_gates as sqg


class gates:
    """Grouped gate definitions kept for backward compatibility with older scripts."""

    Hadamard = sqg.Hadamard()
    X = sqg.X_gate()
    Y = sqg.Y_gate()
    Z = sqg.Z_gate()
    S = sqg.P_gate(np.pi / 2)
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=np.complex128)
    I = np.eye(2, dtype=np.complex128)

    CNOT = sqg.CNOT()
    SWAP = sqg.swap()
    CZ = np.diag([1, 1, 1, -1]).astype(np.complex128)
    iSWAP = np.array(
        [[1, 0, 0, 0], [0, 0, 1j, 0], [0, 1j, 0, 0], [0, 0, 0, 1]],
        dtype=np.complex128,
    )

    @staticmethod
    def Rk(k):
        return np.diag([1, 1, 1, np.exp(-1j * np.pi / 2**k)]).astype(np.complex128)
