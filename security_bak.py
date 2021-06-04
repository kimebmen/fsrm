import subprocess
import os
from fnmatch import fnmatch
from pathlib import Path


def security(s):
    out = [
        "Description",
        "Share",
        "Path",
        "source",
        "Path",
        "Source"
        "Template",
        "Quota",
        "Status",
        "Limit",
        "Limit",
        "Used",
        "Available",
        "Peek",
        "Usage",
        "Thresholds",
        "Warnings",
        "E-mail"
    ]
    s1 = subprocess.check_output(f'dirquota.exe q l /path:{s} /remote:kpcsgt-fs03', shell=True)
    # s1 = subprocess.check_output(f'dirquota.exe q l /path:D:\Shares-G\MKT\500-MKTExtended /remote:kpcsgt-fs03', shell=True)
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

    # new = result
    new = [result[1], result[4], result[7], result[14], result[16], result[17], result[18], result[20], result[21], result[22], result[24], result[25], result[28], result[29], result[30]]
    return new
    # return result
    
    # final=[]
    # for i in range(len(result)):
    # #     result1 = result.split(out)
    # #     print(result1)
    # # return result1
    #     if not any(result[i] in j for j in out):
    #         temp = result[i]
    #         final.append(temp)
    #     return final


print(security("D:\Shares-G\\MSD\\160"))


#-------------

    # final = []
    # for i in range(len(result)):
    #     match = fnmatch(result[i], "Quota*")
    #     if match:
    #         continue
    #     print(i)
    #     if not any(result[i] in j for j in out):
    #         temp = result[i]
    #         final.append(temp)
    #     return final

