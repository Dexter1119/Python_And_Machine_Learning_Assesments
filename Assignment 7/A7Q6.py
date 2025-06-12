#####################################################################
#
# File :        A7Q3.py
# Description : Map the list
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

Expected Input:
Enter list: 1 2 3 4 5 6

Expected Output:
Even numbers: [2, 4, 6]

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



def filterX(Task,Values):
    
    Result = []

    for i in Values:
        bRet = Task(i)
        if(bRet == True):
            Result.append(i)

    return Result


def main():
    List = []
    iNo = 0
    iTemp = 0
    
    print("enter the number of elements:",end =" ")
    iNo = int(input())
    if(iNo < 0):
        print("Enter the correct number of elements")

    print("Enter the Elements")
    for i in range(iNo):
        iTemp = int(input())
        List.append(iTemp)

    List = filterX(CheckPrime,List)

    print("Prime List:",List)

    

if(__name__ == "__main__"):
    main()