###########################################################
#
# File :        A6Q2.py
# Description : Print and sum even
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################
"""
Enter The number : 100

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100

Sum of All Even Numbers is: 2550

"""

def DisplayEven(No):
    iCnt = 1
    iSum = 0

    while(No != 0):
        if(iCnt % 2 == 0):
            print(iCnt,end =" ")
            iSum += iCnt

        iCnt += 1
        No -= 1
    
    print("\nSum of All Even Numbers is:",iSum)
def main():

    No = 0
    print("Enter The number :",end = " ")
    No = int(input())
    DisplayEven(No)


if(__name__ == "__main__"):
    main()