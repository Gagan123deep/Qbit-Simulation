using LinearAlgebra

const H = (1 / sqrt(2)) * [1 1; 1 -1]

export loss_gain_dephase, ZMeasure, XMeasure

"""
    loss_gain_dephase(g1, g2, g3, dt)

Construct Kraus operators for loss, gain, and dephasing on one qubit.
"""
function loss_gain_dephase(g1, g2, g3, dt)
    I2 = Matrix{Float64}(I, 2, 2)
    K1 = sqrt(g1 * dt) * [0 1; 0 0]
    K2 = sqrt(g2 * dt) * [0 0; 1 0]
    K3 = sqrt(g3 * dt) * [1 0; 0 -1]
    K4 = I2 - 0.5 * (K1' * K1 + K2' * K2 + K3' * K3)
    return normalize_kraus_list([K1, K2, K3, K4])
end

"""
    ZMeasure(g, dt)

Construct a weak Z-basis measurement channel.
"""
function ZMeasure(g, dt)
    I2 = Matrix{Float64}(I, 2, 2)
    K1 = sqrt(g * dt) * [1 0; 0 0]
    K2 = sqrt(g * dt) * [0 0; 0 1]
    K3 = I2 - 0.5 * (K1' * K1 + K2' * K2)
    return normalize_kraus_list([K1, K2, K3])
end

"""
    XMeasure(g, dt)

Construct a weak X-basis measurement channel by rotating the Z channel.
"""
function XMeasure(g, dt)
    return normalize_kraus_list([H * K * H for K in ZMeasure(g, dt)])
end
