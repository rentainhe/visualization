import matplotlib.pyplot as plt
import PIL.Image as Image
import cv2

def pillow_img_show(img_path):
    # Use Pillow API
    img = Image.open(img_path)
    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

def cv2_img_show(img_path):
    # Use cv2 API
    img = cv2.imread(img_path) # h, w, c
    img_h, img_w, c = img.shape[0], img.shape[1], img.shape[2]
    img = img[:, :, ::-1]  # reverse the last channel
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))
    plt.axis('off')
    plt.imshow(img)
    plt.show()