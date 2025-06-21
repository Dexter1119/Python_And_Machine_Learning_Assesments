########################################################################
#
# File Name :   A16Q4.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
Enter the numbers:
12
12
23
45
33
12
23
34
112
32

Numbers in the file are:
12
12
23
45
33
12
23
34
112
32
"""
import os
import sys

def Count(path,BufferSize = 1024):

    fd = open("Number.txt",'w') 

    print("Enter the numbers:")
    for iCnt in range(10):
        fd.write(input()+"\n")

    fd.close()

    fd = open("Number.txt",'r')
    print("Numbers in the file are:",fd.read())

    fd.close()
    

    


def main():
    FileName = sys.argv[1]
    Count(FileName)
    

if(__name__ == "__main__"):
    main()