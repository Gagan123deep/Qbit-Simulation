import Pkg
Pkg.activate(@__DIR__)

using ITensors
using ITensorMPS
using Plots

include(joinpath(@__DIR__, "src", "KraussSimulation.jl"))

params = KraussSimulation.SimulationParams(
    N=2,
    g_loss=0.0,
    g_gain=0.1,
    g_dephase=0.1,
    g_meas=0.1,
    dt=0.1,
    nsteps=150,
    show_plot=true,
    print_states=false,
)

result = KraussSimulation.run_protocol(params)

println("Raw Kraus indices:")
println(result.raw_outcomes)
println("Physical measurement outcomes (+1, -1, 0 for no-jump):")
println(result.measurement_outcomes)
println("Entropies: ", result.entropies)
KraussSimulation.visualize_state(KraussSimulation.psi_MPS_to_vec(result.final_state), params.N)
