# encoding: utf-8
"""
@author:  rentianhe
@contact: 596106517@qq.com
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

# check the style sheet
# print(style.library)
# print(style.available)

# 重新加载样式
plt.style.reload_library()

# 设置样式
plt.style.use(['science', 'no-latex', 'grid', 'seaborn-whitegrid'])

# 设置分辨率
plt.rcParams['figure.dpi'] = 1000

# 清空画图
plt.clf()

# 设置测试数据
y1 = np.array(
    [93.48, 16.11, 14.78, 14.11, 13.29, 12.62, 12.07, 11.55, 11.1, 10.68, 8.84, 8.2, 7.57]) / 2.0
y2 = np.array(
    [94.2, 16.11, 14.81, 14.16, 13.36, 12.71, 12.17, 11.68, 11.25, 10.84, 9.04, 8.44, 7.82]) / 4.0
x = np.arange(1, len(y1)+1)

# Draw Line Chart
plt.plot(x, y1, '-', linewidth=1.5, label="Test Data 1")
plt.plot(x, y2, '-', linewidth=1.5, label="Test Data 2")

# 设置 Label
plt.xlabel('Epochs', fontproperties='Times New Roman')
plt.ylabel('Training Loss', fontproperties='Times New Roman')

# 设置图例位置
plt.legend(loc='upper right', frameon=True, fontsize=8)
plt.show()
# plt.savefig('./line_chart.jpg')

