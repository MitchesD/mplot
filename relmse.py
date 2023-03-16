import cv2
import sys
import numpy as np
import math
from PIL import Image

def relMSE(image, ref_image):
    image = image.astype(np.float64)
    ref_image = ref_image.astype(np.float64)
    diff = image - ref_image
    rel_diff = np.square(diff) / (np.square(ref_image) + 1e-3)
    rel_mse = np.mean(rel_diff)
    return rel_mse

if __name__ == "__main__":
    im1 = cv2.imread(sys.argv[1])
    im2 = cv2.imread(sys.argv[2])

    rel_mse = relMSE(im2, im1)
    print(str(rel_mse))
