#################################################################
# 
#   File Name :   A4Q4.py
#   Description : FMR Assesments
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        10/06/2025
#
#################################################################

"""
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204

"""

from functools import reduce

check_even = lambda No : (No % 2 == 0)
square = lambda No : No ** 2
Summation = lambda x,y : x + y

def main():
    
    List = []
    No = 0
    print("Enter the number of elements you want to enter :")
    No = int(input())

    print("Enter the elements :")
    for i in range(No):
        List.append(int(input()))

    print("List is : ",List)

    List = list(filter(check_even , List))
    print("List after filter is : ",List)

    List = list(map(square , List))
    print("List after map is : ",List)

    iRet = 0
    iRet = reduce(Summation , List)
    print("Product of all elements is : ",iRet)


if(__name__ == "__main__"):
    main()