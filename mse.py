import math
import sys
import cv2
import numpy as np
from PIL import Image

def calculate_mse(img1, img2):
    # img1 and img2 have range [0, 255]
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')

    return mse

if __name__ == "__main__":
    im1 = cv2.imread(sys.argv[1])
    im2 = cv2.imread(sys.argv[2])

    mse = calculate_mse(im1, im2)
    print(mse)
