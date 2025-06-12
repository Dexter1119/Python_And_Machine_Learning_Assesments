#####################################################################
#
# File :        A7Q4.py
# Description : Map the list
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

Expected Input:
Enter list: 2 3 4

Expected Output:
Product: 24


"""

#lamda Functions

Sum = lambda No1,No2: No1 + No2
def reduceX(Task,Values):
    
    Result = 0

    for i in Values:
        Result = Task(Result,i)

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

    List = reduceX(Sum,List)

    print("Even List:",List)
    

    

    

if(__name__ == "__main__"):
    main()