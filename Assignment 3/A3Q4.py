#################################################################
# 
#   File Name :   A3Q4.py
#   Description : problems on N Numbers -> Find Minimum
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        09/06/2025
#
#################################################################
"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3

"""

def CountFrequency(Arr, Size , No):
    
    iCnt = 0
    iCount = 0
    
    for iCnt in range(Size):
       if (Arr[iCnt] == No):
            iCount += 1
            
    
    return iCount


def main():
    print("Enter the number of elemets:")
    No = int(input())

    Arr = []

    print("Enter the elements :")
    for iCnt in range (No):
        Arr.append(int(input()))

    print("Enter the element to search :")
    iValue = int(input())
        
    iRet = 0
    iRet = CountFrequency(Arr, No,iValue) 
    print("Frequency of ",iValue," is :",iRet)

if(__name__ == "__main__"):
    main()