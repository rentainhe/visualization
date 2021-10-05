## Difference Between Pillow and CV2

### pre-requisite
```bash
$ pip install opencv-python
$ pip install Pillow
$ pip install matplotlib
```

### Contents
- Relative Code is here [show_img.py](https://github.com/rentainhe/visualization/blob/master/read_img/show_img.py)

#### Read Image by CV2
```python
import matplotlib.pyplot as plt
import cv2
img_path = ...
img = cv2.imread(img_path) # h, w, 3
# print(img.shape)
# reverse the last channel
# img = img[:, :, ::-1]
plt.imshow(img)
```
- if __not reverse__ the last channel:

![](/figs/img_read_example/cv2_not_reverse.png)

- if __reversed__:

![](/figs/img_read_example/reversed.png)

#### Read Image by Pillow
```python
import matplotlib.pyplot as plt
import PIL.Image as Image
img_path = ...
img = Image.open(img_path)
# print(img.size)
plt.imshow(img)
```

- You don't need to do other operations

![](../figs/img_read_example/reversed.png)


