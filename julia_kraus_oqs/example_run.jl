import Pkg
Pkg.activate(@__DIR__)

using DelimitedFiles
using Plots

include(joinpath(@__DIR__, "src", "KrausSimulation.jl"))

output_dir = joinpath(@__DIR__, "..", "figures", "julia")
mkpath(output_dir)

params = KrausSimulation.SimulationParams(
    N=2,
    g_loss=0.0,
    g_gain=0.1,
    g_dephase=0.1,
    g_meas=0.1,
    dt=0.1,
    nsteps=150,
    show_plot=false,
    print_states=false,
)

result = KrausSimulation.run_protocol(params)

steps = collect(1:params.nsteps)
entropy_plot = plot(steps, result.entropies, lw=2, label="Entropy", xlabel="Step", ylabel="Entropy")
savefig(entropy_plot, joinpath(output_dir, "kraus_entropy.png"))
writedlm(
    joinpath(output_dir, "kraus_entropy.csv"),
    hcat(steps, result.entropies),
    ',',
)

println("Raw Kraus indices:")
println(result.raw_outcomes)
println("Physical measurement outcomes (+1, -1, 0 for no-jump):")
println(result.measurement_outcomes)
println("Entropies: ", result.entropies)
println("Saved entropy plot to ", joinpath(output_dir, "kraus_entropy.png"))
println("Saved entropy data to ", joinpath(output_dir, "kraus_entropy.csv"))
KrausSimulation.visualize_state(KrausSimulation.psi_MPS_to_vec(result.final_state), params.N)
