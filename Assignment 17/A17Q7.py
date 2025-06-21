##############################################################
#
# FileName:     A17Q7.py
# Description:  Assessment On Schedular
# Author:       Pradhumnya Changdev Kalsait
# Date:         21/06/2025
# 
##############################################################


import schedule
import time
def UpdateLog():
    Timestamp = time.ctime
    FileName = Timestamp().replace(":", "_") + ".txt"

    fd = open(FileName,'a')
    fd.write("Log Entry Updated at "+time.ctime()+"\n")
    print(time.ctime()+" is written in to log file")

def main():
    schedule.every(1).hours.do(UpdateLog)
    print("Application is in wating state...")
    
    while(True):
            schedule.run_pending()
            time.sleep(1)
    
    print("End Of Automation Scipt")

    

if(__name__ =="__main__"):
    main()