import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple Thresholding

threshold, thresh = cv.threshold(gray,125, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

threshold, thresh_inv = cv.threshold(gray,95, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inversed", thresh_inv)

#  Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Threshold", adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive Threshold Inversed", adaptive_thresh_inv)

cv.waitKey(0)
cv.destroyAllWindows()