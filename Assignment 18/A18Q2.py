########################################################################
#
# File Name :   A18Q2.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################


"""
Input : Demo.txt
Display contents of Demo.txt on console.
"""
import os

def OpenFile(path):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    flag = os.path.exists(path)
    if(flag == False):
        fd = open(path,'w')
        fd.write("Hello This is pradhumnya ")
        fd.close()
    
    fd = open(path,'r')
    print("Contents in the file are:"+fd.read())
    fd.close()


def main():
    FileName = ""

    print("Enter the file name ")
    FileName = input()

    OpenFile(FileName)

    

if(__name__ == "__main__"):
    main()