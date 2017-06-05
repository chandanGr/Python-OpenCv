"""
import cv2
import numpy as np

def nothing(x):
    print(x)

img = np.zeros((1000, 1000, 3), np.uint8)*255
cv2.namedWindow("image")

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
switch = "0: Off \n 1: On"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while(1):
    cv2.imshow("image", img)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv2.destroyAllWindows()
"""

import numpy as np
import cv2

b, g, r, s, size = -1, -1, -1, -1, -1
ix, iy = -1, -1
drawing = False
mode = True

def nothing(x):
    pass

def drawCircle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                print(b, g, r)
                print(ix, iy, x, y)
                cv2.rectangle(img2, (ix, iy), (x, y), (b, g, r), 20)
            else:
                cv2.circle(img2, (x, y), size, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img2, (ix, iy), (x, y), (b, g, r), 2)
        else:
            cv2.circle(img2, (x, y), size, (b, g, r), -1)

img1 = np.zeros((300, 500, 3), np.uint8)
cv2.namedWindow("image")
img2 = np.zeros((800, 1000, 3), np.uint8)
cv2.namedWindow("image1")

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
switch = "1:ON \n    0:Off"
cv2.createTrackbar(switch, "image", 0, 1, nothing)
cv2.createTrackbar("size", "image", 0, 50, nothing)


cv2.setMouseCallback("image1", drawCircle)

while(1):
    cv2.imshow("image", img1)
    cv2.imshow("image1", img2)
    k = cv2.waitKey(2)
    if k == ord("q"):
        break
    elif k == ord("m"):
        mode = not mode
    elif k == ord("c"):
        cv2.rectangle(img2, (0, 0), (1000, 1000), (0, 0, 0), -1)

    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")
    size = cv2.getTrackbarPos("size", "image")

    if s == 0:
        img1[:] = 0
    else:
        img1[:] = [b, g, r]

cv2.destroyAllWindows()






