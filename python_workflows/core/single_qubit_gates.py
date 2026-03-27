import numpy as np

"""Single- and two-qubit gate definitions used by the Python state-vector workflows."""


def U_gate(theta, phi, lamda):
    """Return the most general single-qubit gate in Euler-angle form."""
    U = np.zeros((2, 2)) + 0 * 1j

    U[0, 0] = np.cos(theta / 2)
    U[0, 1] = -np.exp(1j * lamda) * np.sin(theta / 2)
    U[1, 0] = np.exp(1j * phi) * np.sin(theta / 2)
    U[1, 1] = np.exp(1j * phi + 1j * lamda) * np.cos(theta / 2)

    return U



def Hadamard():
    """Return the Hadamard gate."""
    H = np.zeros((2, 2)) + 0 * 1j

    H[0, 0] = 1
    H[0, 1] = 1
    H[1, 0] = 1
    H[1, 1] = -1

    H = H / 2**0.5

    return H

def X_gate():
    """Return the Pauli X gate."""
    return np.array([[0, 1], [1, 0]]) + 0 * 1j

def Y_gate():
    """Return the Pauli Y gate."""
    return np.array([[0, -1j], [1j, 0]]) + 0 * 1j

def Z_gate():
    """Return the Pauli Z gate."""
    return np.array([[1, 0], [0, -1]]) + 0 * 1j

def P_gate(lamda):
    """Return a one-qubit phase gate."""
    return np.array([[1, 0], [0, np.exp(1j * lamda)]])


def SQRT_X_gate():
    """Return a square-root X gate built from the eigendecomposition of X."""
    m = X_gate()
    _, eigvecs = np.linalg.eigh(m)
    a = np.diag([np.exp(-1j * np.pi / 2), 1])
    return eigvecs @ a @ eigvecs.T.conj()


def SQRT_Y_gate():
    """Return a square-root Y gate built from the eigendecomposition of Y."""
    m = Y_gate()
    _, eigvecs = np.linalg.eigh(m)
    a = np.diag([np.exp(-1j * np.pi / 2), 1])
    return eigvecs @ a @ eigvecs.T.conj()


def T_gate():
    """Return the T gate."""
    gate = np.zeros((2, 2)) + 0 * 1j
    gate[0, 0] = 1
    gate[1, 1] = np.exp(-1j * np.pi / 4)
    return gate


def swap():
    """Return the SWAP gate."""
    gate = np.zeros((4, 4)) + 0 * 1j
    gate[0, 0] = 1
    gate[1, 2] = 1
    gate[2, 1] = 1
    gate[3, 3] = 1
    return gate


def CNOT():
    """Return the controlled-NOT gate."""
    gate = np.zeros((4, 4)) + 0 * 1j
    gate[0, 0] = 1
    gate[1, 1] = 1
    gate[2, 3] = 1
    gate[3, 2] = 1
    return gate
