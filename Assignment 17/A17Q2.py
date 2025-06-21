##############################################################
#
# FileName:     A17Q2.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################


import schedule
import time
def DisplayTime():
    timestamp = time.ctime()
    print(timestamp)

def main():
    schedule.every(5).seconds.do(DisplayTime)
    print("Application is in wating state...")
    
    while(True):
            schedule.run_pending()
            time.sleep(1)
    
    print("End Of Automation Scipt")

    

if(__name__ =="__main__"):
    main()