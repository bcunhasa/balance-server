import cv2 as cv
import numpy as np
import math

def create_new_image(width, height):
    """Create a new image with the passed informations"""
    image = np.empty((width, height, 3), np.uint8)
    image[:] = 255
    return image

def is_inside_borders(x, y, width, height):
    """Check if the values of x and y are inside the borders of the image"""
    if (x >= 0 and x < width) and (y >= 0 and y < height):
        return True
    else:
        return False

def rotation(image):
    """Rotate the image"""
    degree = math.radians(90)
    new_image = create_new_image(image.shape[0], image.shape[1])
    
    ponto = [image.shape[0] / 2, image.shape[1] / 2]
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x = int((math.cos(degree) * (i - ponto[0])))
            x += int(-math.sin(degree) * (j - ponto[0]) + ponto[0])
            
            y = int((math.sin(degree) * (i - ponto[1])))
            y += int(math.cos(degree) * (j - ponto[1]) + ponto[1])
            
            if (is_inside_borders(x, y, image.shape[0], image.shape[1])):
                new_image[x, y] = image[i, j]
            
    return new_image
