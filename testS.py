import re
s = "D : \\ sa", "asd", "qwe"

string = " ".join(s)
string = re.sub("asd qwe", '',string)
# string = re.sub(' ','',string)
string = string[0]+string[2]+string[4:]
print(string)


