import os
import pandas as pd
import matplotlib.pyplot as plt
import lvr_func as cf
import lvr_environment as cenv
from lvr_code import lvr_columns
from lvr_func import ping

sdir = cenv.datadir
column = lvr_columns[15]  # '建物移轉總面積平方公尺'
s1 = '2015S4'

data = pd.read_csv('{0}{sep}{1}{sep}{2}_lvr_land_A.CSV'.format(
    sdir, s1, 'A', sep=os.path.sep), encoding='utf-8')
data = data[column] * ping
# print(data)

# Data to plot
labels = '10坪以下', '10-20坪', '20-30坪', '30-40坪', '40-50坪', '50-60坪', '60-70坪', '70坪以上'
sizes = [cf.calrange(data, 0, 10), cf.calrange(data, 10, 20), cf.calrange(data, 20, 30), cf.calrange(
    data, 30, 40), cf.calrange(data, 40, 50), cf.calrange(data, 50, 60), cf.calrange(data, 60, 70), cf.calrange(data, 70, 10000)]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.0, 0.1, 0, 0.0, 0, 0, 0)  # explode 1st slice
print(sizes)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('台北市房屋成交面積', fontproperties=cenv.kai_title)
# plt.axis('equal')

plt.show()
