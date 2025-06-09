#################################################################
# 
#   File Name :   MarvellousNum.py
#   Description : problems on N Numbers -> Helper Module for A3Q5.py
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        09/06/2025
#
#################################################################

"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5)
"""

def ChkPrime(Arr, No):
    
    iCnt = 0
    iSum = 0
    
    for iCnt in range(1,int(No/2+1)):
       if (Arr[iCnt-1] % iCnt == 0):
            iSum += Arr[iCnt]
    
    return iSum