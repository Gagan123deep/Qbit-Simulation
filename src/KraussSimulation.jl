module KraussSimulation

using ITensors
using ITensorMPS
using LinearAlgebra
using Plots

include("normalized_krauss.jl")
include("Krauss_list.jl")
include("Operating_Krauss.jl")
include("Krauss_entropy.jl")
include("Tensors_to_matrices.jl")
include("Krauss_protocol.jl")

export normalize_kraus_list
export loss_gain_dephase, ZMeasure, XMeasure
export apply_kraus
export entanglement_entropy
export psi_MPS_to_vec, visualize_state
export SimulationParams, SimulationResult, build_channels, run_protocol, protocol, prepare_bell_state

end
