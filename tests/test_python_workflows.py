import unittest

import numpy as np

from python_workflows.core import apply_single_qubit, entropy, measurements, qft, single_qubit_gates


class PythonWorkflowTests(unittest.TestCase):
    def test_single_qubit_operator_preserves_shape_and_norm(self):
        state = np.array([1.0, 0.0, 0.0, 0.0], dtype=np.complex128)
        output = apply_single_qubit.Q_Operate(2, 1, state, single_qubit_gates.Hadamard())
        self.assertEqual(output.shape, state.shape)
        self.assertAlmostEqual(np.linalg.norm(output), 1.0, places=12)

    def test_measurement_outputs_are_pm_one(self):
        bell = np.zeros(4, dtype=np.complex128)
        bell[0] = 1 / np.sqrt(2)
        bell[3] = 1 / np.sqrt(2)
        outcome, post = measurements.measure_site(2, 1, bell)
        self.assertIn(outcome, (-1, 1))
        self.assertAlmostEqual(np.linalg.norm(post), 1.0, places=12)

    def test_qft_matches_fft_for_simple_input(self):
        state = np.zeros(4, dtype=np.complex128)
        state[0] = 1 / np.sqrt(2)
        state[1] = 1 / np.sqrt(2)
        circuit = qft.QFT_M_qubits_br(state.copy(), 2)
        reference = np.fft.fft(state, norm="ortho")
        np.testing.assert_allclose(circuit, reference, atol=1e-12)

    def test_entropy_of_product_state_is_zero(self):
        state = np.array([1.0, 0.0, 0.0, 0.0], dtype=np.complex128)
        self.assertAlmostEqual(entropy.entropy(state, 1, 2), 0.0, places=12)


if __name__ == "__main__":
    unittest.main()
