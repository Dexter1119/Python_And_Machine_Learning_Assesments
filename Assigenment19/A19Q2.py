########################################################################
#
# File Name :   A19Q2.py
# Description:  Automation Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################
"""
File Created Successfully
Total Number of .doc Files renamed to .txt :  3

"""

import sys
import os

def RenameFileExtension(path,ext1,ext2):
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)
    
    flag = os.path.exists(path)
    if(flag == False):
        print("Directory Not Found")
        return

    flag = os.path.isdir(path)
    if(flag == False):
        print("Its File Not Directory")
        return

    fd = open("Demo2.txt",'a')
    fd.write("\n\n\nRenamed " + ext1 + " Files in the Given Directory:\n")

    iCount = 0

    for FolderName, SubFolderName , FileName in os.walk(path):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            if(fname.endswith(ext1)):
                iCount += 1

                fname2 = fname.replace(ext1,ext2)
                fname2 = os.path.join(FolderName,fname2)

                os.rename(fname,fname2)
                fd.write(fname +" to \t"+fname2  + "\n")

    fd.write("Total Number of "+ext1+" Files renamed to "+ext2+" : "+str(iCount))
    fd.close()

    print("File Created Successfully")
    print("Total Number of "+ext1+" Files renamed to "+ext2+" : ",iCount)

def main():
    if(len(sys.argv) != 4):
        if(len(sys.argv) == 2 ):
            if(sys.argv[1] == "-h" or sys.argv[1] == "-H"):
                print("This Script Accepts 3 Arguments")
                print("Usage : ScriptName DirectoryName Extension Extension")
                print("Example : Demo.py Demo.txt .txt")
                return
            elif(sys.argv[1] == "-u" or sys.argv[1] == "-U"):
                print("This Script rename the File of Given Extension and create its log file and returns Number of Files with Given Extension has been renamed")
                print("Usage : ScriptName DirectoryName Extension")
                print("Example : Demo.py Demo.txt .txt")
                return
    
        else:
            print("Invalid Arguments")
            return

    if(len(sys.argv) == 4):
        path = sys.argv[1]
        ext1 = sys.argv[2]
        ext2 = sys.argv[3]

        RenameFileExtension(path,ext1,ext2)

if(__name__ == "__main__"):
    main()