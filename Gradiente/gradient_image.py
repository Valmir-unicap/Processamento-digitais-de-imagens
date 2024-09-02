import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
import sys

# O código a seguir mostra como aplicar filtros de realce usando open cv
# Leitura da imagem e conversão para monocromática

img = cv.imread("/content/lena.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

while True:
    ch = cv.waitKey()
    if ch == 27:
        sys.exit()
        
    # Gradiente normal
    
    kernel_x = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, -1, 0]])
    
    kernel_y = np.array([[0, 0, 0],
                         [0, 1, -1],
                         [0, 0, 0]])
    
    grad_x = cv.filter2D(gray, -1, kernel_x)
    grad_y = cv.filter2D(gray, -1, kernel_y)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    gray = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv2_imshow(gray)

    print("Imagem com gradiente normal")
    
    # Gradiente de Roberts
    
    kernel_x = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, -1]])
    
    kernel_y = np.array([[0, 0, 0],
                         [0, 0, 1],
                         [0, -1, 0]])
    
    grad_x = cv.filter2D(gray2, -1, kernel_x)
    grad_y = cv.filter2D(gray2, -1, kernel_y)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    gray2 = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv2_imshow(gray2)

    print("Imagem com gradiente de Roberts")
    
    # Gradiente de Sobel
    
    ddepth = cv.CV_16S
    
    grad_x = cv.Sobel(gray3, ddepth, 1, 0, ksize=3, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray3, ddepth, 0, 1, ksize=3, borderType=cv.BORDER_DEFAULT)
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    cv2_imshow(grad)

    print("Imagem com gradiente de Sobel")

    break
