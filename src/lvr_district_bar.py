import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvr_func as cf
import lvr_environment as cenv
from lvr_code import lvr_columns

def getstrs(idata, le):
    data = []
    for v in idata:
        data.append(v[0:le])
    return data


sdir = cenv.datadir
column = lvr_columns[0]  # '鄉鎮市區'

data = pd.read_csv('{0}{sep}{1}{sep}{2}_lvr_land_A.CSV'.format(sdir, '2014S4', 'A', sep=os.path.sep)
                   , encoding='utf-8')
# print(data.columns)
dists = cf.count_keys(data[column])
print(dists)

width = 0.7                         # the width of the bars: can also be len(x) sequence
opacity = 0.4
plt.rc('font', **cenv.rcfont)
plt.rc('axes', unicode_minus=False)

x = np.arange(len(dists.keys()))    # the x locations for the groups
p1 = plt.bar(x, dists.values(), width,  alpha=opacity,
             color='b',)

plt.xticks(x + width / 2., getstrs(dists.keys(),2), fontproperties="SimHei")
plt.xlabel('鄉鎮市區', fontproperties=cenv.kai)
plt.ylabel('成交量', fontproperties=cenv.kai)
plt.title('台北市分區成交量圖', fontproperties=cenv.kai_title)

plt.show()
