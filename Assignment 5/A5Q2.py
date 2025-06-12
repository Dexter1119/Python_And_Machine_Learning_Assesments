###########################################################
#
# File :        A5Q2.py
# Description : Check char
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
###########################################################


"""
Expected Input:
Enter a character: e

Expected Output:
'e' is a vowel.

"""
def CheckChar(char):
    
    
    if((char == 'a' or char == 'A') or (char == 'e' or char == 'E') or (char == 'i' or char == 'I') or (char == 'o' or char == 'O') or (char == 'u' or char == 'U')):
        return True

    else:
        return False
    



def main():
   
    
    print("Enter the character:",end="")
    cValue = input()

    bRet = False
    bRet = CheckChar(cValue)
    if(bRet == True):
        print(cValue,"is vowel.")

    else:
        print(cValue,"is consonant.")






if (__name__ =="__main__"):
    main()