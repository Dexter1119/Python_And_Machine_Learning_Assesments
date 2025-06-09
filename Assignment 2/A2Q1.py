#################################################################
# 
#   File Name :   A2Q1.py
#   Description : Module Implimentation
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

import Arithmetic
def main():
    
    No1 = 0
    No2 = 0

    print("Enter Fist Number")
    No1 = int(input())

    print("Enter Second Number")
    No2 = int(input())

    Ret = 0

    Ret = Arithmetic.Add(No1, No2)
    print("Addition is : ", Ans)

    Ret = Arithmetic.Sub(No1, No2)
    print("Subtraction is : ", Ans)

    Ret = Arithmetic.Mul(No1, No2)
    print("Multiplication is : ", Ans)

    Ret = Arithmetic.Div(No1, No2)
    print("Division is : ", Ans)



if(__name__ == "__main__"):
    main()