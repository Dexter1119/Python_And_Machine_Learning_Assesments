############################################################################
#
# Name:         A1Q10.py
# Description:  program which display length of its string on console.
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 10 
#
############################################################################

def StrLen(cStr):
    iCnt = 0
    for char in cStr:
        iCnt +=1
    return iCnt

def main():
    print("Enter the name :",end="")
    cValue = input()
    iRet = StrLen(cValue)
    print("Lenth of your name is :",iRet)

if("__main__"==__name__):
    main()