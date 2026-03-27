using ITensors
using ITensorMPS

export entanglement_entropy

function entanglement_entropy(N::Int, psi)
    b = div(N, 2)
    psi2 = orthogonalize(psi, b)
    _, S, _ = svd(psi2[b], linkind(psi2, b), siteind(psi2, b + 1))
    ps = diag(S) .^ 2

    entropy = 0.0
    for p in ps
        if p > 1e-12
            entropy -= p * log(p)
        end
    end

    return entropy
end
