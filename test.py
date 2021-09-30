from visualize import visualize_region_attention, visulize_grid_attention, visulize_grid_attention_v2
import numpy as np

def run_region_attention_example():
# test region attention
    img_path="visualize/test_data/test_image.jpg"
    save_path="test_region_attention/"
    attention_retio=1.0
    boxes = np.array([[14, 25, 100, 200], [56, 75, 245, 300]], dtype='int')
    boxes_attention = [0.36, 0.64]
    visualize_region_attention(img_path,
                                save_path=save_path, 
                                boxes=boxes, 
                                box_attentions=boxes_attention, 
                                attention_ratio=attention_retio,
                                save_image=True,
                                save_origin_image=True,
                                quality=100)


def run_grid_attention_example(img_path="visualize/test_data/test_image.jpg", save_path="test_grid_attention/", attention_mask=None, version=2, quality=100):
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

if __name__ == "__main__":
    run_grid_attention_example(version=2) # version in [1, 2]
    run_region_attention_example()