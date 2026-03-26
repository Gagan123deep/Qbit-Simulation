# CV Bullet to Code Map

## 1. Python and Julia quantum simulation workflows

- Python state-vector workflow:
  - `python_workflows/core/apply_single_qubit.py`
  - `python_workflows/core/apply_two_qubit.py`
  - `python_workflows/core/single_qubit_gates.py`
  - `python_workflows/core/entropy.py`
- Julia MPS / ITensors workflow:
  - `julia_kraus_oqs/src/KraussSimulation.jl`
  - `julia_kraus_oqs/src/Krauss_protocol.jl`

## 2. Unitary gate evolution, QFT circuits, projective measurement, generalized measurement

- Unitary gate evolution:
  - `python_workflows/core/apply_single_qubit.py`
  - `python_workflows/core/apply_two_qubit.py`
- QFT circuits:
  - `python_workflows/core/qft.py`
  - `python_workflows/experiments/run_unitary_qft_demo.py`
- Projective measurement:
  - `python_workflows/core/measurements.py`
  - `python_workflows/experiments/run_measurement_demo.py`
- Kraus-operator generalized measurement:
  - `julia_kraus_oqs/src/Krauss_list.jl`
  - `julia_kraus_oqs/src/Krauss_protocol.jl`

## 3. Decoherence trajectories and entanglement entropy

- Random-circuit / probabilistic measurement exploration:
  - `python_workflows/core/random_circuit.py`
  - `python_workflows/experiments/run_random_circuit_demo.py`
- Entanglement entropy:
  - `python_workflows/core/entropy.py`
  - `julia_kraus_oqs/src/Krauss_entropy.jl`
  - `julia_kraus_oqs/src/Krauss_protocol.jl`
- Stochastic Kraus decoherence trajectories:
  - `julia_kraus_oqs/src/Krauss_list.jl`
  - `julia_kraus_oqs/src/Operating_Krauss.jl`
  - `julia_kraus_oqs/src/Krauss_protocol.jl`
