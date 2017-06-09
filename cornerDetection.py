#SHI-THOMAS CORNER DETECTION

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("corner.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.goodFeaturesToTrack(gray, 10, .001, 10)
corner1 = np.int0(corner)
#print(corner)

for corner in corner1:
    x, y = corner.ravel()
    cv2.rectangle(img, (x, y), (x + 3, y + 3), (255, 255,0), -1)

plt.imshow(img)
plt.show()