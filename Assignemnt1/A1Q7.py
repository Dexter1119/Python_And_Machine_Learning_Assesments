############################################################################
#
# Name:         A1Q7.py
# Description:  program which check the number is divisible 5
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 7 
#
############################################################################


def DivisibleBy5(iNo):
    if(iNo % 5 == 0):
        return True
    else:
        return False


def main():
    print("Enter the Number :",end=" ")
    iValue = int(input())
    bRet = DivisibleBy5(iValue)
    if(bRet == True):
        print("The ",iValue, " is Divible by 5")
    else:
        print("The ",iValue, " is not Divible by 5")


if("__main__"==__name__):
    main()