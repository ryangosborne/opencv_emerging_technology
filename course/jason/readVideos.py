import cv2 as cv

# Captures a video from the
capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    # read a frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

