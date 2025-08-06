############################################################################################
#
# Name:         A22.py
# Description:  Program which Traverse Directory and find checksum pf file and save in file
# Author:       Pradhumnya Changdev Kalsait.
# Date:         21/06/25
#
############################################################################################
import os
import sys
import time
import hashlib
import schedule




def CalculateCheckSum(path,BlcokSize = 1024):

    fobj = open(path,'rb')

    hobj = hashlib.md5() #For Calculate CheckSum 

    Buffer = fobj.read(BlcokSize)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(BlcokSize)

    fobj.close()

    return hobj.hexdigest()


def CommandLine():
    border = "-" * 48
    print(border)
    print("-------------Marvelllous Automation-------------")
    print(border)
    print("")
    print("")



    if(len(sys.argv)== 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H") ): 
            print("This application is used to performed directory")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("Script Name.py  NameOfDirectory ")
            print("Please provide valid absolute path")
        else:
            # result = FindDuplicate(sys.argv[1])
            # DeleteDuplicate(result)  #call the function

            schedule.every(1).minute.do(DeleteDuplicate)

            while (True):
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid Number of Command Line Arguments")
        print("     Use the give flags as")
        print("         --h : for help ")
        print("         --u : for usuage")
        


    print("")
    print("")
    print(border)
    print("----------Thanks For Using Script--------------")
    print(border)


           
def FindDuplicate(Directory_Name = "marvellous"):

    Flag = os.path.isabs(Directory_Name)
    if( Flag == False):
        Directory_Name = os.path.abspath(Directory_Name)


    Flag = os.path.exists(Directory_Name)
    if( Flag == False):
        print("The Path doesnt exists")
        return
       
    Flag = os.path.isdir(Directory_Name)
    if( Flag == False):
        print("The Path exists but target is not Directory")
        return
        
    print("")

    Duplicate = {}

    for FolderName , SubFolderNames , FileNames in os.walk(Directory_Name):

        for fname in FileNames :
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate



def DisplayResult(MyDict):
    duplicate = lambda x: len(x) > 1

    Result = list(filter(duplicate,MyDict.values()))

    Count = 0

    for Value in Result:
        for Subvalue in Value:
            Count += 1
            print(Subvalue)
        print("--------------------------------------")
        print("Value of Count is:",Count)
        print("--------------------------------------")
        Count = 0

            
       
           


def DeleteDuplicate(path = "Marvellous"):

    MyDict = FindDuplicate(path)
    duplicate = lambda x: len(x) > 1

    Result = list(filter(duplicate,MyDict.values()))

    Count = 0
    Cnt = 0

    for Value in Result:
        for Subvalue in Value:
            Count += 1
            if(Count > 1):
                print("Deleted File name :",Subvalue)
                os.remove(Subvalue)
                Cnt += 1


        Count = 0

    print("No.Of Deleted Files: ",Cnt)

           
def main():    
    CommandLine()

if("__main__"== __name__):
    main()