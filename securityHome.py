import subprocess
import os
from fnmatch import fnmatch
from pathlib import Path
import re


def securityHome():
    exclude = [
        "Quotas on machine kpcsgt-fs03:",
        "Thresholds:",
    ]
    s1 = subprocess.check_output(f'dirquota.exe q l  /remote:kpcsgt-fs03', shell=True)
    s2 = s1.decode('utf-8')
    s2 = s2.split("\n\r")
    stringlist = s2[2:]
    tempS2 = s2
    print(len(stringlist))
    result = []
    for i in range(len(stringlist)):
        temp = stringlist[i]
        temp = temp.split("D:").split(":")
        print(temp[i])
        # result.append(temp1)

    # result1 = []
    # for i in range(len(result)):
    #     temp1 = result[i]
    #     temp1 = temp1.split(":")
    #     result1.append(temp1)
    
    # print(result1)
    # for i in range(len(result)):
    #     del result[i][1]


# quotapath, %used, limit, quotatype, source template
        


    return result[0][1]

print(securityHome())

