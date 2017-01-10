import pandas as pd
import os
import string

def dfconcat(sdir, fname):
    dflist = []
    for f in os.listdir(sdir):
        path = sdir + os.path.sep + f
        if os.path.isdir(path):
            path = path + os.path.sep + fname
            # print(path)
            if os.path.exists(path):
                df = pd.read_csv(path)
                dflist.append(df)
    return pd.concat(dflist)

sdir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
tdir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
for n in string.ascii_uppercase[:26]:
    fname = n + '_lvr_land_A.CSV'
    dfall = dfconcat(sdir, fname)
    dfall.to_csv(tdir + os.path.sep + fname)
# dflist = []
# for f in os.listdir(sdir):
#     path = sdir+os.path.sep+f
#     if os.path.isdir(path):
#         path = path + os.path.sep+'A_lvr_land_A.CSV'
#         #print(path)
#         df = pd.read_csv(path)
#         dflist.append(df)
# 
# print(len(dflist))
# dfall = pd.concat(dflist)
# print(dfall.head())
print(dfall.describe())
# dfall.to_csv('A_lvr_land_A.csv')
