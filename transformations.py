import cv2 as cv
import numpy as np

img = cv.imread('Images/image_2.jpg')
cv.imshow('Peacock', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# x --> Right & y --> Down
translated = translate(img, 100, 100)
cv.imshow('Translated1', translated)

# -x --> Left & y --> Down
translated = translate(img, -100, 100)
cv.imshow('Translated2', translated)

cv.waitKey(0)