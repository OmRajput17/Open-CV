import cv2 as cv

img = cv.imread('assets/logo.jpg')

# Edge Cascade
img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
cv.imshow('image', img)

# Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BLurr
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('VBLur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#  Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('Dilated', dilated)

# Eroding

eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Erode', eroded)

cv.waitKey(0)
cv.destroyAllWindows()