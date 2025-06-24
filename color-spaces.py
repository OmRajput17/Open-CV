import cv2 as cv
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

cv.imshow('original', img)

# BGR to Gray

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


cv.waitKey(0)
cv.destroyAllWindows()