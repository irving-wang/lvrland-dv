import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common.func as cf
from lvr_code import lvr_columns

sourcedir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
seasondir = '2014S4'
seasondir2 = '2015S4'
filename = 'A_lvr_land_A.CSV'
column = lvr_columns[0] #'鄉鎮市區'

data = pd.read_csv('{0}\\{1}\\{2}'.format(sourcedir, seasondir, filename), encoding='utf-8')
data2 = pd.read_csv('{0}\\{1}\\{2}'.format(sourcedir, seasondir2, filename), encoding='utf-8')

dists = cf.count_keys(data[column])
# dists = sorted(dists.items())
# print(type(dists))
dists2 = cf.count_keys(data2[column])
# dists2 = sorted(dists2.items(), key=operator.itemgetter(0))
print(dists)
print(dists2)
width = 0.7       # the width of the bars: can also be len(x) sequence
opacity = 1.0
ind = np.arange(len(dists.keys()))  # the x locations for the groups

# N = 5
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (25, 32, 34, 20, 25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
# ind = np.arange(N)    # the x locations for the groups
# width = 0.35       # the width of the bars: can also be len(x) sequence

# p1 = plt.bar(ind, menMeans, width, color='r', yerr=menStd)
p1 = plt.bar(ind, dists.values(), width,  alpha=opacity,
             color='b',)
p2 = plt.bar(ind, dists2.values(), width, color='r', alpha=opacity)
#              bottom=menMeans, yerr=womenStd)
plt.xlabel('鄉鎮市區')
plt.xticks(ind + width / 2., dists.keys(), fontproperties="SimHei")
plt.ylabel('成交量')
plt.title('台北市分區成交量圖', fontproperties='KaiTi')
plt.legend((p1[0], p2[0]), (seasondir, seasondir2))

# plt.ylabel('Scores')
# plt.title('Scores by group and gender')
# plt.xticks(ind + width/2., ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.yticks(np.arange(0, 81, 10))

plt.show()
