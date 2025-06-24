import cv2 as cv
import numpy as np


img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
blank = np.zeros(img.shape, dtype=np.uint8)
cv.imshow('blank', blank)
cv.imshow('original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)
ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours in the image.')

# Drawing Contours

blank = cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Countous Drawn',blank)


cv.waitKey(0)
cv.destroyAllWindows()