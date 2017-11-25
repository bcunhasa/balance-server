import cv2 as cv
import numpy as np

def create_new_image(height, width):
    """Create a new image with the passed informations"""
    image = np.empty((height, width, 3), np.uint8)
    image[:] = 255
    return image

def grayscale(image):
    """Create a greyscale image"""
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)
