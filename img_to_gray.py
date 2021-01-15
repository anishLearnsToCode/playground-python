import os

import cv2
import numpy as np

RESULTS_DIR = os.path.abspath('results')


def simple_gray(I: np.ndarray) -> np.ndarray:
    return np.array(np.average(I, axis=-1), dtype=np.uint8)


def weighted_gray(I: np.ndarray) -> np.ndarray:
    return np.array(np.average(I, axis=-1, weights=(0.0722, 0.7152, 0.2126)), dtype=np.uint8)


I = cv2.imread('assets/lenna.png')
J = simple_gray(I)
J2 = weighted_gray(I)
print(J)
cv2.imshow('gray', J)
cv2.imshow('weighted', J2)
cv2.waitKey(0)

path = os.path.join(RESULTS_DIR, 'lenna-gray.png')
cv2.imwrite(path, J)
