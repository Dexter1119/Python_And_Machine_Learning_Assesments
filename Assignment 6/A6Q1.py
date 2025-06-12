###########################################################
#
# File :        A6Q1.py
# Description : Concept of iterations
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################

"""
Enter The number : 50

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50

"""
def DisplayNum(No):
    iCnt = 1

    while(No != 0):
        print(iCnt,end=" ")
        iCnt += 1
        No -= 1
def main():

    No = 0
    print("Enter The number :",end = " ")
    No = int(input())
    DisplayNum(No)


if(__name__ == "__main__"):
    main()