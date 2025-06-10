#################################################################
# 
#   File Name :   A4Q3.py
#   Description : FMR Assesments
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        10/06/2025
#
#################################################################

"""
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

"""

from functools import reduce

Between70And90 = lambda No : ((No >= 70) and (No <= 90))
Add_Ten = lambda No : No + 10
Product = lambda x , y : x * y

def main():
    
    List = []
    No = 0
    print("Enter the number of elements you want to enter :")
    No = int(input())

    print("Enter the elements :")
    for i in range(No):
        List.append(int(input()))

    print("List is : ",List)

    List = list(filter(Between70And90 , List))
    print("List after filter is : ",List)

    List = list(map(Add_Ten , List))
    print("List after map is : ",List)

    iRet = 0
    iRet = reduce(Product , List)
    print("Product of all elements is : ",iRet)


if(__name__ == "__main__"):
    main()