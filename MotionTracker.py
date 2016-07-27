import os
from FaceDetection import *
from FileOutput import *
from KeyMapping import *

# Variables
active = True
camera = cv2.VideoCapture(0)
destination = 'Videos/'
filename = 'vid_'

# Functions
def main(args=None):
    pass

def update():
    pass

main()

# Setup FileSystem
filesinDir = os.listdir(destination)
fileCount = 0
for fileName in filesinDir:
    if fileName.__contains__(fileName):
        fileCount += 1

# Starts Loop
previousFrame = None
frame = detectface(camera)
codec = cv2.VideoWriter_fourcc('a', 'v', 'c', '1')
output = videowriter(frame, codec, destination + filename + str(fileCount), 5)

while active:
    valid = camera.grab()
    if valid:
        ret, frame = camera.read()
        frame = detectface(camera)
        output.write(frame)
        cv2.imshow("Video", frame)
    keyInput = chr(cv2.waitKey(1) & 0xFF)
    if keyInput == quitKey:
        active = False
    if cv2.getWindowProperty("Video", 0) == -1:
        break

camera.release()
output.release()
cv2.destroyAllWindows()