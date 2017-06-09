import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("feature1.jpg", 1)
img2 = cv2.imread("feature2.jpg", 1)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x : x.queryIdx)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:5], None, flags = 2)

#plt.imshow(img3)
#plt.show()

cv2.imshow("img3", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()