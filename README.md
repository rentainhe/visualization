# visualization
a collection of visualization operation

## Contents
- [__Attention Map Visualization__](https://github.com/rentainhe/visualization/tree/master/visualize_attention_map)
- [__Image Reading Difference__](https://github.com/rentainhe/visualization/tree/master/read_img)
- [__Region Attention Visualization__](https://github.com/rentainhe/visualization/tree/master/visualize_region_attention)
- [__Draw Line Chart__]()


## Usage
### 1. Grid Attention Visualization
```python
import numpy as np
from visualize_attention_map.visualize_attention_map_V2 import visulize_attention_ratio

img_path = 'test_data/test_image.jpg'
save_path = 'test_data/'
random_attention = np.random.randn(14, 14)

visulize_attention_ratio(img_path=img_path, save_path=save_path, attention_mask=random_attention, save_image=True,
                   save_original_image=True)
```
- __img_path: where the image you want to put an attention mask on.__
- __save_path: where to save the image.__
- __attention_mask: the attention mask with format `numpy.ndarray`, its shape is (H, W)__
- __save_image=True: save the image with attention map or not, default: True.__
- __save_original_image=True: save the original image, default: True__

__Just run this example to see the result: [grid_attention_example.py](https://github.com/rentainhe/visualization/blob/master/grid_attention_example.py)__

__Or you can check [Attention Map Visualization](https://github.com/rentainhe/visualization/tree/master/visualize_attention_map) here for more details__

### 2. Region Attention Visualization
```python
from visualize_region_attention.region_attention_visualization import region_attention_visualization
import numpy as np

img_path = "test_data/test_image.jpg"
boxes = np.array([[14, 25, 100, 200], [56, 75, 245, 300]], dtype='int')
region_attention_visualization(img_path, boxes, box_attentions=[0.36, 0.64], attention_ratio=1.0)
```
- __img_path: the path of the original image__
- __boxes: bounding box__
- __box_attentions: the attention score of each bounding box__
- __attention_ratio: a special param, if you set the attention_ratio larger, it will make the attention map look more shallow. Just try!__

__Just run this example to see the result: [region_attention_example.py](https://github.com/rentainhe/visualization/blob/master/region_attention_example.py)__

__Or you can check [Region Attention Visualization](https://github.com/rentainhe/visualization/tree/master/visualize_region_attention) here for more details__

### 3. Draw Line Chart
- [__example.py__](https://github.com/rentainhe/visualization/blob/master/draw_line_chart/draw.py)