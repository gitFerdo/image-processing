import cv2 as cv

img = cv.imread('Images/image_1_resize.jpeg')
cv.imshow('Image', img)
cv.waitKey(0)