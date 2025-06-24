import cv2 as cv
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
cv.imshow('Original', img)

"""
-x -> Left
-y -> Up
x -> Right
y -> Down
"""
#  Translation
def translation(img, x, y):
    transMat = np.float32([[1,0,x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


# Rotation
def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (height//2, width//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotatation = rotate(img, 45)
cv.imshow("Rotated", rotatation)


translates = translation(img, -100, -100)
cv.imshow('Translated', translates)

cv.waitKey(0)
cv.destroyAllWindows()