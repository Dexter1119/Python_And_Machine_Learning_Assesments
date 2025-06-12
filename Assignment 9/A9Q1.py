#####################################################################
#
# File :        A9Q1.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################

"""
Enter the Number:
5
1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

"""
import threading
import time
def DisplayNum(No):
    for i in range(1,No+1):
        print(i,end =" ")

    print("\n")



def main():
    No = 0
    print("Enter the Number:")
    No = int(input())

    thread1 = threading.Thread(target = DisplayNum,args =(No,))
    thread2 = threading.Thread(target = DisplayNum,args =(No,))
    thread3 = threading.Thread(target = DisplayNum,args =(No,))

    thread1.start()
    time.sleep(1)
    thread1.join()

    thread2.start()
    time.sleep(1)
    thread2.join()

    thread3.start()
    time.sleep(1)
    thread3.join()

    print("Exit from Main")
if(__name__ =="__main__"):
    main()
