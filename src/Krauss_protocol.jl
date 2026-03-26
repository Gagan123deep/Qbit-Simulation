using ITensors
using ITensorMPS
using Plots

export SimulationParams, SimulationResult, build_channels, run_protocol, protocol, prepare_bell_state

Base.@kwdef struct SimulationParams
    N::Int = 2
    g_loss::Float64 = 0.0
    g_gain::Float64 = 0.1
    g_dephase::Float64 = 0.1
    g_meas::Float64 = 0.1
    dt::Float64 = 0.1
    nsteps::Int = 4
    show_plot::Bool = true
    print_states::Bool = false
end

struct SimulationResult
    params::SimulationParams
    final_state
    entropies::Vector{Float64}
    loss_raw_outcomes::Matrix{Int}
    raw_outcomes::Matrix{Int}
    measurement_outcomes::Matrix{Int}
    state_history::Vector{Vector{ComplexF64}}
end

measurement_label(outcome_index::Int) = outcome_index == 1 ? 1 : (outcome_index == 2 ? -1 : 0)

function validate_params(params::SimulationParams)
    params.N == 2 || error("This version is set back to the 2-qubit workflow. Use N = 2.")
    params.nsteps >= 1 || error("nsteps must be at least 1.")
    params.dt > 0 || error("dt must be positive.")
end

function build_channels(params::SimulationParams)
    loss_ops = loss_gain_dephase(params.g_loss, params.g_gain, params.g_dephase, params.dt)
    z_measure = ZMeasure(params.g_meas, params.dt)
    x_measure = XMeasure(params.g_meas, params.dt)
    return loss_ops, z_measure, x_measure
end

function prepare_bell_state(sites)
    length(sites) >= 2 || error("prepare_bell_state requires at least two qubits.")

    psi = productMPS(sites, "0")
    H1 = (1 / sqrt(2)) * [1 1; 1 -1]
    cnot = [1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0]

    psi = apply(op(H1, sites[1]), psi)
    psi = apply(op(cnot, sites[2], sites[1]), psi)
    return normalize!(psi)
end

function protocol(psi, sites, loss_ops, z_measure, x_measure, N, nsteps; show_plot=true, print_states=true)
    entropies = zeros(Float64, nsteps)
    loss_raw_outcomes = Matrix{Int}(undef, 2, nsteps)
    raw_outcomes = Matrix{Int}(undef, 2, nsteps)
    measurement_outcomes = Matrix{Int}(undef, 2, nsteps)
    state_history = Vector{Vector{ComplexF64}}(undef, nsteps)

    for i in 1:nsteps
        psi1, loss_outcome1 = apply_kraus(loss_ops, psi, sites, 1)
        psi2, loss_outcome2 = apply_kraus(loss_ops, psi1, sites, 2)
        psi3, raw_outcome1 = apply_kraus(z_measure, psi2, sites, 1)
        psi4, raw_outcome2 = apply_kraus(x_measure, psi3, sites, 2)

        loss_raw_outcomes[1, i] = loss_outcome1
        loss_raw_outcomes[2, i] = loss_outcome2
        measurement_outcomes[1, i] = measurement_label(raw_outcome1)
        measurement_outcomes[2, i] = measurement_label(raw_outcome2)
        raw_outcomes[1, i] = raw_outcome1
        raw_outcomes[2, i] = raw_outcome2
        entropies[i] = entanglement_entropy(N, psi4)
        state_history[i] = ComplexF64.(psi_MPS_to_vec(psi4))

        if print_states
            println("Step $i: outcomes = ($(measurement_outcomes[1, i]), $(measurement_outcomes[2, i])), entropy = $(entropies[i])")
            visualize_state(state_history[i], N)
        end

        psi = psi4
    end

    if show_plot
        steps = 1:nsteps
        plt = plot(layout=(2, 1), size=(800, 600))
        plot!(plt[1], steps, vec(measurement_outcomes[1, :]), label="Outcome 1", lw=2)
        plot!(plt[1], steps, vec(measurement_outcomes[2, :]), label="Outcome 2", lw=2)
        ylims!(plt[1], (-1.1, 1.1))
        plot!(plt[2], steps, entropies, label="Entropy", lw=2)
        display(plt)
    end

    return psi, entropies, loss_raw_outcomes, raw_outcomes, measurement_outcomes, state_history
end

function run_protocol(params::SimulationParams; psi0=nothing, show_plot=params.show_plot, print_states=params.print_states)
    validate_params(params)

    sites = siteinds("Qubit", params.N)
    psi = isnothing(psi0) ? prepare_bell_state(sites) : psi0
    loss_ops, z_measure, x_measure = build_channels(params)

    psi_final, entropies, loss_raw_outcomes, raw_outcomes, measurement_outcomes, state_history = protocol(
        psi,
        sites,
        loss_ops,
        z_measure,
        x_measure,
        params.N,
        params.nsteps;
        show_plot=show_plot,
        print_states=print_states,
    )

    return SimulationResult(
        params,
        psi_final,
        entropies,
        loss_raw_outcomes,
        raw_outcomes,
        measurement_outcomes,
        state_history,
    )
end
