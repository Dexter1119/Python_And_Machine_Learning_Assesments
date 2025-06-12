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

#lamda Functions

ChkEven = lambda No: (No % 2 == 0)
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

    List = filterX(ChkEven,List)

    print("Even List:",List)
    

    

    

if(__name__ == "__main__"):
    main()