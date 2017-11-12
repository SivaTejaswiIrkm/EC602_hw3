import cv2
import numpy as np

image = cv2.imread('Lenna.png')
print(image[20, 25])
b,g,r = cv2.split(image)

cv2.imwrite('b_part.jpg', b)
cv2.imwrite('g_part.jpg', g)
cv2.imwrite('r_part.jpg', r)

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

# Convert RGB to HSV
hsv_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
print(hsv_image[20, 25])
h,s,v = cv2.split(hsv_image)

cv2.imwrite('hue.jpg', h)
cv2.imwrite('saturation.jpg', s)
cv2.imwrite('value.jpg', v)

cv2.imshow('hue', h)
cv2.imshow('saturation', s)
cv2.imshow('value', v)

#Convert RGB to Ycrcb
ycrcb_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
print(ycrcb_image[20, 25])
y,cr,cb = cv2.split(ycrcb_image)

cv2.imwrite('Y.jpg', y)
cv2.imwrite('Cr.jpg', cr)
cv2.imwrite('Cb.jpg', cb)

cv2.imshow('Y', y)
cv2.imshow('Cr', cr)
cv2.imshow('Cb', cb)

cv2.waitKey(0)
cv2.destroyAllWindows()