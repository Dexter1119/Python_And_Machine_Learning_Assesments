##############################################################
#
# FileName:     A17Q6.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################

import threading
import schedule
import time

LunchTime = lambda : print("Lunch Time")
WrapUpWork = lambda : print("Wrap Up Work")

def Task1():
    print("Application is in wating state...")
    schedule.every().day.at("13:00").do(LunchTime)
    while(True):
        schedule.run_pending()
        time.sleep(1)

def Task2():
    print("Application is in wating state...")
    schedule.every().day.at("09:00").do(WrapUpWork)
    while(True):
        schedule.run_pending()
        time.sleep(1)

def main():
    print("Threads are created...")
    t1 = threading.Thread(target=Task1, args=())
    t2 = threading.Thread(target=Task2, args=())
    
    print("Threads are started Execution...")
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("End Of Automation Scipt")
if(__name__ =="__main__"):
    main()