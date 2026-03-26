import numpy as np

from . import single_qubit_gates as sqg
from . import apply_two_qubit as f2qo
from . import apply_single_qubit as fqo
from . import gates as g


def CRk(k):
    CRk=np.identity(4,dtype=np.complex128)
    CRk[3,3]=np.exp(-1j*np.pi/(2**k))
    return CRk
SWAP=g.gates.SWAP


def QFT_M_qubits_br(state, m):
    # Standard QFT circuit with a final bit-reversal implemented via SWAP gates.
    for i in range(1, m + 1):
        state = fqo.Q_Operate(m, i, state, sqg.Hadamard())
        k=1
        for j in range(i + 1, m + 1):
            state = f2qo.qubit2_op(m, i, j, state, CRk(k))
            k += 1
    for i in range(1, int(m / 2) + 1):
        state = f2qo.qubit2_op(m, i, m - i + 1, state, SWAP)
    return state
