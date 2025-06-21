########################################################################
#
# File Name :   A16Q5.py
# Description:  File Handling Assigenment
# Author:       Pradhumnya Changdev Kalsait
# Date:         20/06/2025
#
########################################################################


"""
lines containing grater than 5 words: Python is powerful and easy to learn.

lines containing grater than 5 words: You are doing a great job, keep going!

lines containing grater than 5 words: AI is the future of many industries.

lines containing grater than 5 words: Read every line carefully and understand it.

"""
import os
import sys

def ReadLine(path,BufferSize = 1024):

    flag = os.path.isabs(path)
    if(flag == False):
        path = os.path.abspath(path)
    
    flag = os.path.exists(path)
    if(flag == False):
        fd = open(path,'x')
        fd.close()

    fd = open(path,'r') 

    Buffer = fd.readline()
    iCount = 0
    while(len(Buffer) > 0):
        
        word = ""
        for i in Buffer:
            if(i == " "):
                word = ""
                iCount += 1
            
        if(iCount > 5 ):
            print("lines containing grater than 5 words:",Buffer)
        
        iCount = 0
        Buffer = fd.readline()
    
    fd.close()
            
    


def main():
    FileName = sys.argv[1]
    ReadLine(FileName)
    

if(__name__ == "__main__"):
    main()