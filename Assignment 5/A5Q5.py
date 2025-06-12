###########################################################
#
# File :        A5Q5.py
# Description : Check Even 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""
Expected Input:
Enter a number: 17

Expected Output:
17 is an odd number.

"""
def CheckEvenOdd(No):

    return ((No % 2) == 0)



def main():
   
    
    print("Enter the Number :",end="")
    iValue = int(input())

    bRet = CheckEvenOdd(iValue)
    if(bRet == True):
        print(iValue,"is Even")

    else:
        print(iValue,"is Odd")





if (__name__ =="__main__"):
    main()