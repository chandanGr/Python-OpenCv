import cv2
import numpy as np

e1 = cv2.getTickCount()

img1 = cv2.imread("oneq.jpg", 1)
img2 = cv2.imread("logo.png", 1)
r, c, ch = img2.shape
roi = img1[0:r, 0:c]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 40, 255, cv2.THRESH_BINARY_INV)

img2_bg = cv2.bitwise_and(roi, roi, mask = mask)

dest = cv2.add(img2, img2_bg)
img1[0:r, 0:c] = dest


e1 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

print(time)

cv2.imshow("img1", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
