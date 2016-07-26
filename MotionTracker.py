import os
from FaceDetection import *
from FileOutput import *
from KeyMapping import *

# Variables
active = True
camera = cv2.VideoCapture(0)
destination = "Videos/"
filename = "vid_"


# Functions
def main(args=None):
    pass


def update(previousframe):
    ret, currentframe = camera.read()
    if previousFrame is None:
        img = currentframe
    else:
        img = cv2.subtract(currentframe, previousframe)

    finalimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    finalimg = cv2.GaussianBlur(finalimg, (5, 5), -1)
    ret, finalimg = cv2.threshold(finalimg, 20, 255, cv2.THRESH_BINARY_INV)
    #  contimg, contours, hier = cv2.findContours(finalimg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    #  cv2.drawContours(finalimg, contours, -1, (0, 255, 0), 3)
    ret, currentframe = camera.read()
    return currentframe, finalimg

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
output = videowriter(frame, cv2.VideoWriter_fourcc(*'8BPS'), destination + filename + str(fileCount))

while active:
    #  previousFrame, finalImg = update(previousFrame)
    frame = detectface(camera)
    output.write(frame)
    cv2.imshow("Video", frame)
    keyInput = chr(cv2.waitKey(1) & 0xFF)
    if keyInput == quitKey:
        active = False

camera.release()
output.release()
cv2.destroyAllWindows()