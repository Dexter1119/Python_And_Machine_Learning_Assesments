################################################################################
# 
# File Name   : A10Q2.py
# Description : Functional Approch
# Author      : Pradhumnya Changdev Kalsait
# Date        : 13/06/2025
# 
################################################################################


"""
Input : 4  3     Output : 12
Input : 6  3     Output : 18
"""
Multiply = lambda x,y: x * y

def main():

    No1 = 0
    print("Enter the number", end = " ")
    No1 = int(input())

    No2 = 0
    print("Enter the number", end = " ")
    No2 = int(input())
    
    print("Multiplication of", no1, "and", no2, "is", Multiply(No1, No2))

if(__name__ == "__main__"):
    main()