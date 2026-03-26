from random import randint

import numpy as np

from . import apply_single_qubit as single_qubit
from . import apply_two_qubit as two_qubit
from . import entropy as entropy_tools
from . import single_qubit_gates as sqg


def random_state(N, nsteps, measurement_probability):
    hadamard = sqg.Hadamard()
    pauli_x = sqg.X_gate()
    t_gate = sqg.T_gate()
    cnot = sqg.CNOT()

    psi = np.zeros(2**N, dtype=np.complex128)
    psi[0] = 1.0
    entropies = np.zeros(nsteps, dtype=float)
    midpoint = N // 2
    eps = 1e-30

    p0 = np.array([[1, 0], [0, 0]], dtype=np.complex128)
    p1 = np.array([[0, 0], [0, 1]], dtype=np.complex128)

    for step in range(nsteps):
        for site in range(1, N + 1):
            gate_choice = randint(1, 4)
            if gate_choice == 1:
                psi = single_qubit.Q_Operate(N, site, psi, hadamard)
            elif gate_choice == 2:
                psi = single_qubit.Q_Operate(N, site, psi, pauli_x)
            elif gate_choice == 3:
                psi = single_qubit.Q_Operate(N, site, psi, t_gate)

        for site in range(1, N):
            psi = two_qubit.qubit2_op(N, site, site + 1, psi, cnot)

        psi = psi / np.linalg.norm(psi)

        for site in range(1, N + 1):
            if np.random.rand() < measurement_probability:
                psi_plus = single_qubit.Q_Operate(N, site, psi, p0)
                prob_plus = np.linalg.norm(psi_plus) ** 2

                if prob_plus > eps and np.random.rand() < prob_plus:
                    psi = psi_plus / np.sqrt(prob_plus)
                else:
                    psi_minus = single_qubit.Q_Operate(N, site, psi, p1)
                    prob_minus = np.linalg.norm(psi_minus) ** 2
                    psi = psi_minus / np.sqrt(max(prob_minus, 1e-20))

        entropies[step] = entropy_tools.entropy(psi, midpoint, N)

    return entropies
