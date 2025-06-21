########################################################################
#
# File Name :   A16Q2.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
Input : hello.txt

Output :
    The Number of lines are: 5
    The Number of words are: 5
    The Number of character are: 32
"""
import os
import sys

def Count(path,BufferSize = 1024):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)
    
    flag = os.path.exists(path)
    if(flag == False):
        print("File Not Found")
        return

    fd = open(path,'r')
    Buffer = fd.read(BufferSize)
    iCountC = 0
    iCountW = 0
    iCountL = 0
    while(len(Buffer) > 0):

        word = ""
        for i in Buffer:

            iCountC += 1

            if(i == " " or i == "\n"):
                iCountW += 1
                word = ""

            elif(i != " "):
                word = word + i
            
            if( i == "\n"):
                iCountL += 1

        Buffer = fd.read(BufferSize)

    print("The Number of lines are:",iCountL)       
    print("The Number of words are:",iCountW)       
    print("The Number of character are:",iCountC)       


    fd.close()

    


def main():
    FileName = sys.argv[1]
    Count(FileName)
    

if(__name__ == "__main__"):
    main()