###########################################################
#
# File :        A5Q4.py
# Description : Find MAx Number
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""
Enter three numbers: 5 9 3

Expected Output:
Largest number is 9.

"""
def FindMax(No1,No2,No3):

    if(No1 > No2 and No1 > No3):
        return No1
    elif(No2 > No1 and No2 > No3):
        return No2
    else:
        return No3



def main():
   
    
    print("Enter the Number 1:",end="")
    iValue1 = int(input())

    print("Enter the Number 2:",end="")
    iValue2 = int(input())

    print("Enter the Number 3:",end="")
    iValue3 = int(input())

    iRet = 0
    iRet = FindMax(iValue1,iValue2,iValue3)

    print("Maximum element is:",iRet)






if (__name__ =="__main__"):
    main()