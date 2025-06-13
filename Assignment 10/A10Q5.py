#################################################################
# 
#   File Name :   A10Q5.py
#   Description : FMR Assesments
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        13/06/2025
#
#################################################################

"""
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""

from functools import reduce

def IsPrime(No):
    iCnt = 0
    for iCnt in range(int(No / 2),0,-1):
        if(No % iCnt == 0):
            break

    if(iCnt == 1):
        return True

    return False


MultiplyBy2 = lambda x : x * 2

Maximum = lambda x , y : x if(x > y) else y

def main():
    
    List = []
    No = 0
    print("Enter the number of elements you want to enter :")
    No = int(input())

    print("Enter the elements :")
    for i in range(No):
        List.append(int(input()))

    print("List is : ",List)

    List = list(filter(IsPrime , List))
    print("List after filter is : ",List)

    List = list(map(MultiplyBy2 , List))
    print("List after map is : ",List)

    iRet = 0
    iRet = reduce(Maximum , List)
    print("Maximum Number out of all elements is : ",iRet)


if(__name__ == "__main__"):
    main()