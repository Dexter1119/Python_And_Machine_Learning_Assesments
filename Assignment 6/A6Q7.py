#####################################################################
#
# File :        A6Q7.py
# Description : Program to Print Triangle Pattern using Nested Loops
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

*
* *
* * *
* * * *

"""
def FindMax(Arr):

    if(Arr == None):
        return -1

    iMax = 0
    iCnt = 0

    iMax = Arr[0]
    for iCnt in range(len(Arr)):
        if(Arr[ iCnt] > iMax):
            iMax = Arr[ iCnt]

    return iMax
def main():

    List = []
    iNo = 0
    iTemp = 0
    
    print("enter the number of elements:",end =" ")
    iNo = int(input())
    if(iNo < 0):
        print("Enter the correct number of elements")

    print("Enter the number of Elements")
    for i in range(iNo):
        iTemp = int(input())
        List.append(iTemp)


    iRet = FindMax(List)
    if(iRet == -1):
        print("Something went wrong")
        return

    print("Maximum Element in Array is:",iRet)

if(__name__ == "__main__"):
    main()