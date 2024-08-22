import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
import sys

# O código a seguir mostra como fazer transformações básicas em uma imagem usando open cv
# Leitura da imagem e conversão para monocromática

img = cv.imread("/content/lena.png")
assert img is not None, 'Não consegui achar a imagem'
img = cv.resize(src=img, dsize=None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

while True:
    ch = cv.waitKey()
    if ch == 27:
        sys.exit()
    
    # Comandos de rotacionar
        
    flipped_img_horizontally = cv.flip(img, 0)
    flipped_img_vertically = cv.flip(img, 1)

    cv2_imshow(img)
    cv2_imshow(flipped_img_horizontally)
    cv2_imshow(flipped_img_vertically)    

    # Redimensionamento

    resized_img = cv.resize(src=img, dsize=None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

    cv2_imshow(resized_img)

    # Translação

    o_heigth, o_width = img.shape[:2]
    o_dim = (o_width, o_heigth)

    matriz = np.float64(([1,0,100],[0,1,50]))

    tranlated_img = cv.warpAffine(img, matriz, o_dim)

    cv2_imshow(tranlated_img)

    # Rotação

    escala = 1
    centro = (o_width / 2, o_heigth / 2)

    rotate_matriz = cv.getRotationMatrix2D(centro, 45, 0.8)
    rotate_img = cv.warpAffine(img, rotate_matriz, o_dim)

    cv2_imshow(rotate_img)
