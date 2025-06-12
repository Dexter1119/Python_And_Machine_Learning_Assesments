#####################################################################
#
# File :        A9Q2.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################


import os
import multiprocessing 
import threading
import time



def Sum(No):
    iSum = 0
    for iCnt in range(No+1):
        iSum += iCnt

    print(iSum)
    
   

def main():
    No = 0
    print("Enter the Number:")
    No = int(input())

    

    P1 = multiprocessing.Process(target = Sum,args =(No,))
    T1 = threading.Thread(target = Sum,args =(No,))
   
    start = time.time()
    P1.start()
    P1.join()
    end = time.time()
    timeR = end - start
    print("Time Required for Process:",timeR)

    start = time.time()
    T1.start()
    T1.join()
    end = time.time()
    timeR = end - start
    print("Time Required for Thread:",timeR)


   

    print("Exit from Main")
if(__name__ =="__main__"):
    main()
