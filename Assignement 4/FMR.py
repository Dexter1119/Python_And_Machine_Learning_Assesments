#################################################################
# 
#   File Name :   FMR.py
#   Description : Random Own FMR functions file
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        10/06/2025
#
#################################################################

"""
this is not FMR excution file but tried to make own FMR fuction By Understanding the Conecept 
that can we make our own FMR
"""

#defining lambada for the execution of FMR

check_even = lambda No : (No % 2 == 0)
Add_one = lambda No : No + 1
Summation = lambda x,y : x + y

def filterX(task , list):
    Result = []
    for i in list:
        bRet = task(i)
        if(bRet == True):
            Result.append(i)

    return Result

def mapX(task , list):
    Result = []
    for i in list:
        iRet = task(i)
        Result.append(iRet)

    return Result

def reduceX(task , list):
    Result = 0
    for i in list:
        Result = task(Result , i)

    return Result


def main():
    List = []
    No = 0
    print("Enter the number of elements you want to enter :")
    No = int(input())

    print("Enter the elements :")
    for i in range(No):
        List.append(int(input()))

    print("List is : ",List)

    List = filterX(check_even , List)
    print("List after filter is : ",List)

    List = mapX(Add_one , List)
    print("List after map is : ",List)

    iRet = 0
    iRet = reduceX(Summation , List)
    print("Summation of all elements is : ",iRet)
    

if(__name__ == "__main__"):
    main()
