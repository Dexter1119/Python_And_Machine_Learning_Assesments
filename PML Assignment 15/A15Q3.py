########################################################################
#
# File Name :   A15Q3.py
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

def CopyFile(path):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    fd1 = open(path,'a')
        
    
    fd2 = open("demo.txt",'r')
    
    fd1.write(fd2.read())

    fd1.close()
    fd2.close()

    fd = open(path,'r')
    print('All contets in the copied file are :'+fd.read())

    fd.close()


def main():
    FileName = sys.argv[1]

    CopyFile(FileName)

    

if(__name__ == "__main__"):
    main()