from re import sub
import subprocess

def security(s):

    s1 = subprocess.check_output(f'dirquota.exe q l /path:"{s}" /remote:kpcsgt-fs03', shell=True)  
    s2 = s1.decode('utf-8')
    s2 = s2.split("\n\r")
    stringlist = s2[1:]
    # print(stringlist)
    
    FSRM = []
    for i in range(len(stringlist)):
        temp = stringlist[i].splitlines()
        Quota = []
        for j in range(len(temp)):
            tes = temp[j].split("  ")
            Quota.append(tes[-1])     
        FSRM.append(Quota)

    result = []
    for i in range(len(FSRM)-1):
        disk = {}
        # for j in range(len(FSRM[i])):
        disk["Path"] = FSRM[i][1].strip()
        disk["SharePath"] = FSRM[i][3].strip()
        disk["SourceTemplate"] = FSRM[i][4].strip()
        disk["Limit"] = FSRM[i][6].strip()
        disk["Used"] = FSRM[i][7].strip()
        disk["Available"] = FSRM[i][8].strip()
        disk["PeakUsage"] = FSRM[i][9].strip()
        result.append(disk)

    return result

# print(security("D:\\Shares-G\\MKT\\500-MKTExtended"))

    