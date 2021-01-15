from utils import *
import cv2


J = cv2.imread('assets/lenna.jpg')
message = lsb_decrypt(J)
print(message)
