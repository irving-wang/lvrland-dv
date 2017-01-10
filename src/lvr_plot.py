import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import common.func as cf
from lvr_code import lvr_columns
from common.func import ping

sourcedir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
seasondir = '2014S4'
filename = 'A_lvr_land_A.CSV'
column = lvr_columns[22] #'單價每平方公尺'

data = pd.read_csv('{0}\\{1}\\{2}'.format(sourcedir, seasondir, filename), encoding='utf-8')
data = data[column]/10000/ping

plen = 50
y = np.array(data)
x = np.linspace(0, plen, num=plen)
print('price sum =', cf.calsum(data))
print('price average =', cf.calaverage(data))
print('price average =', cf.calaverage_ping(data))

# print(np.nanmax(y))
print('y.size =', y.size)
plt.plot(x, y[0:plen], color='blue', label='price/m^2', linewidth=2)
plt.legend()

plt.xlabel('房屋')
plt.ylabel('成交價 (萬/坪)')
plt.title('台北市成交價圖', fontproperties='KaiTi')

plt.show()

print('max =', max(y))
print('min =', min(y))

ndata = cf.remove_outlier(y, 100000, 1000000)

print('ndata.len =', len(ndata))
print(ndata)
