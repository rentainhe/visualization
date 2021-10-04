import numpy as np
from visualize import visualize_region_attention, visualize_grid_attention, visualize_grid_attention_v2
from visualize import draw_line_chart


# helpers
def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


# test region attention
def run_region_attention_example():
    img_path="visualize/test_data/example.jpg"
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


# test grid attention
def run_grid_attention_example(img_path="visualize/test_data/example.jpg", save_path="test_grid_attention/", attention_mask=None, version=2, quality=100):
    if not attention_mask:
        attention_mask = np.random.randn(64)
        normed_attention_mask = softmax(attention_mask).reshape(8, 8)
        # attention_mask = np.random.randn(14, 14)
    assert version in [1, 2], "We only support two version of attention visualization example"
    if version == 1:
        visualize_grid_attention(img_path=img_path, 
                                save_path=save_path, 
                                attention_mask=normed_attention_mask, 
                                save_image=True,
                                save_original_image=True,
                                quality=quality)
    elif version == 2:
        visualize_grid_attention_v2(img_path=img_path, 
                                   save_path=save_path, 
                                   attention_mask=normed_attention_mask, 
                                   save_image=True,
                                   save_original_image=True,
                                   quality=quality)

def run_line_chart_example():
    # test data
    data1 = {"data": [13.15, 14.64, 15.83, 17.99], "name": "data 1"}
    data2 = {"data": [14.16, 14.81, 16.11, 18.62], "name": "data 2"}
    data_list = []
    data_list.append(data1["data"])
    data_list.append(data2["data"])
    name_list = []
    name_list.append(data1["name"])
    name_list.append(data2["name"])
    draw_line_chart(data_list=data_list,
                    labels=name_list,
                    xlabel="test_x",
                    ylabel="test_y",
                    save_path="./test.jpg",
                    legend={"loc": "upper left", "frameon": True, "fontsize": 12},
                    title="example")

if __name__ == "__main__":
    run_grid_attention_example(version=2) # version in [1, 2]
    run_region_attention_example()
    run_line_chart_example()