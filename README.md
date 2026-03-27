# Python and Julia Quantum Simulation Workflows

Repository containing small quantum-simulation workflows in Python and Julia. The Python side covers state-vector gate evolution, QFT, projective measurement, and random-circuit entropy dynamics. The Julia side implements a 2-qubit open quantum system with Kraus operators, stochastic trajectories, and entanglement-entropy tracking using ITensors / ITensorMPS.

This repository is organized to match three core project themes:

- Python and Julia quantum simulation workflows
- unitary gates, QFT circuits, and measurement channels
- stochastic decoherence trajectories and entanglement tracking

## Overview

- a **Python state-vector toolkit** for gate-based circuit evolution, Quantum Fourier Transform (QFT), projective measurement, entropy calculation, and random-circuit experiments
- a **Julia open-quantum-system simulator** using `ITensors` / `ITensorMPS` to model two-qubit Kraus dynamics with loss, gain, dephasing, and measurement

Together, these workflows provide a compact codebase for coursework, research applications, and CV use.

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
- a notebook entry point in `julia_kraus_oqs/notebooks/Program_for_OQS_sim.ipynb`

## Installation

### Python

From the repository root:

```powershell
python -m pip install -r requirements.txt
```

### Julia

```powershell
julia --project=julia_kraus_oqs -e "import Pkg; Pkg.instantiate()"
```

## Run

### Python examples

```powershell
python -m python_workflows.experiments.run_unitary_qft_demo
python -m python_workflows.experiments.run_measurement_demo
python -m python_workflows.experiments.run_random_circuit_demo
```

### Julia example

```powershell
julia --project=julia_kraus_oqs julia_kraus_oqs/example_run.jl
```

## Tests

### Python

```powershell
python -m unittest tests.test_python_workflows
```

### Julia

```powershell
julia --project=julia_kraus_oqs julia_kraus_oqs/test/runtests.jl
```

## Example outputs

- `python_workflows/experiments/run_unitary_qft_demo.py` saves a text summary to `figures/python/unitary_qft_demo.txt`
- `python_workflows/experiments/run_measurement_demo.py` saves a text summary to `figures/python/measurement_demo.txt`
- `python_workflows/experiments/run_random_circuit_demo.py` saves:
  - `figures/python/random_circuit_entropy.csv`
  - `figures/python/random_circuit_entropy.png`
- `julia_kraus_oqs/example_run.jl` saves:
  - `figures/julia/kraus_entropy.csv`
  - `figures/julia/kraus_entropy.png`

## What this repo demonstrates

- Python state-vector simulation for unitary gates and simple circuit models
- QFT implementation and a direct comparison with FFT output for a simple input state
- Projective measurement in Z and X bases
- Random-circuit entropy dynamics under probabilistic measurement
- Julia two-qubit open-system simulation with Kraus operators
- ITensors / ITensorMPS usage for a small MPS-based workflow
- Stochastic trajectory tracking and entanglement-entropy calculation

## Scope

- The Python side covers state-vector workflows for gates, QFT, measurement, and entropy experiments.
- The repository does not try to be a general-purpose quantum framework; it is a compact simulation project built around the current coursework.

## Suggested reading order

If you are viewing this repository for the first time:

1. start with `python_workflows/experiments/run_unitary_qft_demo.py`
2. look at `python_workflows/experiments/run_measurement_demo.py`
3. inspect `python_workflows/experiments/run_random_circuit_demo.py`
4. then move to `julia_kraus_oqs/example_run.jl`
5. for the main Julia logic, read `julia_kraus_oqs/src/Kraus_protocol.jl`


