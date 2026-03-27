from dataclasses import dataclass

import numpy as np

from . import apply_single_qubit as single_qubit
from . import apply_two_qubit as two_qubit
from . import entropy as entropy_tools
from . import single_qubit_gates as sqg


@dataclass
class RandomCircuitResult:
    """Container for one random-circuit trajectory."""

    entropies: np.ndarray
    final_state: np.ndarray
    measurements_per_step: np.ndarray
    N: int
    nsteps: int
    measurement_probability: float
    seed: int | None


def _validate_inputs(N, nsteps, measurement_probability):
    if N < 2:
        raise ValueError("N must be at least 2.")
    if nsteps < 1:
        raise ValueError("nsteps must be at least 1.")
    if not 0.0 <= measurement_probability <= 1.0:
        raise ValueError("measurement_probability must be between 0 and 1.")


def _sample_single_qubit_gate(rng):
    gate_index = rng.integers(0, 4)
    if gate_index == 0:
        return sqg.Hadamard()
    if gate_index == 1:
        return sqg.X_gate()
    if gate_index == 2:
        return sqg.T_gate()
    return sqg.Z_gate()


def run_random_circuit(N, nsteps, measurement_probability, seed=None):
    """Run one random circuit trajectory and return entropy and measurement history."""
    _validate_inputs(N, nsteps, measurement_probability)

    rng = np.random.default_rng(seed)
    cnot = sqg.CNOT()
    p0 = np.array([[1, 0], [0, 0]], dtype=np.complex128)
    p1 = np.array([[0, 0], [0, 1]], dtype=np.complex128)
    midpoint = N // 2
    eps = 1e-30

    psi = np.zeros(2**N, dtype=np.complex128)
    psi[0] = 1.0

    entropies = np.zeros(nsteps, dtype=float)
    measurements_per_step = np.zeros(nsteps, dtype=int)

    for step in range(nsteps):
        for site in range(1, N + 1):
            psi = single_qubit.Q_Operate(N, site, psi, _sample_single_qubit_gate(rng))

        for site in range(1, N):
            psi = two_qubit.qubit2_op(N, site, site + 1, psi, cnot)

        psi = psi / np.linalg.norm(psi)

        measurement_count = 0
        for site in range(1, N + 1):
            if rng.random() < measurement_probability:
                measurement_count += 1
                psi_plus = single_qubit.Q_Operate(N, site, psi, p0)
                prob_plus = np.linalg.norm(psi_plus) ** 2

                if prob_plus > eps and rng.random() < prob_plus:
                    psi = psi_plus / np.sqrt(prob_plus)
                else:
                    psi_minus = single_qubit.Q_Operate(N, site, psi, p1)
                    prob_minus = np.linalg.norm(psi_minus) ** 2
                    psi = psi_minus / np.sqrt(max(prob_minus, 1e-20))

        measurements_per_step[step] = measurement_count
        entropies[step] = entropy_tools.entropy(psi, midpoint, N)

    return RandomCircuitResult(
        entropies=entropies,
        final_state=psi,
        measurements_per_step=measurements_per_step,
        N=N,
        nsteps=nsteps,
        measurement_probability=measurement_probability,
        seed=seed,
    )


def average_entropy_trajectories(N, nsteps, measurement_probability, ntrajectories, seed=None):
    """Average entropy trajectories over multiple random-circuit realizations."""
    if ntrajectories < 1:
        raise ValueError("ntrajectories must be at least 1.")

    base_rng = np.random.default_rng(seed)
    trajectories = []
    for _ in range(ntrajectories):
        child_seed = int(base_rng.integers(0, 2**31 - 1))
        trajectories.append(run_random_circuit(N, nsteps, measurement_probability, seed=child_seed).entropies)

    entropy_array = np.vstack(trajectories)
    return {
        "mean_entropy": entropy_array.mean(axis=0),
        "std_entropy": entropy_array.std(axis=0),
        "all_entropies": entropy_array,
        "N": N,
        "nsteps": nsteps,
        "measurement_probability": measurement_probability,
        "ntrajectories": ntrajectories,
        "seed": seed,
    }


def random_state(N, nsteps, measurement_probability, seed=None):
    """Backward-compatible wrapper returning only the entropy trajectory."""
    return run_random_circuit(N, nsteps, measurement_probability, seed=seed).entropies
