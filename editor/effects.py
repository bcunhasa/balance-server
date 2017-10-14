from django.conf import settings

import cv2 as cv
import numpy as np

def rgb_to_gray():
    image = cv.imread(settings.MEDIA_ROOT + '/images/lena.bmp', cv.IMREAD_GRAYSCALE)
    cv2.imwrite('output.bmp', img)
    path = ""
    return path
