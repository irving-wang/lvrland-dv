import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvr_environment as cenv
from lvr_code import lvr_columns
from lvr_func import ping

sdir = cenv.datadir
column = lvr_columns[22]  # '單價每平方公尺'
s1 = '2014S4'

data = pd.read_csv('{0}{sep}{1}{sep}{2}_lvr_land_A.CSV'.format(
    sdir, s1, 'A', sep=os.path.sep), encoding='utf-8')
data = data[column] / 10000.0 / ping

plen = len(data)
y = np.array(data)
x = np.linspace(0, plen, num=plen)
colors = np.random.rand(plen)
# area = np.pi * (15 * np.random.rand(plen))**2  # 0 to 15 point radiuses
area = np.pi * np.array([2 for n in range(plen)])
# print('area =', area)

plt.scatter(x, y[0:plen], s=area, c=colors, alpha=0.5)

plt.xlabel('房屋', fontproperties=cenv.kai)
plt.ylabel('成交價 (萬/坪)', fontproperties=cenv.kai)
plt.title('台北市成交價散布圖', fontproperties=cenv.kai_title)

plt.show()
