import cv2 as cv

# img = cv.imread('Images/image_1_resize.jpeg')
# cv.imshow('img', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# read videos
capture = cv.VideoCapture('Videos/video_1.mp4')

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