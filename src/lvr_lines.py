import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lvr_code import lvr_columns, lvr_6city
from common.func import ping, calaverage
from matplotlib.font_manager import FontProperties

fname = '{cur}{sep}..{sep}fonts{sep}{font}'.format(cur=os.getcwd(),sep=os.path.sep, font='mingliu.ttc')
font = FontProperties(fname=fname, size=12)
print(font.get_name())
font1 = {'family': font.get_name(), 'size': '10'} # DFKai-SB
plt.rc('font', **font1)
plt.rc('axes', unicode_minus=False)

sdir = '..' + os.path.sep + 'rawdata'
column = lvr_columns[22]  # '單價每平方公尺'


def calcode_average(fpath, code):
    fname = '{0}\\{1}_lvr_land_A.CSV'.format(fpath, code)
    data = pd.read_csv(fname, encoding='utf-8')
    data = data[column] / 10000 / ping
    data = calaverage(data)
    return data


xdata = []
adata = []
fdata = []
# hdata = []
# bdata = []
# ddata = []
# edata = []
# data6 = {}
for f in os.listdir(sdir):
    fpath = sdir + os.path.sep + f
    if os.path.isdir(fpath):
        xdata.append(f[2:])
        # for code in lvr_6city.keys:
        adata.append(calcode_average(fpath, 'A'))
        fdata.append(calcode_average(fpath, 'F'))
        # hdata.append(calcode_average(fpath, 'H'))
        # bdata.append(calcode_average(fpath, 'B'))
        # ddata.append(calcode_average(fpath, 'D'))
        # edata.append(calcode_average(fpath, 'E'))
        # print(f, ydata)

plen = len(adata)
# h = np.array(hdata)
x = np.linspace(0, plen, num=plen)

# y = np.array(adata)
# print('y.size =', y.size)
with plt.style.context('fivethirtyeight'):
    plt.plot(x, np.array(adata)[0:plen], label='台北市', linewidth=2)
    plt.plot(x, np.array(fdata)[0:plen], label='新北市', linewidth=2)
    # plt.plot(x, np.array(hdata)[0:plen], label='桃園市', linewidth=2)
    # plt.plot(x, np.array(bdata)[0:plen], label='台中市', linewidth=2)
    # plt.plot(x, np.array(ddata)[0:plen], label='台南市', linewidth=2)
    # plt.plot(x, np.array(edata)[0:plen], label='高雄市', linewidth=2)

plt.xticks(x, xdata)
plt.legend()

plt.xlabel('季度')
plt.ylabel('成交價 (萬/坪)')
plt.title('雙北市成交價趨勢圖', fontproperties=font)

plt.show()
# for key,value in lvr_code2county.items():
#     print(key,value)
