import cv2 as cv

img = cv.imread('Images/image_1.jpeg')
cv.imshow('Image', img)
cv.waitKey(0)