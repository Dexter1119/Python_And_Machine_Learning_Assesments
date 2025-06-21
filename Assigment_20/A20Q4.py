########################################################################
#
# File Name :   A20Q3.py
# Description:  Automation Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################

import hashlib
import os
import sys
import time

def FindChecksum(filename,BufferSize=1024):

    fd = open(filename, "rb")
    hobj = hashlib.md5()

    Buffer = fd.read(BufferSize)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fd.read(BufferSize)

    fd.close()
    return hobj.hexdigest()
   
    
def FindDuplicate(path):
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
    
    fd = open("DuplicateDeleteLog2.txt",'a')
    fd.write("\n\nDeleted Files in the directory:"+path+"\n")

    duplicate = {}
    start = time.time()
    for FolderName , SubFolderName , FileName in os.walk(path):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = FindChecksum(fname)

            if CheckSum in duplicate:
                duplicate[CheckSum].append(fname)

            else:
                duplicate[CheckSum] = [fname]

    
    Duplicate = lambda x : len(x) > 1

    Result = filter(Duplicate,duplicate.values())

    Count = 0
    iCnt = 0
    
    for Value in Result:
        for SubValue in Value:
            Count += 1
            if(Count > 1):
                iCnt += 1
                fd.write("Deleted File Name:"+SubValue+"\n")
                os.remove(SubValue)
        Count = 0

    end = time.time()

    requiredT = end - start
    fd.write("The Time required for the execution is :"+str(requiredT))
    fd.write("Number Of Deleted Files are: " + str(iCnt) + "\n")            
    fd.close()
    print("The Time required for the execution is :",requiredT)
    print("Number Of Deleted Files are: ",iCnt)      


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
            FindDuplicate(path)
        


            

   

    else:
        print("Invalid Arguments")
        return





if(__name__ == "__main__"):
    main()