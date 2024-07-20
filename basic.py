import cv2 as cv

img = cv.imread('Images/image_3.jpg')
cv.imshow('Image', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)