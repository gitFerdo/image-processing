import cv2 as cv
import numpy as np

blank = np.zeros((500, 500), dtype='uint8')
cv.imshow('Blank', blank)

img = cv.imread('Images/image_2.jpg')
cv.imshow('Image', img)

cv.waitKey(0)