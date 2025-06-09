#################################################################
# 
#   File Name :   A3Q2.py
#   Description : problems on N Numbers
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        09/06/2025
#
#################################################################
"""
maximum element
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56

"""

def MaxElement(No):
    Arr = []
    iCnt = 0
    iMax = 0

    print("Enter the elements :")
    for iCnt in range (No):
        Arr.append(int(input()))
        

    iMax = Arr[0]
    for iCnt in range(No):
       if (Arr[iCnt] > iMax):
            iMax = Arr[iCnt]
    
    return iMax


def main():
    print("Enter the number of elemets:")
    No = int(input())

    iRet = 0
    iRet = MaxElement(No)
    print("Maximum Element is :",iRet)

if(__name__ == "__main__"):
    main()