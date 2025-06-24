import cv2

img = cv2.imread('assets/logo.jpg', )

# Resize the image
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)

# Rotate the image
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# -1 -> For coloured Image
# 0 -> for black and white
# 1 -> loads image as individual alpha channel

# Write the name of the image
cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()