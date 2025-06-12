###########################################################
#
# File :        A6Q3.py
# Description : Print Table of No
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################

"""
Enter The number : 988

988 * 1 = 988
988 * 2 = 1976
988 * 3 = 2964
988 * 4 = 3952
988 * 5 = 4940
988 * 6 = 5928
988 * 7 = 6916
988 * 8 = 7904
988 * 9 = 8892
988 * 10 = 9880

"""
def DisplayEven(No):
    iCnt = 1
    

    while(iCnt != 11):
        print(No ,"*", iCnt ,"=",end =" ")
        print(No * iCnt)
        iCnt += 1


def main():

    No = 0
    print("Enter The number :",end = " ")
    No = int(input())
    DisplayEven(No)


if(__name__ == "__main__"):
    main()