from visualize.grid_attention_visualization import visulize_grid_attention, visulize_grid_attention_v2
import numpy as np


def run_grid_attention_example(img_path="visualize/test_data/example.jpg", save_path="test/", attention_mask=None, version=2, quality=100):
    if not attention_mask:
        attention_mask = np.random.randn(14, 14)
    assert version in [1, 2], "We only support two version of attention visualization example"
    if version == 1:
        visulize_grid_attention(img_path=img_path, 
                                save_path=save_path, 
                                attention_mask=attention_mask, 
                                save_image=True,
                                save_original_image=True,
                                quality=quality)
    elif version == 2:
        visulize_grid_attention_v2(img_path=img_path, 
                                   save_path=save_path, 
                                   attention_mask=attention_mask, 
                                   save_image=True,
                                   save_original_image=True,
                                   quality=quality)


