import cv2 as cv
import numpy as np

# blank image of width and height 500, datatype of uint8 (image) -> 3 for num of colour channels (B, G, R)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. paint the image a certain colour
blank[:] = 0,200,0 # painting everything green
blank[200:300, 300:400] = 0,0,200 # adding red square
cv.imshow('Green', blank)

# 2. draw rectangle (point 1), (point 2, can use shape properties), (color) , thickness of line (use -1 for fill)
cv.rectangle(blank, (100, 50), (blank.shape[1]//2, blank.shape[0]//2),
             (255, 0, 0), thickness=5)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (250, 250), 40, (200, 255, 0), thickness=-1)
cv.imshow('Circle', blank)

# 4. draw a line
cv.line(blank, (45, 100), (120, 400), (200, 200, 200), thickness=3)
cv.imshow('Line', blank)

# 5. write text on image
cv.putText(blank, "Mlepnos", (225, 400), cv.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)