from visualize import run_region_attention_example, run_grid_attention_example
from visualize import visualize_region_attention, visulize_grid_attention, visulize_grid_attention_v2
import numpy as np

# test region attention
img_path="test_data/test_image.jpg"
save_path="test"
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

# test region example
run_region_attention_example()

# test grid example
run_grid_attention_example()