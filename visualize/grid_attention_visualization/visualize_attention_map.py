import numpy as np
import cv2
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def visualize_grid_attention(img_path, save_path, attention_mask, ratio=0.5, save_image=True, save_original_image=True, quality=100):
    """
    img_path: where to load the image
    save_path: where to save the image
    attention_mask: the 2-D attention mask on your image, e.g: np.array (h, w) or (w, h)
    ratio:  scaling factor to scale the output h and w
    quality: save image quality
    """
    print("load image from: " + img_path)
    img = Image.open(img_path)
    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))
    
    # scale the image
    img_h, img_w = int(img.size[0] * ratio), int(img.size[1] * ratio)
    img = img.resize((img_h, img_w))
    plt.imshow(img, alpha=1)
    plt.axis('off')

    # normalize the attention map
    mask = cv2.resize(attention_mask, (img_h, img_w))  # you may change the (img_w, img_h) order to adjust the attention mask
    normed_mask = mask / mask.max()
    normed_mask = cv2.resize(normed_mask, img.size)[..., np.newaxis]

    # put the attention map on the original image
    result = (img * normed_mask).astype("uint8")
    plt.imshow(result, alpha=1)

    # save image
    if save_image:
        # build save path
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        assert save_image is not None, "you need to set where to store the picture"
        img_name = img_path.split('/')[-1].split('.')[0] + "_with_attention.jpg"
        img_with_attention_save_path = os.path.join(save_path, img_name)

        # pre-process before saving
        print("save image to: " + save_path)
        plt.axis('off')
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)
        plt.savefig(img_with_attention_save_path, dpi=quality)

    # save original image
    if save_original_image:
        # build save path
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        
        print("save original image at the same time")
        img_name = img_path.split('/')[-1].split('.')[0] + "_original.jpg"
        original_image_save_path = os.path.join(save_path, img_name)
        img.save(original_image_save_path, quality=quality)
