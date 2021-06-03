import subprocess
import os
from fnmatch import fnmatch
from pathlib import Path

def security(s):
    exclude = [
        "NT AUTHORITY\\SYSTEM",
        "SYSTEMS01\\Domain Admins"
        "BUILTIN\\Administrators",
        "BUILTIN\\Users",
        "CREATOR",
        "OWNER",
        "BUILTIN\\Administrators",
        "S-1-5-21-1999317001-1348472629-1808553963-16315",
        "S-1-5-21-143338819-2634011233-480148089-500"
    ]
    s1 = subprocess.check_output(f'icacls.exe "{s}"', shell=True)
    s2 = s1.decode('utf-8')
    decoded_string = s2.split(f"{s}")
    s4 = decoded_string[1]
    s4 = s4.split()
    stringlist = s4[0:-8]

    result = []
    for i in range(len(stringlist)):
        temp = stringlist[i]
        temp = temp.split(":")
        result.append(temp[0])

    # print(f"length result: {len(result)}")
    final = []
    for i in range(len(result)):
        match = fnmatch(result[i], "S-1-5*")
        if match:
            continue
        print(i)
        if not any(result[i] in j for j in exclude):
            temp = result[i]
            # print(f"temp: {temp}")
            t_match = fnmatch(result[i], "SYSTEMS01\\*")
            print(f"tmatch: {t_match}")
            if t_match:
                temp2 = temp.split("\\")
                perm = temp2[1]
                print(perm)
                final.append(perm)

    return final