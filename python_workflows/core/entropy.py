import numpy as np
import math

def entropy(state, s, n):
    A = np.reshape(state, (2**s, 2**(n - s)))  # Fix: shape must be a tuple
    L = np.linalg.svd(A, compute_uv=False)
    S = 0.0
    for i in range(len(L)):
        prob = L[i]**2
        S =float(S - prob*np.log2(prob+10**(-40))) # Prevent log(0)
    return S

