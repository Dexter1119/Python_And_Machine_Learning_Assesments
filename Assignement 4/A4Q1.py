#################################################################
# 
#   File Name :   A4Q1.py
#   Description : Lambada Function Assesments
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        10/06/2025
#
#################################################################

"""
Input : 4 Output : 16
Input : 6 Output : 64

"""

square = lambda x : x**2

def main():
    
    print("Enter the number :")
    No = int(input())

    iRet = 0
    iRet = square(No)
    print("Square of number is : ",iRet)

if(__name__ == "__main__"):
    main()