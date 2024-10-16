from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
from google.colab.patches import cv2_imshow
import argparse

## [Load image]

src = cv.imread(cv.samples.findFile('/content/digital.jpg'))

if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
## [Load image]

## [Separate the image in 3 places ( B, G and R )]
bgr_planes = cv.split(src)
## [Separate the image in 3 places ( B, G and R )]

## [Establish the number of bins]
histSize = 256
## [Establish the number of bins]

## [Set the ranges ( for B,G,R) )]
histRange = (0, 256) # the upper boundary is exclusive
## [Set the ranges ( for B,G,R) )]

## [Set histogram param]
accumulate = False
## [Set histogram param]

## [Compute the histograms]
b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
## [Compute the histograms]

## [Draw the histograms for B, G and R]
hist_w = 512
hist_h = 400
bin_w = int(round( hist_w/histSize ))

histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
## [Draw the histograms for B, G and R]

## [Normalize the result to ( 0, histImage.rows )]
cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
## [Normalize the result to ( 0, histImage.rows )]

## [Draw for each channel]
for i in range(1, histSize):
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(b_hist[i-1]) ),
            ( bin_w*(i), hist_h - int(b_hist[i]) ),
            ( 255, 0, 0), thickness=2)
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(g_hist[i-1]) ),
            ( bin_w*(i), hist_h - int(g_hist[i]) ),
            ( 0, 255, 0), thickness=2)
    cv.line(histImage, ( bin_w*(i-1), hist_h - int(r_hist[i-1]) ),
            ( bin_w*(i), hist_h - int(r_hist[i]) ),
            ( 0, 0, 255), thickness=2)
## [Draw for each channel]

## [Display]
cv2_imshow(src)
cv2_imshow(histImage)

_, dst = cv.threshold(src, 130, 255, cv.THRESH_BINARY_INV)
cv2_imshow(dst)
cv.waitKey()
## [Display]
