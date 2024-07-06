import cv2 as cv

# read images
# img = cv.imread('Images/image_1_resize.jpeg')
# cv.imshow('Image', img)

# cv.waitKey(0)

# read videos
capture = cv.VideoCapture('Videos/video_1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # stop playing video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()