#####################################################################
#
# File :        A8Q1.py
# Description : program demonstrate threading 
# Author :      Pardhumnya Changedev Kalsait 
# Date :        12/06/25       
#
#####################################################################
"""
ENter the number : 10
Displaying Even
0
2
Displaying Odd
4
1
3
5
7
6
9
8
10

"""
import threading
def PrintEven(No):
    print("Displaying Even")
    for i in range (No+1):
        if(i % 2 == 0):
            print(i)

def PrintOdd(No):
    print("Displaying Odd")
    for i in range (No+1):
        if(i % 2 != 0):
            print(i)
            
def main():
    No = 0
    print("ENter the number :",end=" ")
    No = int(input())
    Even = threading.Thread(target= PrintEven,args = (No,))
    Odd = threading.Thread(target= PrintOdd,args = (No,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if(__name__ =="__main__"):
    main()
