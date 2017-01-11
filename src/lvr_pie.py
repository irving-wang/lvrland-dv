import pandas as pd
import matplotlib.pyplot as plt
import common.func as cf
from lvr_code import lvr_columns
from common.func import ping


sourcedir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
seasondir = '2014S4'
filename = 'A_lvr_land_A.CSV'
column = lvr_columns[22]  # '單價每平方公尺'

data = pd.read_csv('{0}\\{1}\\{2}'.format(
    sourcedir, seasondir, filename), encoding='utf-8')
data = data[column] / 10000 / ping
print(len(data))

# Data to plot
labels = '20萬以下', '20-30萬', '30-40萬', '40-50萬', '50-60萬', '60-70萬', '70-80萬', '80萬以上'
sizes = [cf.calrange(data, 0, 20), cf.calrange(data, 20, 30), cf.calrange(data, 30, 40), cf.calrange(
    data, 40, 50), cf.calrange(data, 50, 60), cf.calrange(data, 60, 70), cf.calrange(data, 70, 80), cf.calrange(data, 80, 10000)]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.0, 0.0, 0, 0.1, 0, 0, 0.1)  # explode 1st slice
print(sizes)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('台北市房屋成交價格', fontproperties='KaiTi')
# plt.axis('equal')

plt.show()
