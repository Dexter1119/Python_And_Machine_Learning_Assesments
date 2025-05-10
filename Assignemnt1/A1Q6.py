############################################################################
#
# Name:         A1Q6.py
# Description:  program which check number is positive or negative or zero
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 6 
#
############################################################################


def ChkPositiveNegative(iNo):
    if(iNo > 0):
        return 1
    elif(iNo < 0):
        return -1
    else:
        return 0


def main():
    print("Enter the number:" ,end=" ")
    iValue = int(input())
    iRet = ChkPositiveNegative(iValue)
    if(iRet == 1):
        print("The " ,iValue, " is Positive")
    elif(iRet == -1):
        print("The " ,iValue, " is Negative")
    else:
        print("The " ,iValue, " is Zero")


if("__main__" == __name__):
    main()