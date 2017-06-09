import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    frame = cap.read()

    hsv = cv2.Color(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([0,50,50])
    upper_blue = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("res", res)
    k = cv2.waitKey(5)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()