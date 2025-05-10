############################################################################
#
# Name:         A1Q9.py
# Description:  program which display first n even numbers on console.
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 9 
#
############################################################################


def DisplayEven(iNo):
    for i in range(2,2 * iNo + 1,2):
        print(i,end=" ")


def main():
    print("Enter the number:",end="")
    iValue = int(input())
    DisplayEven(iValue)

if("__main__"==__name__):
    main()