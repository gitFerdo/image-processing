import cv2 as cv

img = cv.imread('Images/image_3.jpg')
cv.imshow('Image', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur Image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade in the Image
# canny = cv.Canny(img, 125, 125)
canny = cv.Canny(blur, 125, 125)
cv.imshow('Edge Cascade', canny)

cv.waitKey(0)