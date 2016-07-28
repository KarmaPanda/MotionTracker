import os
import time
import math
from FaceDetection import *
from FileOutput import *
from KeyMapping import *

# Variables
active = True
camera = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
destination = 'Videos/'
destinationPic = "ScreenShots/"
fileCount = 0
fileCountPic = 0
filename = 'vid_'
filenamePic = 'pic_'
output = None
record = False


# Functions
def main(args=None):
    global fileCount
    global fileCountPic
    global output

    # Setup Optimization
    cv2.setUseOptimized(True)

    # Setup Picture File System
    filesinDirP = os.listdir(destinationPic)
    fileCountPic = 0
    for fileName in filesinDirP:
        if fileName.__contains__(filenamePic):
            fileCountPic += 1

    # Setup Video File System
    filesinDir = os.listdir(destination)
    fileCount = 0
    for fileName in filesinDir:
        if fileName.__contains__(filename):
            fileCount += 1

    if record:
        output = setuprecording()


def update():
    valid = camera.grab()
    if valid:
        frame = detectface(camera)
        if record:
            output.write(frame)
        cv2.imshow("Video", frame)
        return frame
    return None


def setuprecording(frame = None):
    if frame is None:
        frame = detectface(camera)
    fps = getaveragefps()
    output = videowriter(frame, codec, destination + filename + str(fileCount), fps)
    return output


def getaveragefps():
    num_frames = 0
    start = time.time()
    frame = detectface(camera)
    cv2.imshow("Video", frame)
    num_frames += 1
    fps = (num_frames / (time.time() - start))
    return int(math.floor(fps)) - 1


def takescreenshot(frame):
    global fileCountPic
    ret = cv2.imwrite("{0}{1}{2}.jpg".format(destinationPic, filenamePic, str(fileCountPic)), frame)
    fileCountPic += 1
    return ret

main()

while active:
    x = update()
    keyInput = chr(cv2.waitKey(getaveragefps()) & 0xFF)
    if keyInput == quitKey:
        break
    if keyInput == recordKey:
        if record:
            record = False
            fileCount += 1
            output.release()
        else:
            output = setuprecording(x)
            record = True
    if keyInput == screenshotKey:
        takescreenshot(x)
    if cv2.getWindowProperty("Video", 0) == -1:
        break

camera.release()
if record:
    output.release()
cv2.destroyAllWindows()