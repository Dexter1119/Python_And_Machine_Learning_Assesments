#################################################################
# 
#   File Name :   A3Q4.py
#   Description : problems on N Numbers -> Find Minimum
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        09/06/2025
#
#################################################################

import MarvellousNum




def main():
    print("Enter the number of elemets:")
    No = int(input())

    Arr = []

    print("Enter the elements :")
    for iCnt in range (No):
        Arr.append(int(input()))

        
    iRet = 0
    iRet = MarvellousNum.ChkPrime(Arr, No) 
    print("Summation of all prime numbers is :",iRet)

if(__name__ == "__main__"):
    main()