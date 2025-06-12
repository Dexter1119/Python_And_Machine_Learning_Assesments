###########################################################
#
# File :        A5Q2.py
# Description : Check Age
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""
Expected Input:
Enter age: 19

Expected Output:
Eligible to vote.

"""
def CheckAge(No):
    if(No < 0 ):
        return -1
    return (No > 18)
    
    



def main():
   
    
    print("Enter the Age:",end="")
    iValue = int(input())

    bRet = False
    bRet = CheckAge(iValue)
    if(bRet == -1):
        print("!!...Enter Correct Age...!!")
        return
        
    if(bRet == True):
        print("Eligible to vote")

    else:
        print("Not eligible to vote")






if (__name__ =="__main__"):
    main()