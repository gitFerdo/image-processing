import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image from certain color
# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

# Color certain portions of the image
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red', blank)

cv.waitKey(0)