########################################################################
#
# Name:         A21Q2.py
# Description:  Program which Shows the infor of all Running Processes
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/06/25
#
########################################################################

import psutil
import sys

def ProcessInfo(proc_name):
    Border = "*" * 25
    print(Border)
    print("Information Of Currently Running Processes")
    print(Border)

    bFlag = False

    for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_info']):
        try:
            info = proc.info
            if proc_name.lower() == info['name'].lower():
                info['vms'] = proc.memory_info().vms / (1024 * 1024)

                print(f"PID        : {info['pid']}")
                print(f"Name       : {info['name']}")
                print(f"Username   : {info['username']}")
                print(f"VMS        : {info['vms']:.2f} MB")
                bFlag = True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if (bFlag == False):
        print(f"No running process found with name: {proc_name}")
        

def main():

    if (len(sys.argv)!= 2):
        print("Print the name of the process to search")
        return

    ProcessInfo(sys.argv[1])
   

if(__name__ == "__main__"):
    main()