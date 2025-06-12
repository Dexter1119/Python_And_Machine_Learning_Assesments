#####################################################################
#
# File :        A8Q5.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################
import threading
def DisplayNum(No):
    for i in range(1,No+1):
        print(i,end =" ")

    print("\n")

def DisplayNumRev(No):
    for i in range(No,0,-1):
        print(i,end=" ")
        
    print("\n")

def main():
    No = 0
    print("Enter the Number:")
    No = int(input())

    thread1 = threading.Thread(target = DisplayNum,args =(No,))
    thread2 = threading.Thread(target = DisplayNumRev,args =(No,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()
if(__name__ =="__main__"):
    main()
