#################################################################
#
# Name:         A1Q2.py
# Description:  Program which checks input is Even or Odd
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 2
#
#################################################################

def ChkNum(iNo):
    if(iNo % 2 == 0):
        return True
    else:
        return False


def main():
    iValue = 0
    print("ENter the number :")
    iValue = int(input())
    bRet = ChkNum(iValue)
    if(bRet == True):
        print("The number is Even")
    else:
        print("The number is Odd")

if(__name__ == "__main__"):
    main()
    