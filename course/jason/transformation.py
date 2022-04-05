import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/park.jpg')
cv.imshow('Boston', img)

# translation (shifting image)
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0]) # shape[1] is width, shape[0] is height
    return cv.warpAffine(img, transMat, dimensions)

# negative x values will move to left, negative y values will move up
# positive x values will move to right, positive y values will move down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)