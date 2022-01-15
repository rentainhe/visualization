import os
import cv2
import math
from typing import Tuple, Optional, List

import matplotlib.pyplot as plt


def pair(t):
    return t if isinstance(t, tuple) else (t, t)


def divide_img(img_path, img_size = None, patch_size = 16, save_path = None):
    """
    Args:
        img_path (str): path to the input image file
        img_size (int, tuple): input image size
        patch_size (int, tuple): patch size
        save_path (str): path to save the image patchess
    """
    img_size = pair(img_size)
    patch_size = pair(patch_size)
    
    # load image
    img = cv2.imread(img_path)

    if img_size:
        img = cv2.resize(img, img_size)

    h, w = img.shape[0], img.shape[1]
    patch_h, patch_w = patch_size
    
    # patch nums
    divide_h = int(math.floor(h / patch_h))
    divide_w = int(math.floor(w / patch_w))

    # save img
    for i in range(divide_h):
        for j in range(divide_w):
            print("Visualize patch ({}, {}) of the input image".format(i, j))
            patch = img[divide_h*i : divide_h*(i+1), divide_w*j : divide_w*(j+1), :]

            # save single patch
            cv2.imwrite(os.path.join(save_path + 'patch_{}_{}.jpg'.format(i, j)), patch)

