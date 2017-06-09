import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while(1):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 5, 5), 5)
        roiGray = gray[y:y+h, x:x+w]
        roiColor = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roiGray)
        print(eyes)
        for(ex, ey, ew, eh) in eyes:
            cv2.circle(roiColor, (ex, ey), 50, (0, 0, 0), -1)

    cv2.imshow("img", img)
    k = cv2.waitKey(20) & 0xff
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()