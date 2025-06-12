#####################################################################
#
# File :        A8Q2.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################


"""
ENter the number : 9

addition of even factors of given number: 0
addition of odd factors of given number: 4

exit from main
"""
import threading
def EvenFactorSum(No):
    iSum = 0
    iCnt = 0

    for iCnt in range (1,int(No//2+1)):
        if(( No % iCnt == 0)and(iCnt % 2 == 0)):
            iSum += iCnt
    
    Result["even"] = iSum

    print("addition of even factors of given number:",iSum)

def OddFactorSum(No):
    iSum = 0
    iCnt = 0

    for iCnt in range (1,int(No//2)):
        if(( No % iCnt == 0)and(iCnt % 2 != 0)):
            iSum += iCnt

    Result["odd"] = iSum

    print("addition of odd factors of given number:",iSum)

Result ={"even": 0,"odd": 0}  
def main():

    No = 0
    print("ENter the number :",end=" ")
    No = int(input())

    EvenFactor  = threading.Thread(target= EvenFactorSum,args = (No,))
    OddFactor = threading.Thread(target= OddFactorSum,args = (No,))

    EvenFactor.start()
    OddFactor.start()


    EvenFactor.join()
    OddFactor.join()

    print("exit from main")

if(__name__ =="__main__"):
    main()
