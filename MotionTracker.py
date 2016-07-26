import os
from FaceDetection import *
from FileOutput import *
from KeyMapping import *

# Variables
active = True
camera = cv2.VideoCapture(1)
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
codec = cv2.VideoWriter_fourcc('H','2','6','4')
output = videowriter(frame, codec, destination + filename + str(fileCount))

while active:
    ret, frame = camera.read()
    frame = detectface(camera)
    output.write(frame)
    cv2.imshow("Video", frame)
    keyInput = chr(cv2.waitKey(1) & 0xFF)
    if keyInput == quitKey:
        active = False

camera.release()
output.release()
cv2.destroyAllWindows()