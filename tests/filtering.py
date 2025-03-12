# filtering.py

import numpy as np
import scipy.ndimage as ndimage

def apply_gaussian_filter(image, sigma=1.0):
    """Applies a Gaussian filter to smooth the image."""
    return ndimage.gaussian_filter(image, sigma=sigma)

def apply_median_filter(image, size=3):
    """Applies a median filter to reduce noise."""
    return ndimage.median_filter(image, size=size)

if __name__ == "__main__":
    # Example usage
    sample_image = np.random.rand(256, 256)
    smoothed_image = apply_gaussian_filter(sample_image, sigma=2.0)
    denoised_image = apply_median_filter(sample_image, size=5)
    
    print("Filtering applied successfully.")

