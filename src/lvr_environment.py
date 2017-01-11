import os
from matplotlib.font_manager import FontProperties

fname = '{cur}{sep}..{sep}fonts{sep}{font}'.format(cur=os.getcwd(),sep=os.path.sep, font='msyh.ttc')
font = FontProperties(fname=fname, size=12)
kname = '{cur}{sep}..{sep}fonts{sep}{font}'.format(cur=os.getcwd(),sep=os.path.sep, font='kaiu.ttf')
kai = FontProperties(fname=kname, size=12)
kai_title = FontProperties(fname=kname, size=14)
print(fname, font.get_name())
rcfont = {'family': font.get_name(), 'size': '10'} # DFKai-SB

datadir = '..' + os.path.sep + 'rawdata'
print(datadir)