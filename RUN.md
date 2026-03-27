# Run Guide

## Command line

From the project root:

```powershell
julia --project=. -e "import Pkg; Pkg.instantiate()"
julia --project=. example_run.jl
```

## Notebook

Open:

- `notebooks/Program_for_OQS_sim.ipynb`

Then run the cells in order.

## Main parameters

Edit `example_run.jl` if you want to change:

- `g_loss`
- `g_gain`
- `g_dephase`
- `g_meas`
- `dt`
- `nsteps`

This public version is intentionally kept at the 2-qubit level:

- qubit 1: `Z` measurement
- qubit 2: `X` measurement
