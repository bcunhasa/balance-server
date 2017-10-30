import cv2 as cv
import numpy as np

def grayscale(image):
    """Create a greyscale image"""
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image
