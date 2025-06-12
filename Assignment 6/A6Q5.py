###########################################################
#
# File :        A6Q5.py
# Description : Check Prime
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################

"""

Expected Input:
Enter a number: 11

Expected Output:
11 is a prime number

"""
def CheckPrime(No):
    iCnt = 1
    
    for iCnt in range(2,int(No // 2 + 1)):
        if((No %iCnt) == 0):
            break
     
    
    if(iCnt == int(No // 2) ):
        return True
    else:
        return False

def main():

    No = 0
    print("Enter The number :",end = " ")
    No = int(input())

    bRet = False
    bRet = CheckPrime(No)
    if(bRet == True):
        print(No,"is Prime")
    else:
        print(No,"is Composite")

if(__name__ == "__main__"):
    main()