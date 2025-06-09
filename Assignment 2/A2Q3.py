#################################################################
# 
#   File Name :   A2Q3.py
#   Description : Program is used to find the Factorial
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 5
Output :
    120
"""


def factorial(No):
    if(No < 0):
        No = -No

    iCnt = 0
    iFact = 1

    for iCnt in range(1,No+1):
        iFact = iFact * iCnt
    return iFact

def main():
    No = 0
    print("Enter Number:",end=" ")
    No = int(input())

    iRet = 0
    iRet = factorial(No)
    print("Factorial is : ", iRet)


if("__main__" == __name__):
    main()