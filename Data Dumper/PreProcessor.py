import cv2
import numpy as np


def cleanImg(frame=None, key=None):
    b, _, r = cv2.split(frame)
    black_channel = np.zeros(frame.shape[:2], dtype='uint8')
    frame = cv2.merge([b, black_channel, r])
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 2)
    _, res = cv2.threshold(
        th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return [res, np.array(labelCreation(key))]


def labelCreation(n=None):
    label = [0]*23
    label[n] = 1
    return label
