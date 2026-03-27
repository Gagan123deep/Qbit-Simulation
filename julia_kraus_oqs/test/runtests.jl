using Test
using LinearAlgebra
using ITensorMPS

include(joinpath(@__DIR__, "..", "src", "KrausSimulation.jl"))

@testset "KrausSimulation" begin
    channels = KrausSimulation.loss_gain_dephase(0.05, 0.02, 0.03, 0.1)
    channel_sum = zero(channels[1]' * channels[1])
    for op in channels
        channel_sum += op' * op
    end
    @test isapprox(channel_sum, Matrix{Float64}(I, 2, 2), atol=1e-8)

    sites = siteinds("Qubit", 2)
    bell = KrausSimulation.prepare_bell_state(sites)
    @test isapprox(KrausSimulation.entanglement_entropy(2, bell), log(2), atol=1e-6)

    params = KrausSimulation.SimulationParams(nsteps=4, show_plot=false, print_states=false)
    result = KrausSimulation.run_protocol(params)
    @test length(result.entropies) == 4
    @test size(result.measurement_outcomes) == (2, 4)
end
