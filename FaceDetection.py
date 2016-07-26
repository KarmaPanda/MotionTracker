import cv2
import numpy as np

# Variables
face_cascade = cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('HaarCascade/parojos.xml')


def detectface(cap):
    ret, frame = cap.read()

    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayframe, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi = frame[y:y+h, x:x+w]
            roi_gray = grayframe[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        return frame
    else:
        return None