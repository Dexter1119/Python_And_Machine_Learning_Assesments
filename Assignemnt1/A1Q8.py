############################################################################
#
# Name:         A1Q8.py
# Description:  program which print n number of “*” on console.
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 8 
#
############################################################################



def DisplayStar(iNo):
    for i in range(iNo):
        print("*",end=" ")

def main():
    print("Enter the Number:",end=" ")
    iValue = int(input())
    DisplayStar(iValue)


if("__main__"==__name__):
    main()