########################################################################
#
# File Name :   A19Q1.py
# Description:  Automation Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################
"""
File Created Successfully
Total Number of .c Files are :  206
"""

import sys
import os

def FindFile(path,ext):
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)
    
    flag = os.path.exists(path)
    if(flag == False):
        print("Directory Not Found")
        return

    flag = os.path.isdir(path)
    if(flag == False):
        print("Its File Not Directory")
        return

    fd = open("Demo.txt",'a')
    fd.write(ext+"Files in the Given Directory Are:\n")
    iCount = 0

    for FolderName, SubFolderName , FileName in os.walk(path):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            if(fname.endswith(ext)):
                iCount += 1
                fd.write(fname + "\n")

    fd.write("Total Number of "+ext+"Files are : "+str(iCount))
    fd.close()

    print("File Created Successfully")
    print("Total Number of "+ext+" Files are : ",iCount)

def main():
    if(len(sys.argv) != 3):
        if(len(sys.argv) == 2 ):
            if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
                print("This Script Accepts 2 Arguments")
                print("Usage : ScriptName DirectoryName Extension")
                print("Example : Demo.py Demo.txt .txt")
                return
            elif(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
                print("This Script returns Number of Files with Given Extension and create its log file")
                print("Usage : ScriptName DirectoryName Extension")
                print("Example : Demo.py Demo.txt .txt")
                return
    
        else:
            print("Invalid Arguments")
            return

    if(len(sys.argv) == 3):
        path = sys.argv[1]
        ext = sys.argv[2]

        FindFile(path,ext)

if(__name__ == "__main__"):
    main()