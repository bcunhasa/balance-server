import cv2 as cv
import numpy as np

def create_new_image(height, width):
    """Create a new image with the passed informations"""
    image = np.empty((height, width, 3), np.uint8)
    image[:] = 255
    return image

def light_corrector(image):
    """Create a greyscale image"""
    
    n = 0 # Primeira coluna; número de tons de cinza
    pr = 1 # Segunda coluna; normalização
    freq = 2 # Terceira coluna; cálculo da soma normalizada
    eq = 3 # Quarta coluna; look-up table
    r = 4 # Quinta coluna; imagem de saída
    
    # Start the table with zeros
    table = []
    print(type(table))
    for i in range(256):
        # num, normalização, soma normalizada, lut, saída
        table.append([[0, 0.0, 0.0, 0.0, 0], [0, 0.0, 0.0, 0.0, 0], [0, 0.0, 0.0, 0.0, 0]])

    # Calcula o número total de cada tom de cinza na imagem
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            table[image[i, j][0]][0][n] += 1
            table[image[i, j][1]][1][n] += 1
            table[image[i, j][2]][2][n] += 1

    # Normalização dos valores
    for i in range(len(table)):
        table[i][0][pr] = float(table[i][0][n] / (image.shape[0] * image.shape[1]))
        table[i][1][pr] = float(table[i][1][n] / (image.shape[0] * image.shape[1]))
        table[i][2][pr] = float(table[i][2][n] / (image.shape[0] * image.shape[1]))

    # Create a look-up table
    for i in range(len(table)):
        table[i][0][eq] = table[i][0][pr] * 255
        table[i][1][eq] = table[i][1][pr] * 255
        table[i][2][eq] = table[i][2][pr] * 255
        if i > 0:
            table[i][0][eq] = table[i - 1][0][eq] + (table[i][0][pr] * 255)
            table[i][1][eq] = table[i - 1][1][eq] + (table[i][1][pr] * 255)
            table[i][2][eq] = table[i - 1][2][eq] + (table[i][2][pr] * 255)

    # Arredonda os valores finais para gerar a imagem de saída
    for i in range(len(table)):
        table[i][0][r] = int(table[i][0][eq])
        table[i][1][r] = int(table[i][1][eq])
        table[i][2][r] = int(table[i][2][eq])
    
    new_image = create_new_image(image.shape[0], image.shape[1])
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_image[i, j][0] = int(table[image[i, j][0]][0][r])
            new_image[i, j][1] = int(table[image[i, j][1]][1][r])
            new_image[i, j][2] = int(table[image[i, j][2]][2][r])

    return new_image
