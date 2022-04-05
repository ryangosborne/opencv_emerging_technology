import cv2 as cv

img = cv.imread('../resources/photos/park.jpg')
cv.imshow('Boston', img)

# converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blurring an image (removing noise)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175) # doing operation to blur
cv.imshow('Canny', canny)

# dilating the image
dilated = cv.dilate(canny, (10,10), iterations=2)
cv.imshow('Dilation', dilated)

# eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# resize image (does not care about aspect ratio) INTER_AREA good for shrinking, INTER_CUBIC good for making larger
resize = cv.resize(gray, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resize)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)