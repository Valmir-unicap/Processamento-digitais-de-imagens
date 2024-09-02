import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
import sys

# O código a seguir mostra como aplicar o filtro da média usando open cv

def main():
    
    img = cv.imread('/content/lena.png')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27: #esc
            break

        averageBlur = cv.blur(img, (3, 3)) 
  
        # Mostrando a imagem 
        print("Imagem Original")
        cv2_imshow(img)
        print("Imagem Average blur")
        cv2_imshow(averageBlur) 

        # Aplicando o filtro da média em loop
        for i in range(2):
            averageBlur = cv.blur(averageBlur, (3, 3))
            print("Imagem Average blur")
            cv2_imshow(averageBlur)

        break

if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
