from visualize.visualize_attention_map import visulize_grid_attention, visulize_grid_attention_v2
import numpy as np


def run_grid_attention_example():
    img_path = 'test_data/test_image.jpg'
    random_attention = np.random.randn(14, 14)
    save_path = 'test/'
    visulize_grid_attention_v2(img_path=img_path, save_path=save_path, attention_mask=random_attention, save_image=True,
                       save_original_image=True)


