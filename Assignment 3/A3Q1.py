#################################################################
# 
#   File Name :   A3Q1.py
#   Description : problems on N Numbers
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        09/06/2025
#
#################################################################
"""
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130

"""

def AddElements(No):
    Arr = []
    iCnt = 0
    iSum = 0

    print("Enter the elements :")
    for iCnt in range (No):
        Arr.append(int(input()))
        

    
    for iCnt in range(No):
        iSum += Arr[iCnt]
    
    return iSum


def main():
    print("Enter the number of elemets:")
    No = int(input())

    iRet = 0
    iRet = AddElements(No)
    print("Addition of Elements is :",iRet)

if(__name__ == "__main__"):
    main()