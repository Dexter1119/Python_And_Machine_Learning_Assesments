#################################################################
#
# Name:         A1Q3.py
# Description:  Program which Add two Numbers given by user
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 3 
#
#################################################################


def Add(iNo1 , iNo2):
    iAns = iNo1 +iNo2
    return iAns


def main():
   
    print("Enter the First Number:",end=" ")
    iValue1 = int(input())

    print("Enter the Second Number:",end=" ")
    iValue2 = int(input())

    iRet = Add(iValue1,iValue2)
    print("The addition of two numbers is :",iRet)

if(__name__ == "__main__"):
    main()