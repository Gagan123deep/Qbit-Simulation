using LinearAlgebra

export normalize_kraus_list

"""
    normalize_kraus_list(Klist::Vector{<:AbstractMatrix}) -> Vector{Matrix}

Normalize a list of Kraus operators so that `sum(K' * K for K in Klist)` is the
identity up to numerical tolerance.
"""
function normalize_kraus_list(Klist::Vector{<:AbstractMatrix})
    S = zeros(eltype(Klist[1]), size(Klist[1])...)
    for K in Klist
        S += K' * K
    end

    vals, vecs = eigen(Hermitian(S))
    if minimum(vals) < 1e-12
        @warn "Small eigenvalues encountered during normalization; result may be unstable."
    end

    Sinv_sqrt = vecs * Diagonal(1.0 ./ sqrt.(clamp.(vals, 1e-14, Inf))) * vecs'
    return [Matrix(K * Sinv_sqrt) for K in Klist]
end
