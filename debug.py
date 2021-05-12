import cv2
from PIL import Image
import matplotlib.pyplot as plt

def visulize_spatial_attention(img_path, attention_mask, ratio=1, cmap="jet"):
    """
    img_path:   image file path to load
    save_path:  image file path to save
    attention_mask: 2-D attention map with np.array type, e.g, (h, w) or (w, h)
    ratio:  scaling factor to scale the output h and w
    cmap:   attention style, default: "jet"
    """
    print("load image from: ", img_path)
    img = Image.open(img_path, mode='r')
    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))

    # scale the image
    img_h, img_w = int(img.size[0] * ratio), int(img.size[1] * ratio)
    img = img.resize((img_h, img_w))
    plt.imshow(img, alpha=1)
    plt.axis('off')

    mask = cv2.resize(attention_mask, (img_h, img_w))
    normed_mask = mask / mask.max()
    normed_mask = (normed_mask * 255).astype('uint8')
    plt.imshow(normed_mask, alpha=0.5, interpolation='nearest', cmap=cmap)
    plt.show()


img_path = 'test_data/test_image.jpg'
import numpy as np
random_attention = np.random.randn(14, 14)
save_path = 'test_data/'

visulize_spatial_attention(img_path=img_path, attention_mask=random_attention)
print(type(random_attention))