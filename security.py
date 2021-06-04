import subprocess
from fnmatch import fnmatch
from pathlib import Path


def security(s):
    s1 = subprocess.check_output(f'dirquota.exe q l /path:{s} /remote:kpcsgt-fs03', shell=True)
    s2 = s1.decode('utf-8')
    decoded_string = s2.split(f"{s}")
    s4 = decoded_string[1]
    s4 = s4.split()
    stringlist = s4[0:]

    result = []
    for i in range(len(stringlist)):
        temp = stringlist[i]
        temp = temp.split(":")
        result.append(temp[0])

    new = [result[1], result[4], result[7], result[14], result[16], result[17], result[18], result[20], result[21], result[22], result[24], result[25], result[28], result[29], result[30]]
    return new
# print(security("D:\Shares-G\\MSD\\160"))


