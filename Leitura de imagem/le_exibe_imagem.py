import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow

def main():
    import sys
    img = cv.imread("/content/lena.png")
    
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27:
            break
        cv2_imshow(img)
        
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
