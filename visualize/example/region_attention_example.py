import numpy as np
from ..region_attention_visualization import visualize_region_attention


def run_region_attention_example(img_path="visualize/test_data/example.jpg", save_path="test", attention_retio=1.0, boxes=None, box_attentions=None, quality=200):
    if boxes:
        assert box_attentions is not None, "boxes should be passed in with box_attentions"
    else:
        boxes = np.array([[14, 25, 100, 200], [56, 75, 245, 300]], dtype='int')
        boxes_attention = [0.36, 0.64]
        visualize_region_attention(img_path,
                                   save_path=save_path, 
                                   boxes=boxes, 
                                   box_attentions=boxes_attention, 
                                   attention_ratio=attention_retio,
                                   save_image=True,
                                   save_origin_image=True,
                                   quality=quality)
