########################################################################
#
# File Name :   A15Q1.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
Input : Demo.txt
Check whether Demo.txt exists or not.

"""
import os

def CheckExist(path):
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    return os.path.exists(path)

def main():
    FileName = ""
    print("Enter the file name ")
    FileName = input()

    bRet = CheckExist(FileName)
    if(bRet == True):
        print("The File Exists")
    else:
        print("FIle Doesnt exist")

if(__name__ == "__main__"):
    main()