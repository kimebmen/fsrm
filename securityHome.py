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
    # print(s1)
    s2 = s1.decode('utf-8')
    s2 = s2.split("\n\r")
    # s2 = s2.splitlines()
    stringlist = s2[1:]
    # print(stringlist.split("\r\n"))

    FSRM = []
    for i in range(len(stringlist)):
        temp = stringlist[i].splitlines()
        Quota = []
        for j in range(len(temp)):
            tes = temp[j].split("  ")
<<<<<<< HEAD
            Quota.append(tes[-1])     
        FSRM.append(Quota)


    result = []
    for i in range(len(FSRM)-1):
        disk = {}
        # for j in range(len(FSRM[i])):
        disk["Path"] = FSRM[i][1].strip()
        disk["SharePath"] = FSRM[i][3].strip()
        disk["SourceTemplate"] = FSRM[i][4].strip()
        disk["limit"] = FSRM[i][6].strip()
        disk["Used"] = FSRM[i][7].strip()
        disk["Available"] = FSRM[i][8].strip()
        disk["Peak Usage"] = FSRM[i][9].strip()
        result.append(disk)

    return result
=======
            Quota.append(tes[-1])
        
        FSRM.append(Quota)
        # print(temp[1].split())
    print(FSRM)
>>>>>>> 21087b2ffa417ab75e9c8b807a8a2d6074cd11e5

print(securityHome())

