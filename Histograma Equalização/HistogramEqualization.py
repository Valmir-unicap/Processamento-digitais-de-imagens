from __future__ import print_function
import cv2 as cv
from google.colab.patches import cv2_imshow
import argparse
 
src = cv.imread(cv.samples.findFile('/content/mergulhador.jpg'))
if src is None:
    print('Could not open or find the image:')
    exit(0)
 
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
 
dst = cv.equalizeHist(src)
 
cv2_imshow(src)
cv2_imshow(dst)

cv.waitKey()
