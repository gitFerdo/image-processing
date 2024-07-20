import cv2 as cv

img = cv.imread('Images/image_1.jpeg')
cv.imshow('img', img)

def rescaleFrame(frame, scale=0.75):
    # this methods are only working for Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resize Image', resized_image)

def changeRes(width, height):
    # Only for Live videos
    capture.set(3, width)
    capture.set(5, height)

# read videos
capture = cv.VideoCapture('Videos/video_2.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

     # stop playing video
    if cv.waitKey(20) & 0xFF == ord('d'):
         break

capture.release()
cv.destroyAllWindows()