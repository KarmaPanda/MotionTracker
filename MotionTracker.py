import cv2
import numpy as np


def main(args=None):
    camera = cv2.VideoCapture(0)
    ret, previousFrame = camera.read()
    while True:
        ret, currentFrame = camera.read()
        img = cv2.subtract(currentFrame, previousFrame)
        ret, thresh = cv2.threshold(img, 10, 160, cv2.THRESH_BINARY)
        previousFrame = currentFrame
        cv2.imshow("image", thresh)
main()