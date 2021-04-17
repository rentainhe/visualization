import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt


def region_attention_visualization(img_path, boxes, box_attentions, img_ratio=1.5, attention_ratio=1.0):
    """
    img_path: 读取图片的位置
    boxes: 一系列 bounding box, 类型 np.int, [x,y,x,y] 前两个表示左上角坐标, 后两个是右下角坐标
    box_attentions:  每个box对应的attention值, 类型是list, list中每个index对应一个bounding box的attention
    img_ratio: 图片缩放比率（可选）
    """
    print("load image from: ", img_path)
    # load the image
    img = Image.open(img_path, mode='r')
    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))

    # scale the image
    img_h, img_w = int(img.size[0] * img_ratio), int(img.size[1] * img_ratio)
    img = img.resize((img_h, img_w))
    plt.imshow(img, alpha=1)
    plt.axis('off')

    # draw bounding box with attention
    img = np.ascontiguousarray(img)  # 将Image.Image类型转化为连续的numpy数组
    for box, attention in zip(boxes, box_attentions):
        box = cv2.rectangle(img, tuple(box[:2]), tuple(box[2:]), (255, 0, 0), -1)  # 最后一个值设置为负数, 表示全填充
        plt.imshow(box, alpha=attention / attention_ratio)  # add a scale of 2 for better visualization
    plt.show()

if __name__ == "__main__":
    img_path = "../test_data/test_image.jpg"
    boxes = np.array([[14, 25, 100, 200], [56, 75, 245, 300]], dtype='int')
    region_attention_visualization(img_path, boxes, box_attentions=[0.36, 0.64], attention_ratio=1.25)
