########################################################################
#
# File Name :   A20Q1.py
# Description:  Automation Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################

import hashlib
import os
import sys

def FindChecksum(filename,BufferSize=1024):

    fd = open(filename, "rb")
    hobj = hashlib.md5()

    Buffer = fd.read(BufferSize)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fd.read(BufferSize)

    fd.close()
    return hobj.hexdigest()
   
    
def CheckSum(path):
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    flag = os.path.exists(path)
    if(flag == False):
        print("Directory Not Exists")
        return 
    flag = os.path.isdir(path)
    if(flag == False):
        print("Its Not Directory")
        return
    
    fd = open("CheckSumLog.txt",'a')
    fd.write("\n\nCheckSum of the file in the directory:"+path+"\n")

    for FolderName , SubFolderName , FileName in os.walk(path):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = FindChecksum(fname)

            fd.write("File Name:"+os.path.basename(fname)+"\nCheckSum:"+CheckSum+"\n\n")
            print("File Name:"+os.path.basename(fname)+"\nCheckSum:"+CheckSum+"\n\n")
    

    fd.close()


def main():
    if(len(sys.argv) == 2 ):
        if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
            print("This Script Accepts 2 Arguments")
            print("Usage : ScriptName DirectoryName")
            print("Try To Provide Absolute Path")
            return
        elif(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
            print("This Script calculate the checkSum of the files in give Directoryy ")
            print("Usage : ScriptName DirectoryName")
            return
        else:
            path = sys.argv[1]
            CheckSum(path)
        


            

   

    else:
        print("Invalid Arguments")
        return





if(__name__ == "__main__"):
    main()