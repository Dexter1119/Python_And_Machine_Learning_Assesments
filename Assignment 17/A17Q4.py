##############################################################
#
# FileName:     A17Q4.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################


import schedule
import time
def DisplayGreeting():
    print("!!...Namaskar...!!")

def main():
    schedule.every().day.at("09:00").do(DisplayGreeting)
    print("Application is in wating state...")
    
    while(True):
            schedule.run_pending()
            time.sleep(1)
    
    print("End Of Automation Scipt")

    

if(__name__ =="__main__"):
    main()