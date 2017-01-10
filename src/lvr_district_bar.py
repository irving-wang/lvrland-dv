import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common.func as cf
from lvr_code import lvr_code2county, lvr_county2code, lvr_columns

print(lvr_code2county)
print(lvr_county2code)
print(lvr_columns[1])

sourcedir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
seasondir = '2014S4'
filename = 'A_lvr_land_A.CSV'
column = lvr_columns[0] #'鄉鎮市區'

data = pd.read_csv('{0}\\{1}\\{2}'.format(sourcedir, seasondir, filename), encoding='utf-8')
print(data.columns)

dists = cf.count_keys(data['鄉鎮市區'])
print(dists)
width = 0.7       # the width of the bars: can also be len(x) sequence
opacity = 0.4

font = {'family': 'DFKai-SB'}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

ind = np.arange(len(dists.keys()))  # the x locations for the groups
p1 = plt.bar(ind, dists.values(), width,  alpha=opacity,
             color='b',)

plt.xlabel('鄉鎮市區')
plt.xticks(ind + width / 2., dists.keys(), fontproperties="SimHei")
plt.ylabel('成交量')
plt.title('台北市分區成交量圖', fontproperties='KaiTi')

plt.show()
