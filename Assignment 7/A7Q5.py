#####################################################################
#
# File :        A7Q5.py
# Description : Map the list
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""

Expected Input:
Enter a string: radar

Expected Output:
radar is a palindrome.


"""

def CheckPalindrom(str):
    
    start = 0
    end = len(str)-1

    while(start > end):
        if(str[start] != str[end]):
            break
        start += 1
        end -= 1

    return (start <=  end)
    
    




def main():
    str = ""
    print("Enter the String:")
    str = input()

    bRet = CheckPalindrom(str)
    if(bRet == True):
        print(str,"is palindrom")
    else:
        print(str,"is not palindrom")
    

    

    

if(__name__ == "__main__"):
    main()