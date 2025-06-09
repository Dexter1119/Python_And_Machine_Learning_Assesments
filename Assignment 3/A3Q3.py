#################################################################
# 
#   File Name :   A3Q3.py
#   Description : problems on N Numbers -> Find Minimum
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        09/06/2025
#
#################################################################
"""
maximum element
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 4

"""

def MaxElement(Arr):
    
    iCnt = 0
    iMin = 0

    iMin = Arr[0]
    for iCnt in range(len(Arr)):
       if (Arr[iCnt] < iMin):
            iMin = Arr[iCnt]
    
    return iMin


def main():
    print("Enter the number of elemets:")
    No = int(input())

    Arr = []

    print("Enter the elements :")
    for iCnt in range (No):
        Arr.append(int(input()))
        


    iRet = 0
    iRet = MaxElement(Arr)
    print("Minimum Element is :",iRet)

if(__name__ == "__main__"):
    main()