# creating a rpogram that takes in an image and a message and encrypts that message inside the image

import os

from utils import *

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT, 'encrypted')

# open the image
I = cv2.imread('assets/lenna.png')
print(I.shape)
print('no. len bits:', get_image_data_volume_bit_len(I))
print('max message length:', max_message_length(I))
plaintext = "attack tomorrow at dawn"
plaintext = random_string(max_message_length(I))

# Converting the image to png and saving the image
cv2.imwrite(os.path.join(os.path.join(APP_ROOT, 'png'), 'lenna.png'), I)

# Load the png image
I = cv2.imread('png/lenna.png')

# Encrypt the png image
J = lsb_encrypt(I, plaintext)
print(np.sum(I != J))

# save the encrypted image as png
cv2.imwrite(os.path.join(target, 'lenna.png'), J)

# open encrypted png image
J = cv2.imread(os.path.join(target, 'lenna.png'))


message = lsb_decrypt(J)
print(message == plaintext)
if len(message) < 1000:
    print(message)

cv2.imshow('original', I)
cv2.imshow('new', J)
diff = image_diff(I, J)
# print(diff)
cv2.imshow('diff', diff)
cv2.waitKey(0)
