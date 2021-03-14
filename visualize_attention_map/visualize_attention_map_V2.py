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
    # load the image
    # img = skimage.img_as_float(img).astype(np.float32)
    #         img_h, img_w = img.shape[0], img.shape[1]
    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))

    #         cv2.resize(img,(16,16))
    # alphas = np.array(alphas).swapaxes(0, 1)  # n,49,1

    plt.imshow(img, alpha=1)
    plt.axis('off')
    #         scale  = 16
    # alpha_img = skimage.transform.pyramid_expand(alphas[0,:].reshape(7,7),upscale=16,sigma=20)
    # alpha_img = skimage.transform.resize(alphas[0, :].reshape(scale, scale), [img.shape[0], img.shape[1]])
    #         alpha_img = transform.resize(alphas.reshape(scale, scale), [img_h, img_w])
    #         alpha_img = transform.resize(alpha_img.reshape(scale, scale,1), [img_w, img_h])
    mask = cv2.resize(attention_mask, (img_h, img_w))
    normed_mask = mask / mask.max()
    #         normed_mask = (normed_mask * 255 ).astype('uint8')
    #         normed_mask = cv2.applyColorMap(normed_mask, cv2.COLORMAP_BONE)
    #         if img.shape[2]
    #         mask = cv2.resize(normed_mask, img.size)[..., np.newaxis]
    #         img = cv2.addWeighted(np.float32(img),1,mask,0.2,0)
    #         plt.imshow(normed_mask, alpha=0.2, interpolation='nearest')

    # plan B
    mask = cv2.resize(normed_mask, img.size)[..., np.newaxis]
    result = (img * mask).astype("uint8")
    plt.imshow(result, alpha=1)

    # save
    # img_name = img_path.split('/')[-1]
#         plt.savefig(save_path + 'atted.jpg', format='jpg', dpi=100)
