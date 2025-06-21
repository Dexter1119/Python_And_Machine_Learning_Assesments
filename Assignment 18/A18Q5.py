########################################################################
#
# File Name :   A18Q5.py
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
import sys

def CountFrequency(path , str,BufferSize = 1024):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    flag = os.path.exists(path)
    if(flag == False):
        return

    fd = open(path,'r')
    
    iCount = 0

    Buffer = fd.read(BufferSize)
    while(len(Buffer) > 0):
        word = ""
        for i in Buffer:
            if(i == " "):
                word = ""

            elif(i != " "):
                word = word + i
            
            if(word == str):
                iCount += 1


        Buffer = fd.read(BufferSize)
    
    fd.close()
    return iCount



def main():
    FileName = sys.argv[1]
    Name = sys.argv[2]
    
    Ret = CountFrequency(FileName,Name)
    print("The frequency if the "+Name+" is:",Ret)

    

if(__name__ == "__main__"):
    main()