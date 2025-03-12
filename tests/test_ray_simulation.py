# test_ray_simulation.py

import unittest
import numpy as np
from openrbyr.ray_simulation import RaySimulation

class TestRaySimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = RaySimulation(num_rays=10, detector_distance=50)

    def test_simulate_rays(self):
        rays = self.simulation.simulate_rays()
        self.assertEqual(len(rays), 10)
        self.assertTrue(all(isinstance(ray, tuple) for ray in rays))

    def test_visualize_rays(self):
        rays = self.simulation.simulate_rays()
        try:
            self.simulation.visualize_rays(rays)
        except Exception as e:
            self.fail(f"Visualization failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
