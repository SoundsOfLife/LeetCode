import sys,os

"""
A script to rename file
"""

fileList = os.listdir(os.getcwd())
for file in fileList:
    s = file.split("-")
    if s.__len__() == 2:
        le = 4 - len(s[0])
        name = le * '0'+ s[0]+ "-" + s[1]
        print(name)
        os.rename(os.path.join(path,file),os.path.join(path,name)
