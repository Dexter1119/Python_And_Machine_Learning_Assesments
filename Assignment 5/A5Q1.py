###########################################################
#
# File :        A5Q1.py
# Description : Simple calculator
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""
Expected Input:
Enter first number: 10
Enter second number: 2

Expected Output:
Sum: 12
Difference: 8
Product: 20
Division: 5.0

"""
def Calculator(No1 , No2):
    
    print("The Addition is:",(No1 + No2))
    print("The Subtraction is:",(No1 - No2))
    print("The Product is:",(No1 * No2))

    if(No2 == 0):
        print("Divide BY Zero is not possible")
    print("The Division is:",float(No1 // No2))







def main():
        No1 = 0
        print("Enter the first Number:")
        No1 = int(input())

        No2 = 0
        print("Enter the first Number:")
        No2 = int(input())

        Calculator(No1,No2)




if (__name__ =="__main__"):
    main()