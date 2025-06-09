#################################################################
# 
#   File Name :   A2Q8.py
#   Description : Program is used to display pattern
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 5187934     Output : 7

"""

def CountDigits(No):
    iCnt = 0
    while(No != 0):
        No = No // 10
        iCnt = iCnt + 1

    return iCnt


def main():
    No1 = 0
    
    print("Enter the number:",end=" ")
    No1 = int(input())

    iRet = 0
    iRet = CountDigits(No1)
    print("Number of Digits are : ", iRet)

  

if("__main__" == __name__):
    main()