import numpy as np
import cv2
import pprint
from utils import *
import os
RESULTS_DIR = os.path.abspath('results')


I = cv2.imread('assets/lenna.png')
J = cv2.imread('assets/lenna.png')
print(max_message_length(I))
plaintext = random_string(max_message_length(I))
# plaintext = 'hello world, we attack tomorrow!'
lsb_encrypt(J, plaintext)
decrypted = lsb_decrypt(J)
print(decrypted == plaintext)
diff = I - J
print(np.sum(I != J))
cv2.imshow('original', I)
cv2.imshow('novel', J)
cv2.imshow('diff', diff)
cv2.waitKey(0)

path = os.path.join(RESULTS_DIR, 'encrypted.png')
diff_path = os.path.join(RESULTS_DIR, 'lenna-diff-1.png')
cv2.imwrite(path, J)
cv2.imwrite(diff_path, diff)
