#####################################################################
#
# File :        A8Q3.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################


"""
ENter the number of Elements : 3
Enter the Elements : 
1
2
3
addition of Even Elements in List: 2
addition of odd Elements in List: 4
exit from main

"""
import threading
def OddSum(No):
    iSum = 0
    iCnt = 0

    for iCnt in No:
        if(iCnt %2 != 0):
            iSum += iCnt


    Result["odd"] = iSum

def EvenSum(No):
    iSum = 0
    iCnt = 0

    for iCnt in No:
        if(iCnt %2 == 0):
            iSum += iCnt


    Result["even"] = iSum

   

Result ={"even": 0,"odd": 0}  
def main():

    No = 0
    List = []

    print("ENter the number of Elements :",end=" ")
    No = int(input())

    print("Enter the Elements :")
    for i in range (No):
        List.append(int(input()))

    EvenList  = threading.Thread(target= EvenSum,args = (List,))
    OddList = threading.Thread(target= OddSum,args = (List,))

    EvenList.start()
    OddList.start()

    print("addition of Even Elements in List:",Result["even"])
    print("addition of odd Elements in List:",Result["odd"])


    EvenList.join()
    OddList.join()

    print("exit from main")

if(__name__ =="__main__"):
    main()
