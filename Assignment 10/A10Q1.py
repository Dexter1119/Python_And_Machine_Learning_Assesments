################################################################################
# 
# File Name   : A10Q1.py
# Description : Functional Approch
# Author      : Pradhumnya Changdev Kalsait
# Date        : 13/06/2025
# 
################################################################################


"""
Input : 4       Output : 16
Input : 6       Output : 64
"""
square = lambda x: x ** 2

def main():

    No = 0
    print("Enter the number", end = " ")
    No = int(input())
    
    print("Square of", no, "is", square(No))

if(__name__ == "__main__"):
    main()