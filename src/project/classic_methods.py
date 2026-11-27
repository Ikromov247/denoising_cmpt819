import numpy as np
import cv2


def mean_filtering(img:np.ndarray, sigma:int):
    """
    Perform mean filtering on img using sigma * sigma shape filter 
    Args:
        img: Input image to be blurred
        sigma: Filter size
    Returns:
        Denoised image
    """
    return cv2.blur(img, (sigma, sigma))

def bilateral_filterting(img:np.ndarray, sigma_color:int, sigma_space:int):
    """
    Perform bilateral filtering on img. For sigma_color, a good value to start is noise sigma or higher. 
    Args:
        img: Input image to be blurred
        sigma_color: Weight to color intensity difference. Larger=more different colors considered 
        sigma_space: Size of domain used in filtering. Larger=wider neighborhood used
    Returns:
        Denosied image
    """
    return cv2.bilateralFilter(
        img, 
        sigmaColor=sigma_color,
        sigmaSpace=sigma_space
    )