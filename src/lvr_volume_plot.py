import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvr_environment as cenv
from lvr_code import get_roc_year


def fetch_data(fpath, code):
    fname = '{0}\\{1}_lvr_land_A.CSV'.format(fpath, code)
    data = pd.read_csv(fname, encoding='utf-8')
    return data


sdir = cenv.datadir

xdata = []
ydata = []
fdata = []
for f in os.listdir(sdir):
    fpath = sdir + os.path.sep + f
    if os.path.isdir(fpath):
        xdata.append(get_roc_year(f)[1:])
        ydata.append(len(fetch_data(fpath, 'A')))
        fdata.append(len(fetch_data(fpath, 'F')))

print(ydata)
plen = len(ydata)
x = np.linspace(0, plen, num=plen)

plt.plot(x, np.array(ydata), label='台北市', color='blue', linewidth=2)
plt.plot(x, np.array(fdata), label='新北市', color='red', linewidth=2)
plt.legend()

plt.xticks(x, xdata)
plt.xlabel('(民國)年．季度', fontproperties=cenv.kai)
plt.ylabel('成交量', fontproperties=cenv.kai)
plt.title('雙北市成交量趨勢圖', fontproperties=cenv.kai_title)

plt.show()
