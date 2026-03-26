from python_workflows.core import random_circuit


def main():
    nqubits = 4
    nsteps = 24
    measurement_probability = 0.2

    entropies = random_circuit.random_state(
        N=nqubits,
        nsteps=nsteps,
        measurement_probability=measurement_probability,
    )

    print("Random circuit entropy trajectory")
    print("N =", nqubits)
    print("nsteps =", nsteps)
    print("measurement_probability =", measurement_probability)
    print("entropies =", entropies.tolist())


if __name__ == "__main__":
    main()
