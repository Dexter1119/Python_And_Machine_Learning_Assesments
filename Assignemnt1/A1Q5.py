###################################################################
#
# Name:         A1Q5.py
# Description:  program which display 10 to 1 on console.
# Author:       Pradhumnya Changdev Kalsait
# Date:         10-05-25
# Assignemnt :  Assignement 1 Question 5 
#
###################################################################

def DisplayNum():
    
    for iCnt in range(10,0,-1):
        print(iCnt ,end=" ")

def main():
    DisplayNum()


if("__main__" == __name__):
    main()