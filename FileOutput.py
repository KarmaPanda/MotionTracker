import cv2
import numpy as np


def videowriter(frame, codec, dest):
    height, width, depth = frame.shape
    return cv2.VideoWriter(dest, codec, 5.0, (width, height))