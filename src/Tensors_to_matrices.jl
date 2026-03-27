using ITensors
using ITensorMPS

export psi_MPS_to_vec, visualize_state

"""
    psi_MPS_to_vec(psi)

Contract an MPS into a full state vector.
"""
function psi_MPS_to_vec(psi)
    psi_full = reduce(*, psi)
    return vec(Array(psi_full, siteinds(psi)))
end

"""
    visualize_state(state::AbstractVector, N::Int)

Print the nonzero amplitudes of a state vector in the computational basis.
"""
function visualize_state(state::AbstractVector, N::Int)
    first_print = true
    for (i, c) in pairs(state)
        abs(c) < 1e-12 && continue
        bitstring = reverse(lpad(string(i - 1, base=2), N, '0'))
        coeff_str = round(c, digits=14)
        if first_print
            println("  ", coeff_str, " |$bitstring>")
            first_print = false
        else
            println("+ ", coeff_str, " |$bitstring>")
        end
    end
end
