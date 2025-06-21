########################################################################
#
# File Name :   A16Q6.py
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

def CopyFile(path1,path2,BufferSize = 1024):

    flag = os.path.isabs(path1)
    if(flag == False):
        path = os.path.abspath(path1)
    
    flag = os.path.exists(path1)
    if(flag == False):
        print("Source file not found")
        return
    
    flag = os.path.isabs(path2)
    if(flag == False):
        path = os.path.abspath(path2)
    
    flag = os.path.exists(path2)
    if(flag == False):
        fd = open(path2,'x')
        fd.close()


    fd1 = open(path1,'r') 
    fd2 = open(path2,'w')

    Buffer = fd1.read(BufferSize)
    while(len(Buffer) > 0):
        fd2.write(Buffer)
        Buffer = fd1.read(BufferSize)

    fd1.close()
    fd2.close()
            
    


def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]
    CopyFile(FileName1,FileName2)
    

if(__name__ == "__main__"):
    main()