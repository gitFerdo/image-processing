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
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)

# Filling a Rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(blank, (0, 0), ((blank.shape[1]//2), (blank.shape[0]//2)), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# Draw a Circle
# cv.circle(blank, (250, 250), 40, (255, 0, 0), thickness=3)
cv.circle(blank, (250, 250), 40, (255, 0, 0), thickness=-1)
cv.imshow('Circle', blank)

# Draw a Line
# cv.line(blank, (0, 0), (250, 250), (0, 0, 255), thickness=4)
cv.line(blank, (100, 250), (300, 400), (0, 0, 255), thickness=1)
cv.imshow('Line', blank)

cv.waitKey(0)