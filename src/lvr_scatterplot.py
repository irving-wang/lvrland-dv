import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lvr_code import lvr_columns
from common.func import ping


sourcedir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
seasondir = '2014S4'
filename = 'A_lvr_land_A.CSV'
column = lvr_columns[22]  # '單價每平方公尺'

data = pd.read_csv('{0}\\{1}\\{2}'.format(
    sourcedir, seasondir, filename), encoding='utf-8')
data = data[column]

plen = len(data)
y = np.array(data / 10000.0 / ping)
x = np.linspace(0, plen, num=plen)
colors = np.random.rand(plen)
# area = np.pi * (15 * np.random.rand(plen))**2  # 0 to 15 point radiuses
area = np.pi * np.array([2 for n in range(plen)])
# print('area =', area)

plt.scatter(x, y[0:plen], s=area, c=colors, alpha=0.5)

plt.xlabel('房屋')
plt.ylabel('成交價 (萬/坪)')
plt.title('台北市成交價散布圖', fontproperties='KaiTi')

plt.show()
