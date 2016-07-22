import cv2
import numpy as np

# Variables
active = True
camera = cv2.VideoCapture(0)

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

previousFrame = None

while active:
    previousFrame, finalImg = update(previousFrame)
    cv2.imshow("Image", finalImg)
    keyInput = chr(cv2.waitKey(1) & 0xFF)
    if keyInput == 'q':
        active = False