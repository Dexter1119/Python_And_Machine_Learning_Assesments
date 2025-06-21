########################################################################
#
# File Name :   A16Q1.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
program to create a text file named student.txt and write the
names of 5 students into it.

Enter the name of the student:
rahul
ankita
neel
lokesh
kartik

Your Entered names were:
rahul
ankita
neel
lokesh
kartik
"""
import os
import sys

def AddEntry(path ):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

       
    fd = open(path,'x')
    print("Enter the name of the student:")
    for iCnt in range(1,6):
        fd.write(input()+"\n")
    
    fd.close()

    fd = open(path,'r')
    print("Your Entered names were:",fd.read())
    fd.close()

    


def main():
    FileName = sys.argv[1]
    AddEntry(FileName)
    

if(__name__ == "__main__"):
    main()