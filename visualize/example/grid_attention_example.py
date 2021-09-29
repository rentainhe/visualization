from visualize_attention_map.visualize_attention_map import visulize_attention
from visualize_attention_map.visualize_attention_map_V2 import visulize_attention_ratio
import numpy as np

if __name__ == "__main__":
    img_path = 'test_data/test_image.jpg'
    random_attention = np.random.randn(14, 14)
    save_path = 'test_data/'
    visulize_attention_ratio(img_path=img_path, save_path=save_path, attention_mask=random_attention, save_image=True,
                       save_original_image=True)

