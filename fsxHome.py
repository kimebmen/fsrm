import subprocess
import re

def fsxHome():
    s1 = subprocess.check_output(f'dirquota.exe q l  /remote:kpcsgt-fsx', shell=True)
    s2 = s1.decode('utf-8')
    s2 = s2.split("\n\r")
    stringlist = s2[1:]

    FSRM = []
    for i in range(len(stringlist)):
        temp = stringlist[i].splitlines()
        Quota = []
        for j in range(len(temp)):
            tes = temp[j].replace('(', '').replace(')', '').split()
            Quota.append(tes)     
        FSRM.append(Quota)
    
    result = []
    for i in range(len(FSRM)-1):
        disk = {}
        try:
            disk["UsedPercent"] = FSRM[i][7][3]
            findLen = len(FSRM[i][1])
            FSRM[i][1] = " ".join(FSRM[i][1])
            FSRM[i][1] = re.sub('Quota Path: ','', str(FSRM[i][1]))
            disk["Path"] = FSRM[i][1]
            
            disk["SharePath"] = FSRM[i][3][-1]

            FSRM[i][6][1] = re.sub(',','', str(FSRM[i][6][1]))
            sizeLimit = FSRM[i][6][2]
            if sizeLimit == 'MB':
                n = float(FSRM[i][6][1])*0.001
                lval = '%.3f' %n 
                disk["Limit"] = lval
            elif sizeLimit == 'KB':
                n = float(FSRM[i][6][1])*0.001*0.001
                lval = '%.3f' %n 
                disk["Limit"] = lval
            elif sizeLimit == 'TB':
                n = float(FSRM[i][6][1])*1000
                lval = '%.0f' %n 
                disk["Limit"] = lval
            else:
                n = float(FSRM[i][6][1])
                lval = '%.2f' %n 
                disk["Limit"] = lval
            
            FSRM[i][7][1] = re.sub(',','', str(FSRM[i][7][1]))
            sizeUsed = FSRM[i][7][2]
            if sizeUsed == 'MB':
                m = float(FSRM[i][7][1])*0.001
                uval = '%.3f' %m
                disk["Used"] = uval
            elif sizeUsed == 'KB':
                m = float(FSRM[i][7][1])*0.001*0.001
                uval = '%.3f' %m
                disk["Used"] = uval
            elif sizeUsed == 'TB':
                m = float(FSRM[i][7][1])*1000
                uval = '%.2f' %m
                disk["Used"] = uval
            else:
                m = float(FSRM[i][7][1])
                uval = '%.2f' %m
                disk["Used"] = uval        

            FSRM[i][8][1] = re.sub(',','', str(FSRM[i][8][1]))
            sizeAvail = FSRM[i][8][2]
            if sizeAvail == 'MB':
                o = float(FSRM[i][8][1])*0.001
                aval = '%.3f' %o
                disk["Available"] = aval
            elif sizeAvail == 'KB':
                o = float(FSRM[i][8][1])*0.001*0.001
                aval = '%.3f' %o
                disk["Available"] = aval
            elif sizeAvail == 'TB':
                o = float(FSRM[i][8][1])*1000
                aval = '%.0f' %o
                disk["Available"] = aval
            else:
                o = float(FSRM[i][8][1])
                aval = '%.2f' %o
                disk["Available"] = aval
            
            # print(len(FSRM[i][7]))

            result.append(disk)    
    
        except:
            disk["UsedPercent"] = FSRM[i][6][3]
            FSRM[i][1] = " ".join(FSRM[i][1])
            FSRM[i][1] = re.sub('Quota Path: ','', str(FSRM[i][1]))
            # newPath = [FSRM[i][1]]
            # if newPath[1] == ' ' or newPath[3] == ' ':
            #     FSRM[i][1] = FSRM[i][1][0]+FSRM[i][1][2]+FSRM[i][1][4:]
                   
            disk["Path"] = FSRM[i][1]
            
            disk["SharePath"] = 'None'

            FSRM[i][5][1] = re.sub(',','', str(FSRM[i][5][1]))
            sizeLimit = FSRM[i][6][2]
            if sizeLimit == 'MB':
                n = float(FSRM[i][5][1])*0.001
                lval = '%.3f' %n 
                disk["Limit"] = lval
            elif sizeLimit == 'KB':
                n = float(FSRM[i][5][1])*0.001*0.001
                lval = '%.3f' %n 
                disk["Limit"] = lval
            elif sizeLimit == 'TB':
                n = float(FSRM[i][5][1])*1000
                lval = '%.0f' %n 
                disk["Limit"] = lval
            else:
                n = float(FSRM[i][5][1])
                lval = '%.2f' %n 
                disk["Limit"] = lval
            
            FSRM[i][6][1] = re.sub(',','', str(FSRM[i][6][1]))
            sizeUsed = FSRM[i][6][2]
            if sizeUsed == 'MB':
                m = float(FSRM[i][6][1])*0.001
                uval = '%.3f' %m
                disk["Used"] = uval
            elif sizeUsed == 'KB':
                m = float(FSRM[i][6][1])*0.001*0.001
                uval = '%.3f' %m
                disk["Used"] = uval
            elif sizeUsed == 'TB':
                m = float(FSRM[i][6][1])*1000
                uval = '%.2f' %m
                disk["Used"] = uval
            else:
                m = float(FSRM[i][6][1])
                uval = '%.2f' %m
                disk["Used"] = uval        

            FSRM[i][7][1] = re.sub(',','', str(FSRM[i][7][1]))
            sizeAvail = FSRM[i][8][2]
            if sizeAvail == 'MB':
                o = float(FSRM[i][7][1])*0.001
                aval = '%.3f' %o
                disk["Available"] = aval
            elif sizeAvail == 'KB':
                o = float(FSRM[i][7][1])*0.001*0.001
                aval = '%.3f' %o
                disk["Available"] = aval
            elif sizeAvail == 'TB':
                o = float(FSRM[i][7][1])*1000
                aval = '%.0f' %o
                disk["Available"] = aval
            else:
                o = float(FSRM[i][7][1])
                aval = '%.2f' %o
                disk["Available"] = aval
            
            # print(len(FSRM[i][7]))

            result.append(disk)



        
    
    # return FSRM[0]
    # return cleanFSRM[0]
    return result
    # return result


# print(fsxHome())

