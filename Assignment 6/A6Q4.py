###########################################################
#
# File :        A6Q4.py
# Description : Find Factorial
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################

"""

Expected Input:
Enter a number: 5

Expected Output:
Factorial of 5 is: 120

"""
def Factorial(No):
    iCnt = 1
    iFact = 1
    

    for iCnt in range(1,No+1,1):
        iFact *= iCnt

    return iFact


def main():

    No = 0
    print("Enter The number :",end = " ")
    No = int(input())

    iRet = 0
    iRet = Factorial(No)
    print("The Factorial of", No ," is:",iRet)


if(__name__ == "__main__"):
    main()