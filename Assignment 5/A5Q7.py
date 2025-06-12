###########################################################
#
# File :        A5Q6.py
# Description : Calculate Area And Parameter 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""

Expected Input:
Enter length: 5
Enter width: 3

Expected Output:
Area: 15
Perimeter: 16

"""
def CalAreaPari(length , width):

    if(length < 0 or width < 0):
        print("enter Correct values")
        return

    Area = 0
    Parimeter = 0

    print("Area of Rectangle is:", length * width) 

    print("Perimeter of Rectangle is: ",int(2 * (length + width)))




def main():
   
    
    print("Enter the length :",end="")
    iValue1 = int(input())

    print("Enter the width :",end="")
    iValue2 = int(input())

    CalAreaPari(iValue1,iValue2)





if (__name__ =="__main__"):
    main()