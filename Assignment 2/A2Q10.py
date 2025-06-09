#################################################################
# 
#   File Name :   A2Q10.py
#   Description : Add The Digits in a Number
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 5187934     Output : 7

"""

def AddDigits(No):
    iDigit = 0
    iSum = 0
    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10
        

    return iSum


def main():
    No1 = 0
    
    print("Enter the number:",end=" ")
    No1 = int(input())

    iRet = 0
    iRet = AddDigits(No1)
    print("Summation of Digits are : ", iRet)

  

if("__main__" == __name__):
    main()