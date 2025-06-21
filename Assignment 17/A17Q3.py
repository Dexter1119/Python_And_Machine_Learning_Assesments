##############################################################
#
# FileName:     A17Q3.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################


import schedule
import time
def Display():
    print("Do Coding.....")

def main():
    schedule.every(30).minutes.do(Display)
    print("Application is in wating state...")
    
    while(True):
            schedule.run_pending()
            time.sleep(1)
    
    print("End Of Automation Scipt")

    

if(__name__ =="__main__"):
    main()