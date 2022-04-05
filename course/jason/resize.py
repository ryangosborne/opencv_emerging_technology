import cv2 as cv


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) # width of image
    height = int(frame.shape[0] * scale) # height of image
    dimensions = (width, height) # creates a tuple of width and height
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # resize video to certain dimension

# Read video
capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    # read a re-sized frame
    frame_resized = rescale_frame(frame, scale=.6)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

