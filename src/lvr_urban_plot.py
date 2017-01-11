import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvr_environment as cenv
from lvr_code import lvr_columns, get_roc_year
from lvr_func import ping, calaverage


def calcode_average(fpath, code):
    fname = '{0}\\{1}_lvr_land_A.CSV'.format(fpath, code)
    data = pd.read_csv(fname, encoding='utf-8')
    data = data[column] / 10000.0 / ping
    data = calaverage(data)
    return data


plt.rc('font', **cenv.rcfont)
plt.rc('axes', unicode_minus=False)

sdir = cenv.datadir
column = lvr_columns[22]  # '單價每平方公尺'

xdata = []
adata = []
fdata = []
hdata = []
bdata = []
ddata = []
edata = []
for f in os.listdir(sdir):
    fpath = sdir + os.path.sep + f
    if os.path.isdir(fpath):
        xdata.append(get_roc_year(f)[1:])
        adata.append(calcode_average(fpath, 'A'))
        fdata.append(calcode_average(fpath, 'F'))
        hdata.append(calcode_average(fpath, 'H'))
        bdata.append(calcode_average(fpath, 'B'))
        ddata.append(calcode_average(fpath, 'D'))
        edata.append(calcode_average(fpath, 'E'))

plen = len(adata)
x = np.linspace(0, plen, num=plen)

with plt.style.context('fivethirtyeight'):
    plt.plot(x, np.array(adata), label='台北', linewidth=2)
    plt.plot(x, np.array(fdata), label='新北', linewidth=2)
    plt.plot(x, np.array(hdata), label='桃園', linewidth=2)
    plt.plot(x, np.array(bdata), label='台中', linewidth=2)
    plt.plot(x, np.array(ddata), label='台南', linewidth=2)
    plt.plot(x, np.array(edata), label='高雄', linewidth=2)

plt.legend(loc='upper right', bbox_to_anchor=(1.0, 0.8), fontsize='medium')

plt.xticks(x, xdata)
plt.xlabel('年．季度(民國)', fontproperties=cenv.kai)
plt.ylabel('成交價 (萬/坪)', fontproperties=cenv.kai)
plt.title('六都房屋買賣成交價趨勢圖 ', fontproperties=cenv.kai_title)

plt.show()
