#################################################################
# 
#   File Name :   A2Q4.py
#   Description : Program is used to find Addition of Factors
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 12 Output : 16 (1+2+3+4+6)

"""

def AddFactors(No):
    if(No < 0):
        No = -No

    iCnt = 0
    iSum = 0

    for iCnt in range(1,int(No/2+1)):
        if(No % iCnt == 0):
            iSum = iSum + iCnt
    return iSum
   

def main():
    No = 0
    print("Enter Number:",end=" ")
    No = int(input())

    iRet = 0
    iRet = AddFactors(No)
    print("The Summation of all factors of", No, " is : ", iRet)


if("__main__" == __name__):
    main()