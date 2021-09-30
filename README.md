# visualization
a collection of visualization operation for easier usage

## New Features
**2021/09/29**
- Add pip installation
- Build a cleaner repo

## Contents
### Visualization Function
- [__Grid Attention Visualization__](/visualize/grid_attention_visualization/)
- [__Region Attention Visualization__](/visualize/region_attention_visualization/)
- [__Draw Line Chart__](/visualize/draw_line_chart/draw.py)

### Learning Notes Sharing
- [__Image Reading Difference__](/notes)


## Installation
```bash
pip install visualize==0.5.0
```

## Usage
<details>
<summary> <b> Run Example </b> </summary>

You can try [example.py](/example.py) by cloning this repo for a quick start.
```bash
git clone https://github.com/rentainhe/visualization.git
python example.py
```
results will be saved to `./test_grid_attention` and `./test_region_attention`
</details>

<details>
<summary> <b> Region Attention Visualization </b> </summary>

**download the [example.jpg](/visualize/test_data/example.jpg) to any folder you like**
```bash
$ wget 
```
**build the following python script for a quick start**
```python
import numpy as np
from visualize import visualize_region_attention

img_path="path/to/example.jpg"
save_path="example"
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
```
- `img_path`: where to load the original image
- `boxes`: a list of coordinates for the bounding boxes
- `box_attentions`: a list of attention scores for each bounding box
- `attention_ratio`: a special param, if you set the attention_ratio larger, it will make the attention map look more shallow. Just try!

**Note that you can check [Region Attention Visualization](/visualize/region_attention_visualization/) here for more details**

</details>

<details>
<summary> <b> Grid Attention Visualization</b> </summary>

**download the [example.jpg](/visualize/test_data/example.jpg) to any folder you like**
```bash
$ wget 
```

**build the following python script for a quick start**
```python
import numpy as np
from visualize 

img_path = 'test_data/example.jpg'
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


**Note that you can check [Attention Map Visualization](https://github.com/rentainhe/visualization/tree/master/visualize_attention_map) here for more details**

</details>

