from Dependencies import *

class FaceTracker(object):
    face_cascade = cv2.CascadeClassifier('HaarCascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('HaarCascade/parojos.xml')
    camera = None
    fileoutput = None

    def __init__(self, camera, fileoutput):
        self.camera = camera
        self.fileoutput = fileoutput

    def detectface(self, frame):
        #ret, frame = self.camera.read()
        #if ret:
        faces = self.face_cascade.detectMultiScale(frame, 1.15, 5, cv2.CASCADE_DO_CANNY_PRUNING)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi = frame[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(roi)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        return frame
        #else:
            #return None

    @property
    def getaveragefps(self):
        num_frames = 0
        start = time.time()
        frame = self.detectface
        cv2.imshow("Video", frame)
        cv2.destroyWindow("Video")
        num_frames += 1
        fps = (num_frames / (time.time() - start))
        return int(math.floor(fps))