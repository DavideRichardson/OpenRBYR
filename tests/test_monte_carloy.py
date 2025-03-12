# test_monte_carlo.py

import unittest
import numpy as np
from openrbyr.monte_carlo import MonteCarloSimulation

class TestMonteCarloSimulation(unittest.TestCase):
    def setUp(self):
        self.simulation = MonteCarloSimulation(num_particles=1000, detector_distance=50)

    def test_run_simulation(self):
        interactions = self.simulation.run_simulation()
        self.assertEqual(interactions.shape, (1000, 2))

    def test_analyze_results(self):
        interactions = self.simulation.run_simulation()
        results = self.simulation.analyze_results(interactions)
        self.assertIn("total_particles", results)
        self.assertIn("absorbed_ratio", results)

if __name__ == '__main__':
    unittest.main()

