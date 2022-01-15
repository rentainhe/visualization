# encoding: utf-8
"""
@author:  rentianhe
@contact: 596106517@qq.com
"""

import os
import argparse
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# helpers
def add_path(a, b):
    return os.path.join(a, b)

def load_data_from_txt(path):
    data = []
    with open(path, "r") as f:
        for _line in f.readlines():
            data.append(float(_line.strip()))
    return data

def draw_line_chart(data_list: list,
                    labels: list,
                    xlabel: str,
                    ylabel: str,
                    save_path: str,
                    legend = {"loc": "upper right", "frameon": True, "fontsize": 8},
                    title = None, # Optional
                    xlim = None, # Optional
                    ylim = None, # Optional  
                    ):
    assert len(labels) == len(data_list), "One kind of data matches one label"

    # setup
    plt.rcParams["figure.dpi"] = 100
    plt.clf()
    plt.xlabel(xlabel, fontproperties="Times New Roman")
    plt.ylabel(ylabel, fontproperties="Times New Roman")
    if xlim:
        plt.xlim(xlim[0], xlim[1])
    if ylim:
        plt.ylim(ylim[0], ylim[1])

    for data, label in zip(data_list, labels):
        idx = [i for i in range(len(data))]
        plt.plot(idx, data, label=label)
    if title:
        plt.title(title)
    plt.legend(loc=legend["loc"], frameon=legend["frameon"], fontsize=legend["fontsize"])
    plt.savefig(save_path)
    print("Save image to [PATH: '%s']" % save_path)
    
if __name__ == "__main__":
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

