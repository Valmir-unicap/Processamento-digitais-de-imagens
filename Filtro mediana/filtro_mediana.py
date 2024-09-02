import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
import sys

# O código a seguir mostra como aplicar o filtro da mediana usando open cv

def main():

    img = cv.imread('/content/lena.png')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27: #esc
            break

        medianBlur = cv.medianBlur(img, 3)

        # Mostrando a imagem
        print("Imagem Original")      
        cv2_imshow(img)
        print("Imagem Median blur")
        cv2_imshow(medianBlur)

        # Fazendo a operação em loop
        for i in range(2):
            medianBlur = cv.medianBlur(medianBlur, 3)
            print("Imagem Median blur com operações")
            cv2_imshow(medianBlur)

        break

if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
