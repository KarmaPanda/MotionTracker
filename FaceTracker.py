from Dependencies import *

class FaceTracker(object):
    face_cascade = cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('HaarCascade/parojos.xml')
    camera = None
    fileoutput = None
    instance = None

    def __init__(self, camera, instance, fileoutput):
        self.camera = camera
        self.instance = instance
        self.fileoutput = fileoutput

    def detectface(self, frame):
        faces = self.face_cascade.detectMultiScale(frame, 1.15, 5, cv2.CASCADE_DO_CANNY_PRUNING)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi = frame[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(roi)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        return frame