#####################################################################
#
# File :        A7Q2.py
# Description : Map the list
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

Expected Input:
Enter list: 1 2 3 4 5

Expected Output:
Doubled list: [2, 4, 6, 8, 10]

"""

#lamda Functions

double = lambda No: No * 2
def mapX(Task,Values):

    Result = []

    for i in Values:
        iRet = Task(i)
        Result.append(iRet)

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

    List = mapX(double,List)

    print("Doubled List:",List)
    

    

    

if(__name__ == "__main__"):
    main()