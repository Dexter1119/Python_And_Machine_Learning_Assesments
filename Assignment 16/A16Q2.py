########################################################################
#
# File Name :   A16Q2.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
Input : Demo.txt
Display contents of Demo.txt on console.
"""
import os
import sys

def DisplayContents(path ):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)
    
    flag = os.path.exists(path)
    if(flag == False):
        print("File Not Found")
        return

    fd = open(path,'r')
    print("Data From the file is",fd.read())
    fd.close()

    


def main():
    FileName = sys.argv[1]
    DisplayContents(FileName)
    

if(__name__ == "__main__"):
    main()