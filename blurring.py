import cv2 as cv
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 

cv.imshow('Image', img)

# Average_Blurring
avg = cv.blur(img, (7,7))
cv.imshow('Avg', avg)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 5, 20, 20)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()
