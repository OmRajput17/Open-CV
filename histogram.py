import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('assets/soccer_practice.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 

black = np.zeros(img.shape[:2], dtype=np.uint8)
cv.imshow('blank', black)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

mask = cv.circle(black, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

# # GrayScale histogram
# gray_hist = cv.calcHist([gray],[0], mask, [256],[0, 256])

# plt.figure()
# plt.title("Gray Hist")
# plt.xlabel('Bins')
# plt.ylabel('No. of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Colour Histogram

plt.figure()
plt.title("Gray Hist")
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist,color=col)
    plt.xlim([0, 256])
    
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()