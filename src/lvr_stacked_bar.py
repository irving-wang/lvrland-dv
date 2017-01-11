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


def get_values(dists, keys):
    data = []
    for k in keys:
        data.append(dists[k])
    print(data)
    return data


sdir = cenv.datadir
column = lvr_columns[0]  # '鄉鎮市區'
s1 = '2014S4'
s2 = '2015S4'

data = pd.read_csv('{0}{sep}{1}{sep}{2}_lvr_land_A.CSV'.format(
    sdir, s1, 'A', sep=os.path.sep), encoding='utf-8')
data2 = pd.read_csv('{0}{sep}{1}{sep}{2}_lvr_land_A.CSV'.format(
    sdir, s2, 'A', sep=os.path.sep), encoding='utf-8')

dists = cf.count_keys(data[column])
dists2 = cf.count_keys(data2[column])
keys = dists.keys()
print(keys)
print(dists)
print(dists2)

width = 0.7       # the width of the bars: can also be len(x) sequence
opacity = 1.0

x = np.arange(len(dists.keys()))  # the x locations for the groups
p1 = plt.bar(x, get_values(dists, keys), width, alpha=opacity, color='b')
p2 = plt.bar(x, get_values(dists2, keys), width, color='r', alpha=opacity)

plt.xticks(x + width / 2., getstrs(dists.keys(), 2), fontproperties=cenv.font)
plt.xlabel('鄉鎮市區', fontproperties=cenv.kai)
plt.ylabel('成交量', fontproperties=cenv.kai)
plt.title('台北市分區成交量圖', fontproperties=cenv.kai_title)
plt.legend((p1[0], p2[0]), (s1, s2))

plt.show()
