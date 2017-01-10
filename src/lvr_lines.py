import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lvr_code import lvr_columns
from common.func import ping, calaverage

sdir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
column = lvr_columns[22] #'單價每平方公尺'

ydata = []
# xdata = []
# index = 0
for f in os.listdir(sdir):
    fpath = sdir + os.path.sep+f
    if os.path.isdir(fpath):
        fname = '{}\\A_lvr_land_A.CSV'.format(fpath)
#         print(fname.format(fpath))
        data = pd.read_csv(fname, encoding='utf-8')
        data = data[column]/10000/ping
        data = calaverage(data)
        ydata.append(data)
#         xdata.append(f)
#         index+=1
#         print(index,'=>',data)
#     print(calaverage(data))

plen = len(ydata)
y = np.array(ydata)
# x = np.array(xdata)
x = np.linspace(0, plen, num=plen)

print('y.size =', y.size)
plt.plot(x, y[0:plen], color='blue', label='萬元/坪', linewidth=2)
plt.legend()

plt.xlabel('季度')
plt.ylabel('成交價 (萬/坪)')
plt.title('台北市成交價趨勢圖', fontproperties='KaiTi')

plt.show()
# for key,value in lvr_code2county.items():
#     print(key,value)