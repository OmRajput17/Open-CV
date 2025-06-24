import cv2 as cv

img = cv.imread('assets/logo.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
cv.imshow('image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('image', gray)

# blur = cv.GaussianBlur(img, (0,0), cv.BORDER_DEFAULT)
# cv.imshow('image', blur)

cv.waitKey(0)
cv.destroyAllWindows()