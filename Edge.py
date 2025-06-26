# Importing libraries
import cv2 as cv
import numpy as np

# Reading File
img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian 
lap = cv.Laplacian(gray, cv.CV_64F )
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.waitKey(0)
cv.destroyAllWindows()
