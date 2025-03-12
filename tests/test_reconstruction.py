# test_reconstruction.py

import unittest
import numpy as np
from openrbyr.reconstruction import MARTReconstruction

class TestMARTReconstruction(unittest.TestCase):
    def setUp(self):
        self.reconstructor = MARTReconstruction(num_iterations=5)
        self.fake_projections = np.random.rand(50, 50)

    def test_reconstruct(self):
        reconstructed_image = self.reconstructor.reconstruct(self.fake_projections)
        self.assertEqual(reconstructed_image.shape, (50, 50))
        self.assertTrue(np.all(reconstructed_image >= 0))

    def test_visualize_reconstruction(self):
        reconstructed_image = self.reconstructor.reconstruct(self.fake_projections)
        try:
            self.reconstructor.visualize_reconstruction(reconstructed_image)
        except Exception as e:
            self.fail(f"Visualization failed with error: {e}")

if __name__ == '__main__':
    unittest.main()

