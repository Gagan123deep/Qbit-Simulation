# Quantum Simulation Portfolio

Collection of Python and Julia quantum-simulation workflows supporting unitary circuit evolution, projective and generalized measurement, open-system Kraus dynamics, and entanglement-entropy analysis.

This repository is organized to match three core project themes:

- Python and Julia quantum simulation workflows
- unitary gates, QFT circuits, and measurement channels
- stochastic decoherence trajectories and entanglement tracking

## Overview

The portfolio combines two complementary tracks:

- a **Python state-vector toolkit** for gate-based circuit evolution, Quantum Fourier Transform (QFT), projective measurement, entropy calculation, and random-circuit experiments
- a **Julia open-quantum-system simulator** using `ITensors` / `ITensorMPS` to model two-qubit Kraus dynamics with loss, gain, dephasing, and measurement

Together, these workflows support a compact but defensible quantum-simulation portfolio for coursework, research applications, and CV use.

## What This Repository Demonstrates

- Single- and two-qubit unitary evolution in Python
- Quantum Fourier Transform circuits and verification against a discrete Fourier transform
- Projective measurement in different bases
- Generalized measurement and decoherence channels using Kraus operators
- Open-system stochastic trajectory simulation
- Entanglement-entropy tracking in both Python and Julia workflows

## Repository Structure

### `python_workflows/core/`

Reusable Python utilities for:

- one-qubit operator application
- two-qubit operator application
- standard gate definitions
- QFT construction
- projective measurement
- entropy calculation
- random-circuit evolution with probabilistic measurement

### `python_workflows/experiments/`

Runnable Python demos:

- `run_unitary_qft_demo.py`
  Demonstrates unitary gate evolution and QFT output.
- `run_measurement_demo.py`
  Demonstrates projective measurement on a Bell state.
- `run_random_circuit_demo.py`
  Demonstrates entropy evolution in a random circuit with probabilistic measurement.

### `julia_kraus_oqs/`

Standalone Julia project for two-qubit open-system dynamics:

- Bell-state preparation
- Kraus channels for loss, gain, and dephasing
- `Z` measurement on qubit 1 and `X` measurement on qubit 2
- stochastic outcome tracking
- entanglement-entropy evolution using MPS / ITensors

### `docs/`

Documentation linking the code directly to CV claims:

- `CV_MAP.md`

## How This Maps to a CV

This repository supports statements such as:

- Built Python and Julia quantum simulation workflows, including a Julia MPS/ITensors simulator for two-qubit open-system dynamics.
- Implemented unitary gate evolution, QFT circuits, projective measurement, and Kraus-operator-based generalized measurement channels.
- Simulated stochastic decoherence trajectories and tracked entanglement entropy under measurement and dephasing.

The exact mapping from each claim to source files is documented in `docs/CV_MAP.md`.

## Run

### Python setup

From the repository root:

```powershell
python -m pip install -r requirements.txt
```

### Python demos

```powershell
python -m python_workflows.experiments.run_unitary_qft_demo
python -m python_workflows.experiments.run_measurement_demo
python -m python_workflows.experiments.run_random_circuit_demo
```

### Julia setup

```powershell
julia --project=julia_kraus_oqs -e "import Pkg; Pkg.instantiate()"
```

### Julia open-system simulation

```powershell
julia --project=julia_kraus_oqs julia_kraus_oqs/example_run.jl
```

## Suggested Reading Order

If you are viewing this repository for the first time:

1. start with `python_workflows/experiments/run_unitary_qft_demo.py`
2. look at `python_workflows/experiments/run_measurement_demo.py`
3. inspect `python_workflows/experiments/run_random_circuit_demo.py`
4. then move to `julia_kraus_oqs/example_run.jl`
5. for the main Julia logic, read `julia_kraus_oqs/src/Krauss_protocol.jl`

## Technical Highlights

- Python
- Julia
- NumPy
- ITensors / ITensorMPS
- tensor networks / matrix product states
- open quantum systems
- Kraus operators
- QFT
- projective and generalized measurement
- entanglement entropy

## Future Improvements

- add saved figures and example output plots
- add tests for the Python workflows
- add parameter-sweep scripts for the Julia Kraus simulator
- add a cleaner comparison notebook between Python and Julia workflows

## Short Project Description

Portfolio of Python and Julia quantum simulations covering gate-based circuit evolution, QFT, measurement, entropy analysis, and two-qubit open-system Kraus dynamics with tensor-network methods.
