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



def Square(No):

    square = No ** 2
    print("Square is:",square)
   







def main():
    No = 0
    print("Enter the Number:")
    No = int(input())

    

    P1 = multiprocessing.Process(target = Square,args =(No,))
   
    P1.start()
    time.sleep(1)
    P1.join()

   

    print("Exit from Main")
if(__name__ =="__main__"):
    main()
