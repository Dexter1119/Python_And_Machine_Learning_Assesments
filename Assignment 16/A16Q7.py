########################################################################
#
# File Name :   A16Q7.py
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

def CopyFile(path,BufferSize = 1024):

    
    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)

    fd1 = open(path,'a') 
    myDict = {}
    
    print("enter the number of student you wanna display")
    iNo = int(input())

    for i in range(iNo):
        print("ENter the name of student:")
        sname = input()
        
        print("Enter the marks of the student:")
        mark = int(input())

        myDict[sname] = mark

    fd1.write(str(myDict))
    fd1.close()

    fd1 = open(path,'r')
    fd2 = open("Scholar.txt",'w')

    Buffer = fd1.read(BufferSize)
    while(len(Buffer) > 0):
        mydict = dict(Buffer)
        for i in mydict:
            if(mydict.values([i]) >= 75):
                fd2.write(name + "\n")

        Buffer = fd1.read(BufferSize)

    fd1.close()
    fd2.close()
    


def main():
    FileName1 = sys.argv[1]
    
    CopyFile(FileName1)
    

if(__name__ == "__main__"):
    main()