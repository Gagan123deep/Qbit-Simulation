import numpy as np


def entropy(state, s, n):
    """Compute bipartite entanglement entropy across a cut after ``s`` qubits."""
    A = np.reshape(state, (2**s, 2**(n - s)))
    L = np.linalg.svd(A, compute_uv=False)
    S = 0.0
    for i in range(len(L)):
        prob = L[i] ** 2
        S = float(S - prob * np.log2(prob + 10 ** (-40)))
    return S

