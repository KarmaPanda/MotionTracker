import cv2
import numpy as np

# http://docs.opencv.org/master/db/df8/tutorial_py_meanshift.html

cap = cv2.VideoCapture(1)

# take first frame of the video
ret, frame = cap.read()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # sets up face detection
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('HaarCascade/parojos.xml')
    faces = face_cascade.detectMultiScale(grayFrame, 1.3, 5)

    roi = None
    roi_gray = None

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi = frame[y:y+h, x:x+w]
        roi_gray = grayFrame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    #  hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    #  mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    #  roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv2.imshow("Frame", frame)

    keyInput = chr(cv2.waitKey(1) & 0xFF)
    if keyInput == 'q':
        break

cv2.destroyAllWindows()
'''

# starts to process video feed
while True:
    ret, frame = cap.read()
    editedFrame = frame.copy()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

'''
