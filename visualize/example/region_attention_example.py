from visualize_region_attention.region_attention_visualization import region_attention_visualization
import numpy as np

if __name__ == "__main__":
    img_path = "test_data/test_image.jpg"
    boxes = np.array([[14, 25, 100, 200], [56, 75, 245, 300]], dtype='int')
    region_attention_visualization(img_path, boxes, box_attentions=[0.36, 0.64], attention_ratio=1.0)