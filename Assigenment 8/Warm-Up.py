#####################################################################
#
# File :        Warm-Up.py
# Description : Program to Warm Up the threading
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

import threading
import time
def fun1(No):
    for iCnt in range(No+1):
        print(iCnt)

def fun2(No):
    for iCnt in range(No+2):
        print(iCnt)


def main():
    No = 0
    print("Enter the Number:")
    No = int(input())

    thread1 = threading.Thread(target = fun1,args =(No,))
    thread2 = threading.Thread(target = fun2,args =(No,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if(__name__ == "__main__"):
    main()