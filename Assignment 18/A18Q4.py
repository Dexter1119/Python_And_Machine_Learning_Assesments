########################################################################
#
# File Name :   A18Q4.py
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
import hashlib

def CalculateCheckSum(FileName,BufferSize = 1024):
    Fd = open(FileName , 'rb')

    hobj = hashlib.md5()
    
    Buffer = Fd.read(BufferSize)
    while(len(Buffer) > 0 ):
        hobj.update(Buffer)
        Buffer = Fd.read(BufferSize)

    Fd.close()

    return hobj.hexdigest()



def CopyFile(path1 , path2):

    flag = os.path.isabs(path1)
    if(flag == False):
        path = os.path.abspath(path1)

    flag = os.path.exists(path1)
    if(flag == False):
        return

    flag = os.path.isabs(path2)
    if(flag == False):
        path = os.path.abspath(path2)

    flag = os.path.exists(path2)
    if(flag == False):
        return
        
    
    CheckSum1 = CalculateCheckSum(path1)
    CheckSum2 = CalculateCheckSum(path2)

    return (CheckSum1 == CheckSum2)


def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    ret = CopyFile(FileName1,FileName2)
    if(ret == True):
        print("Files Contents are exactly same")
    else:
        print("These are different files")


    

if(__name__ == "__main__"):
    main()