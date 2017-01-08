import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvr.func as cf

data = pd.read_csv('C:\\Users\\cs\\Downloads\\OpenData\\2014S4\\A_lvr_land_A2.CSV', encoding='big5')
print(data.columns)

dists = cf.count_keys(data['鄉鎮市區'])
print(dists)
width = 0.7       # the width of the bars: can also be len(x) sequence
opacity = 0.4

ind = np.arange(len(dists.keys()))  # the x locations for the groups
p1 = plt.bar(ind, dists.values(), width,  alpha=opacity,
                 color='b',)

plt.xlabel('鄉鎮市區')
plt.xticks(ind+width/2., dists.keys())
plt.ylabel('成交量')
plt.show()