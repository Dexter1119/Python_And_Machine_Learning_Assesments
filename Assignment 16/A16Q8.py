########################################################################
#
# File Name :   A16Q8.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
copy content from file to file
"""
import os
import sys

def CleanFile(path,BufferSize = 1024):

    
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    

    fd1 = open(path,'r')
    fd2 = open("Cleaned.txt",'w')

    Buffer = fd1.read(BufferSize)
    while(len(Buffer) > 0):
        for i in Buffer:
            if(i == " " or i == "\n"):
                continue

            elif(i != " " or i != "\n"):
                fd2.write(i)
           
        Buffer = fd1.read(BufferSize)
        
    
   
    fd1.close()
    fd2.close()
    


def main():
    FileName1 = sys.argv[1]
    
    CleanFile(FileName1)
    

if(__name__ == "__main__"):
    main()