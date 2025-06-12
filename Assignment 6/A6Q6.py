#####################################################################
#
# File :        A6Q6.py
# Description : Program to Print Triangle Pattern using Nested Loops
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

*
* *
* * *
* * * *

"""
def DisplayPattern(Rows , Cols):

    i = 0
    j = 0

    for i in range(1,Rows+1):
        for j in range(1,Cols+1):
            if(i >= j ):
                print("*",end=" ")
            else:
                print(" ",end = " ")
                
        print("")

def main():

    No1 = 0
    print("Enter The number of rows :",end = " ")
    No1 = int(input())

    No2 = 0
    print("Enter The number of cols:",end = " ")
    No2 = int(input())

    DisplayPattern(No1, No2)

if(__name__ == "__main__"):
    main()