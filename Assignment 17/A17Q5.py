##############################################################
#
# FileName:     A17Q5.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################


import schedule
import time
def UpdateLog():
    fd = open("Marvellous.txt",'a')
    fd.write(time.ctime()+"\n")
    print(time.ctime()+" is written in to log file")

def main():
    schedule.every(1).seconds.do(UpdateLog)
    print("Application is in wating state...")
    
    while(True):
            schedule.run_pending()
            time.sleep(1)
    
    print("End Of Automation Scipt")

    

if(__name__ =="__main__"):
    main()