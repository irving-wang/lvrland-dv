"""
Simple demo of a scatter plot.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\cs\\Downloads\\OpenData\\2014S4\\A_lvr_land_A2.CSV', encoding='big5')
data = data['單價每平方公尺']

plen = len(data)
y = np.array(data)
x = np.linspace(0, plen, num=plen)
colors = np.random.rand(plen)
area = np.pi * (15 * np.random.rand(plen))**2  # 0 to 15 point radiuses
area = np.pi * np.array([2 for n in range(plen)])
# print('area =', area)
plt.scatter(x, y[0:plen], s=area, c=colors, alpha=0.5)
plt.show()
