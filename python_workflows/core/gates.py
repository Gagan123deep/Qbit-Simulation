import numpy as np

class gates:
    """Class containing important 1-qubit and 2-qubit quantum gates as matrices."""

    # Single-qubit gates
    Hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    S = np.array([[1, 0], [0, 1j]])
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
    I = np.eye(2)  # Identity matrix

    # Two-qubit gates
    CNOT = np.array([
        [1, 0, 0, 0], 
        [0, 1, 0, 0], 
        [0, 0, 0, 1], 
        [0, 0, 1, 0]
    ])
    
    CZ = np.array([
        [1, 0, 0, 0], 
        [0, 1, 0, 0], 
        [0, 0, 1, 0], 
        [0, 0, 0, -1]
    ])

    SWAP = np.array([
        [1, 0, 0, 0], 
        [0, 0, 1, 0], 
        [0, 1, 0, 0], 
        [0, 0, 0, 1]
    ])

    iSWAP = np.array([
        [1, 0, 0, 0], 
        [0, 0, 1j, 0], 
        [0, 1j, 0, 0], 
        [0, 0, 0, 1]
    ])

    def Rk(k):
        return np.diag([1, 1, 1, np.exp(-1j * np.pi / 2**(k))])

