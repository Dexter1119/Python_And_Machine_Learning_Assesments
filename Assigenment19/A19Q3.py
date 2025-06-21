########################################################################
#
# File Name :   A19Q3.py
# Description:  Automation Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
#
########################################################################
"""

File Copy Successfully
Total Number of Files Copied are : 3

"""

import sys
import os
import shutil

def RenameFileExtension(path):
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

    Dir_Name = "CopyOF" + os.path.basename(path)

    location = r"C:\Users\Admin\Desktop\Assigenment19"
    Dir_Name = os.path.join(location, Dir_Name)

    os.mkdir(Dir_Name)

    src = path
    dest = Dir_Name

    


    fd = open("Demo3.txt",'a')
    fd.write("\n\nFiles Copied From "+path+" to "+Dir_Name+"\n")

    iCount = 0

    for FolderName, SubFolderName , FileName in os.walk(path):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            shutil.copy(fname,dest)
            iCount += 1
            fd.write(fname + "\n")
    

    fd.write("Total Number of Files Copied are : "+str(iCount))
    fd.close()
    print("File Copy Successfully")
    print("Total Number of Files Copied are : "+str(iCount))


def main():

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
                path = sys.argv[1]
                RenameFileExtension(path)
    
        else:
            print("Invalid Arguments")
            return

    

if(__name__ == "__main__"):
    main()