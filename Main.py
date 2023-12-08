from Dependencies import *
from FileOutput import FileOutput
from FaceTracker import FaceTracker
from ObjectTracker import ObjectTracker


class Main(object):
    _active = True
    _cameraPort = 0
    _camera = cv2.VideoCapture(_cameraPort)
    _currentFrame = None
    _faceTracker = FaceTracker(None, object, None)
    _fileOutput = FileOutput(None)
    _objectTracker = ObjectTracker(None)

    def __init__(self):
        self._faceTracker.__init__(
            camera=self._camera, instance=self, fileoutput=self._fileOutput)
        self._fileOutput.__init__(facetracker=self._faceTracker)
        self._objectTracker.__init__(camera=self._camera)

        while self._active:
            if self._fileOutput.record:
                self._fileOutput.output = self._fileOutput.setuprecording()
            t_end = time.time() + 15
            while time.time() < t_end:
                self.update()
                ret = self.checkkey()
                if not ret:
                    break
            # self._camera.release()
            if self._fileOutput.record:
                self._fileOutput.output.release()
                self._fileOutput.fileCountVid += 1

        self._camera.release()
        if self._fileOutput.record:
            self._fileOutput.output.release()
        cv2.destroyAllWindows()

    def update(self):
        try:
            frame = self._objectTracker.update()
            if frame is not None:
                if self._objectTracker.isOccupied:
                    frame = self._faceTracker.detectface(frame)
                frame = self._objectTracker.printstamp(frame)
                cv2.imshow("Video", frame)
                if self._fileOutput.record and self._objectTracker.isOccupied:
                    self._fileOutput.output.write(frame)
                self._currentFrame = frame
            else:
                print("No frame found...")
        except:
            print("Error in update...")

    def checkkey(self):
        ret = True
        keyInput = chr(cv2.waitKey(5) & 0xFF)
        if keyInput == Keymap.quitKey:
            self._active = False
            ret = False
        if cv2.getWindowProperty("Video", 0) == -1:
            self._active = False
            ret = False
        if keyInput == Keymap.recordKey:
            if self._fileOutput.record:
                self._fileOutput.record = False
                self._fileOutput.output.release()
                self._fileOutput.fileCountVid += 1
            else:
                self._fileOutput.output = self._fileOutput.setuprecording(
                    self._currentFrame)
                self._fileOutput.record = True
        if keyInput == Keymap.screenshotKey:
            self._fileOutput.takescreenshot(self._currentFrame)
        return ret


instance = Main()
instance.__init__()
