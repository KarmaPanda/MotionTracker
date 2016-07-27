import cv2
import numpy as np


def videowriter(frame, codec, dest, fps):
    height, width, depth = frame.shape
    return cv2.VideoWriter(dest, codec, fps, (width, height), 1)