import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image from certain color
# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

# Color certain portions of the image
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red', blank)

# Draw a Rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)