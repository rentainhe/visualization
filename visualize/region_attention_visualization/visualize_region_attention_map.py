# encoding: utf-8
"""
@author:  rentianhe
@contact: 596106517@qq.com
"""

import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def visualize_region_attention(img_path, save_path, boxes, box_attentions, img_ratio=1.5, attention_ratio=1.0,
                               save_image=True, save_origin_image=True, quality=200):
    """
    img_path: 读取图片的位置
    boxes: 一系列 bounding box, 类型 np.int, [x,y,x,y] 前两个表示左上角坐标, 后两个是右下角坐标
    box_attentions:  每个box对应的attention值, 类型是list, list中每个index对应一个bounding box的attention
    img_ratio: 图片缩放比率（可选）
    save_image: 保存生成attention后的图片
    save_original_image: 保存原始图片
    quality: 保存的图片质量
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
    img_numpy = np.ascontiguousarray(img)  # 将Image.Image类型转化为连续的numpy数组
    for box, attention in zip(boxes, box_attentions):
        box = cv2.rectangle(img_numpy, tuple(box[:2]), tuple(box[2:]), (255, 0, 0), -1)  # 最后一个值设置为负数, 表示全填充
        plt.imshow(box, alpha=attention / attention_ratio)  # add a scale of 2 for better visualization
    plt.show()

    # save image
    if save_image:
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        img_name = img_path.split('/')[-1].split('.')[0] + "_with_attention.jpg"
        img_with_attention_save_path = os.path.join(save_path, img_name)
        
        # pre-process and save image
        print("save image to: " + save_path + " as " + img_name)
        plt.axis('off')
        plt.subplots_adjust(top=1, bottom=0, right=1,  left=0, hspace=0, wspace=0)
        plt.margins(0, 0)
        plt.savefig(img_with_attention_save_path, dpi=quality)
    
    if save_origin_image:
        # build save path
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        # save original image file
        print("save original image at the same time")
        img_name = img_path.split('/')[-1].split('.')[0] + "_original.jpg"
        original_image_save_path = os.path.join(save_path, img_name)
        img.save(original_image_save_path, quality=quality)
