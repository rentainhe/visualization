import torch
import numpy as np
import cv2
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def visulize_attention(img, save_path, attention_mask):
    """
    alphas:     attn weights, (49,)
    img_path:   image file path to load
    save_path:  image file path to save
    scale:      reshape alphas to (scale, scale)
    return:
    """

    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))


    plt.imshow(img, alpha=1)
    plt.axis('off')

    mask = cv2.resize(attention_mask, (img_h, img_w))
    normed_mask = mask / mask.max()
    normed_mask = (normed_mask * 255 ).astype('uint8')
    normed_mask = cv2.applyColorMap(normed_mask, cv2.COLORMAP_BONE)
    mask = cv2.resize(normed_mask, img.size)[..., np.newaxis]
    img = cv2.addWeighted(np.float32(img),1,mask,0.2,0)
    plt.imshow(normed_mask, alpha=0.2, interpolation='nearest')

