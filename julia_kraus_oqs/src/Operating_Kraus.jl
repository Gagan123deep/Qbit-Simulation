export apply_kraus

function apply_kraus(Klist, psi, sites, pos; cutoff=1e-16, maxdim=200)
    r = rand()
    prob = 0.0

    for k in eachindex(Klist)
        E = Klist[k]' * Klist[k]
        p = expect(psi, E; sites=pos)
        prob += p
        if r <= prob
            op1 = op(Klist[k], sites[pos])
            psi_new = apply(op1, psi; cutoff=cutoff, maxdim=maxdim)
            return normalize!(psi_new), k
        end
    end

    op1 = op(Klist[end], sites[pos])
    psi_new = apply(op1, psi; cutoff=cutoff, maxdim=maxdim)
    return normalize!(psi_new), length(Klist)
end
