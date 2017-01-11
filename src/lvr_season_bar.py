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

width = 0.35                         # the width of the bars: can also be len(x) sequence
opacity = 0.4
plt.rc('font', **cenv.rcfont)
plt.rc('axes', unicode_minus=False)
# plt.plot(x, np.array(ydata), label='台北市', color='blue', linewidth=2)
# plt.plot(x, np.array(fdata), label='新北市', color='red', linewidth=2)
p1 = plt.bar(x, np.array(ydata), width,  alpha=opacity,
             color='b',)
rects1 = plt.bar(x, np.array(ydata), width,
                 alpha=opacity,
                 color='b',
#                  yerr=std_men,
#                  error_kw=error_config,
                 label='台北市')

rects2 = plt.bar(x + width, np.array(fdata), width,
                 alpha=opacity,
                 color='r',
#                  yerr=std_women,
#                  error_kw=error_config,
                 label='新北市')
plt.legend()

plt.xticks(x, xdata)
plt.xlabel('(民國)年．季度', fontproperties=cenv.kai)
plt.ylabel('成交量', fontproperties=cenv.kai)
plt.title('雙北市成交量', fontproperties=cenv.kai_title)

plt.show()
