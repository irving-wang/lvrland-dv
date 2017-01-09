import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lvr.func as cf

data = pd.read_csv(
    'C:\\Users\\cs\\Downloads\\OpenData_output\\2014S4\\A_lvr_land_A.CSV', encoding='utf-8')
print(data.columns)
data = data['單價每平方公尺']

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
plt.show()

print('max =', max(y))
print('min =', min(y))

ndata = cf.remove_outlier(y, 100000, 1000000)

print('ndata.len =', len(ndata))
print(ndata)
