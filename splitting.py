import cv2 as cv
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
cv.imshow('Original',img)

black = np.zeros(img.shape[:2], dtype=np.uint8)

b, g, r = cv.split(img)

blue = cv.merge([b, black, black])
green = cv.merge([black, g, black])
red = cv.merge([black, black, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)
cv.destroyAllWindows()