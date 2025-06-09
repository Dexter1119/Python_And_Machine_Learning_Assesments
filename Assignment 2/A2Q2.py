#################################################################
# 
#   File Name :   A2Q2.py
#   Description : Pattern Printing
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 5
Output :
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *

"""

def Display(No):

    i = 0
    j = 0

    for i in range(1,No+1):
        for j in range(1,No+1):
            print("*", end = " ")
        print()


def main():
    No = 0
    print("Enter Number:",end=" ")
    No = int(input())

    Display(No)
if("__main__" == __name__):
    main()