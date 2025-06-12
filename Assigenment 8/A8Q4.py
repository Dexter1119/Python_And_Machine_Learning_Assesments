#####################################################################
#
# File :        A8Q4.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################


"""
HeLLo@1106

Small Character are:  e
Small Character are:  o
Thread ID is: 4888
Capital Character are:  H
Digits are:  1
Capital Character are:  L
Digits are:  1
Capital Character are:  L
Digits are:  0
Thread ID is: 2008
Digits are:  6
Thread ID is: 11896
Thread Name is: Thread-3 (DisplayDigit)
Thread Name is: Thread-2 (DisplayCapital)
Thread Name is: Thread-1 (DisplaySmall)

"""
import threading

def DisplaySmall(str):
    iCnt = 0
    for iCnt in str:
        if((iCnt >= 'a') and (iCnt <= 'z')):
            print("Small Character are: ",iCnt)
        
    print("Thread ID is:",threading.current_thread().ident)
    print("Thread Name is:",threading.current_thread().name)

def DisplayCapital(str):
    iCnt = 0
    for iCnt in str:
        if((iCnt >= 'A') and (iCnt <= 'Z')):
            print("Capital Character are: ",iCnt)
        
    print("Thread ID is:",threading.current_thread().ident)
    print("Thread Name is:",threading.current_thread().name)

def DisplayDigit(str):
    iCnt = 0
    for iCnt in str:
        if((iCnt >= '0') and (iCnt <= '9')):
            print("Digits are: ",iCnt)
        
    print("Thread ID is:",threading.current_thread().ident)
    print("Thread Name is:",threading.current_thread().name)

def main():
    str = ''
    print("Enter the string:")
    str = input()

    small = threading.Thread(target = DisplaySmall ,args =(str,))
    Capital = threading.Thread(target = DisplayCapital ,args = (str,))
    Digit = threading.Thread(target = DisplayDigit ,args =(str,))

    small.start()
    Capital.start()
    Digit.start()

    small.join()
    Capital.join()
    Digit.join()

if(__name__ =="__main__"):
    main()
