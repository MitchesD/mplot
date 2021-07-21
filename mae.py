import math
import sys
import cv2
import numpy as np
from PIL import Image

def calculate_mae(img1, img2):
    # img1 and img2 have range [0, 255]
    x = img1.shape[0]
    y = img1.shape[1]
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mae = np.sum(np.absolute(img1 - img2))
    mae /= float(x * y * 255)
    if mae == 0:
        return float('inf')

    return mae

if __name__ == "__main__":
    im1 = cv2.imread(sys.argv[1])
    im2 = cv2.imread(sys.argv[2])

    mae = calculate_mae(im1, im2)
    print(mae)
