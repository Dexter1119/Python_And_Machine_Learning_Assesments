#################################################################
# 
#   File Name :   A2Q7.py
#   Description : Program is used to display pattern
#   Name :        Pradhumnya Changdev Kalsait
#   Date :        08/06/2025
#
#################################################################

"""
Input : 5
Output : 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""

def DisplayPattern(iRow , iCol):
    
        
    i = 0
    j = 0

    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
          print(j, end = " ")
        print()
   

def main():
    No1 = 0
    No2 = 0
    print("Enter the number of rows:",end=" ")
    No1 = int(input())

    print("Enter the number of columns:",end=" ")
    No2 = int(input())

    DisplayPattern(No1, No2)

  

if("__main__" == __name__):
    main()