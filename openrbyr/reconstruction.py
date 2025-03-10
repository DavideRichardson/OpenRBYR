# reconstruction.py

import numpy as np
import matplotlib.pyplot as plt

class MARTReconstruction:
    def __init__(self, num_iterations=10):
        self.num_iterations = num_iterations

    def reconstruct(self, projections):
        """Performs a basic MART-like iterative reconstruction."""
        reconstructed_image = np.ones_like(projections)
        for _ in range(self.num_iterations):
            reconstructed_image *= projections / (np.sum(reconstructed_image, axis=0) + 1e-8)
        return reconstructed_image

    def visualize_reconstruction(self, image):
        plt.imshow(image, cmap='gray')
        plt.title("Reconstructed Image")
        plt.colorbar()
        plt.show()

if __name__ == "__main__":
    fake_projections = np.random.rand(50, 50)
    recon = MARTReconstruction()
    reconstructed = recon.reconstruct(fake_projections)
    recon.visualize_reconstruction(reconstructed)
