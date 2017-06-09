import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    cv2.imshow('frame1',frame)
    k = cv2.waitKey(30) & 0xff
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()