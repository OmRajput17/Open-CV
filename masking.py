import cv2 as cv
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 

cv.imshow('Image', img)

black = np.zeros(img.shape[:2], dtype=np.uint8)
cv.imshow('blank', black)

mask = cv.circle(black, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked_img', masked_img)

cv.waitKey(0)
cv.destroyAllWindows()