import numpy as np
import cv2
import os


img = cv2.imread('../assets/lenna.png')
J = cv2.GaussianBlur(img, (33, 33), sigmaX=10)
cv2.imshow('blur', J)
cv2.waitKey(0)
cv2.imwrite(os.path.join(os.path.abspath('../results'), 'lenna-gaussian.png'), J)
