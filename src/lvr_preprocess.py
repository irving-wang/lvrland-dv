import subprocess
import os
import string


def convert_file(sdir, tdir, name):
    sfile = sdir + os.path.sep + name
    if os.path.exists(sfile) and os.path.isfile(sfile):
        out = tdir + os.path.sep + name
        output = open(out, 'w')
        subprocess.Popen(['iconv', '-c', '-f', 'big5', '-t',
                          'utf-8', sfile], stdout=output)


sdir = 'C:\\Users\\cs\\Downloads\\OpenData'
tdir = 'C:\\Users\\cs\\Downloads\\OpenData_output'
if not os.path.exists(tdir):
    os.mkdir(tdir)

print(os.listdir(sdir))

for f in os.listdir(sdir):
    indir = sdir + os.path.sep + f
    if os.path.isdir(indir):
        outdir = tdir + os.path.sep + f
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        for n in string.ascii_uppercase[:26]:
            convert_file(indir, outdir, n + '_lvr_land_A.CSV')
    # print(n)


# print(f,'isfile', os.path.isfile(sdir+os.path.sep+f))

# output = open('C:\\Users\\cs\\Downloads\\OpenData\\2014S4\\B_lvr_land_A2.CSV', 'w')
# subprocess.Popen(['iconv', '-c', '-f', 'big5', '-t', 'utf-8' ,'C:\\Users\\cs\\Downloads\\OpenData\\2014S4\\B_lvr_land_A.CSV'], stdout=output)
