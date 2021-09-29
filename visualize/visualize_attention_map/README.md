## attention map visualization

### pre-requisite
```bash
$ pip install opencv-python
$ pip install matplotlib
$ pip install Pillow
$ pip install numpy
```

### Contents
- __Version1__ is here [visualize_attention_map.py](/visualize/visualize_attention_map/visualize_attention_map.py)
- __Version2 (recommended)__ is here [visualize_attention_map_V2.py](/visualize/visualize_attention_map/visualize_attention_map_V2.py)


the attention style in version2 can be changed by "cmap", choose the color map you like [here](https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html)

### Result
#### 1. Version1 example
- __original image__

![](/figs/attention/original_fig.jpg)
 
- __image with attention__ (for example we use random attention map here)

![](/figs/attention/fig_with_attention.jpg)

#### 2. Version2 example
- __original image__

![](/figs/attention/version2_example_without_attention.png)
 
- __image with attention__ (for example we use random attention map here)

![](/figs/attention/version2_example_with_attention.png)