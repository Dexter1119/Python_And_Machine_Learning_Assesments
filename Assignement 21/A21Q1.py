########################################################################
#
# Name:         A21Q1.py
# Description:  Program which Shows the infor of all Running Processes
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/06/25
#
########################################################################

import psutil

def ProcessDisplay():
    Border = "*" * 25
    print(Border)
    print("Information Of Currently Running Processes")
    print(Border)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ['pid','name','username'])
        info['vms'] = proc.memory_info().vms / (1024 * 1024)
        print(info)



def main():
    ProcessDisplay()

if(__name__ == "__main__"):
    main()