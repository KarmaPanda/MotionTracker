from Dependencies import *
from FileOutput import FileOutput
from FaceTracker import FaceTracker
from ObjectTracker import ObjectTracker
from KeyMapping import Keymap

_camera = cv2.VideoCapture(0)
_faceTracker = FaceTracker(None, None)
_fileOutput = FileOutput(None)
_objectTracker = ObjectTracker(None)
_faceTracker.__init__(camera=_camera, fileoutput=_fileOutput)
_fileOutput.__init__(facetracker=_faceTracker)
_objectTracker.__init__(camera=_camera)

while True:
    frame = _objectTracker.update()
    if _objectTracker.isOccupied:
        frame = _faceTracker.detectface(frame)
    frame = _objectTracker.printstamp(frame)
    cv2.imshow("Video", frame)
    if _fileOutput.record:
        _fileOutput.output.write(frame)
    keyInput = chr(cv2.waitKey(1) & 0xFF)
    if keyInput == Keymap.quitKey:
        break
    if cv2.getWindowProperty("Video", 0) == -1:
        break
    if keyInput == Keymap.recordKey:
        if _fileOutput.record:
            _fileOutput.record = False
            _fileOutput.output.release()
            _fileOutput.fileCountVid += 1
        else:
            _fileOutput.output = _fileOutput.setuprecording(frame)
            _fileOutput.record = True
    if keyInput == Keymap.screenshotKey:
        _fileOutput.takescreenshot(frame)

'''

x = FaceTracker()

while FaceTracker.active:
    frame = x.update()
    keyInput = chr(cv2.waitKey(x.getaveragefps()) & 0xFF)

'''

_camera.release()
if _fileOutput.record:
    _fileOutput.output.release()
cv2.destroyAllWindows()