import cv2 as cv
import numpy as np

img = cv.imread('assets/group 2.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')


faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

print(f"No. of faces found are {len(faces_rect)}")

for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0),thickness= 2)

cv.imshow('Detected faces', img)

cv.waitKey(0)
cv.destroyAllWindows()