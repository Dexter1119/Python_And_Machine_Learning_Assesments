#####################################################################
#
# File :        A7Q1.py
# Description : Write two lambda functions to find Square and cube
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

Expected Input:
Enter a number: 3

Expected Output:
Square: 9
Cube: 27

"""

#lamda Functions
square = lambda No: No**2
cube = lambda No: No**3

def main():
    No = 0
    print("ENter the Number:",end =" ")
    No = int(input())

    iRet = square(No)
    print("The Square is: ", iRet)

    iRet = cube(No)
    print("The Cube is: ",iRet)

if(__name__ == "__main__"):
    main()