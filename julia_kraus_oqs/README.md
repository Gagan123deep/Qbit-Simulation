# Open Quantum Kraus Simulation

Julia simulation of two-qubit open quantum system dynamics using Kraus operators and tensor-network methods. The project models stochastic loss, gain, dephasing, and measurement channels on a Bell pair, then tracks the resulting trajectory and entanglement entropy.

## Why this project is useful

- Shows open quantum system evolution with Kraus maps rather than closed-system unitary dynamics only.
- Uses `ITensors` / `ITensorMPS`, so the simulation is built around tensor-network ideas instead of a plain brute-force workflow.
- Separates the simulation code into reusable Julia modules, a runnable script, and a notebook entry point.

## Methods

- Initial state: Bell pair on two qubits
- Channels: loss, gain, dephasing, `Z` measurement on qubit 1, `X` measurement on qubit 2
- State representation: matrix product state (MPS)
- Observables: stochastic measurement outcomes and bipartite entanglement entropy

## Repo Layout

- `src/KraussSimulation.jl`: main module entry point
- `src/Krauss_protocol.jl`: protocol loop, state preparation, result tracking
- `src/Krauss_list.jl`: Kraus channel construction
- `src/Operating_Krauss.jl`: single-site Kraus application and outcome sampling
- `src/Krauss_entropy.jl`: entropy helper
- `src/Tensors_to_matrices.jl`: MPS-to-vector conversion and basis-state display
- `example_run.jl`: main script entry point
- `notebooks/Program_for_OQS_sim.ipynb`: notebook version of the workflow

## Run

From this folder:

```powershell
julia --project=. -e "import Pkg; Pkg.instantiate()"
julia --project=. example_run.jl
```

## What the output shows

- Physical measurement outcomes reported as `+1`, `-1`, or `0` for the no-jump branch
- Entanglement entropy over the protocol
- Final state amplitudes in the computational basis

## Technical Highlights

- Julia
- ITensors / ITensorMPS
- Tensor networks / MPS
- Open quantum systems
- Kraus operators
- Scientific computing
- Numerical simulation

## CV-ready summary

If you want to describe this project briefly on a CV:

> Built a Julia simulator for two-qubit open quantum system dynamics using Kraus operators and tensor-network methods (MPS/ITensors), with stochastic measurement channels and entanglement-entropy tracking.
