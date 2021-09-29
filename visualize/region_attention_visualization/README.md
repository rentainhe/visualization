## attention map visualization

### pre-requisite
```bash
$ pip install opencv-python
$ pip install matplotlib
$ pip install Pillow
$ pip install numpy
```

### Contents
- __code__ is here [__region_attention_visualization.py__](https://github.com/rentainhe/visualization/blob/master/visualize_region_attention/region_attention_visualization.py)

当前版本还有改进空间, 改进后会更新至github

### API Reference
使用到的接口
```python
import cv2
cv2.rectangle(img=..., pt1=..., pt2=..., color=..., thickness=...)
```
- `img`: 输入的图像
- `pt1`: 左上角坐标
- `pt2`: 右下角坐标
- `color`: 框颜色的数值, RGB
- `thickness`: 框的厚度, 当设置为-1的时候采用全填充的形式

### Results
#### original figure
![](/figs/attention/region_image_original.jpg)

#### with region attention
![](/figs/attention/region_image_with_attention.jpg)