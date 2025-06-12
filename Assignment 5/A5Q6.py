###########################################################
#
# File :        A5Q6.py
# Description : Convert Ferhanite
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""
Expected Input:
Enter temperature in Celsius: 25

Expected Output:
Temperature in Fahrenheit: 77.0°F

"""
def ConvertFeh(No):

    Ferh = 0

    Ferh = (No * (9/5))+ 32

    return Ferh



def main():
   
    
    print("Enter the Temp in Celcius :",end="")
    iValue = int(input())

    iRet = ConvertFeh(iValue)
    print("The Temperature in Ferhanite is:",iRet)





if (__name__ =="__main__"):
    main()