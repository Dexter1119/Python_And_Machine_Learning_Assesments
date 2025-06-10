#################################################################
# 
#   File Name :   A4Q2.py
#   Description : Lambada Function Assesments
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        10/06/2025
#
#################################################################

"""
Input : 4 3 Output : 12
Input : 6 3 Output : 18

"""

Multiplication = lambda x , y : x * y

def main():
    
    print("Enter the number 1 :")
    No1 = int(input())

    print("Enter the number 2:")
    No2 = int(input())

    iRet = 0
    iRet = Multiplication(No1 , No2)
    print("Multiplication of two numbers is : ",iRet)

if(__name__ == "__main__"):
    main()