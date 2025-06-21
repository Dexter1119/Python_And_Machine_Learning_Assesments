##############################################################
#
# FileName:     A17Q1.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################


import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Display)
    while (True):
        schedule.run_pending()
        time.sleep(1)

if(__name__ == "__main__"):
    main()