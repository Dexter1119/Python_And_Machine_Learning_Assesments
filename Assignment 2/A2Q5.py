#################################################################
# 
#   File Name :   A2Q5.py
#   Description : Program is used to check prime
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 5 Output : It is Prime Number

"""

def CheckPrime(No):
    if(No < 0):
        No = -No

    iCnt = 0
    

    for iCnt in range(int(No/2+1),0,-1):
        if(No % iCnt == 0):
            break
    
    if(iCnt == 1):
        return True
    else:
        return False
   

def main():
    No = 0
    print("Enter Number:",end=" ")
    No = int(input())

    bRet = False
    bRet = CheckPrime(No)
    if(bRet == True):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")


if("__main__" == __name__):
    main()