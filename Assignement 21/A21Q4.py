########################################################################
#
# Name:         A21Q4.py
# Description:  Program which Shows the infor of all Running Processes
# Author:       Pradhumnya Changdev Kalsait.
# Date:         21/06/25
#
########################################################################

import os
import sys
import psutil
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def CreateProcessLog(Directory_Name):

    IsAbsolute = os.path.isabs(Directory_Name)

    if(IsAbsolute == False):
        Directory_Name = os.path.abspath(Directory_Name)

    PathExists = os.path.exists(Directory_Name)

    if(PathExists == False):
        print("ERROR: The specified path does not exist.")
        return

    IsDirectory = os.path.isdir(Directory_Name)

    if(IsDirectory == False):
        print("ERROR: The path exists but is not a directory.")
        return

    print("")

    CurrentTime = datetime.now().strftime("%Y%m%d_%H%M%S")
    LogFileName = "ProcessLog_" + CurrentTime + ".log"
    LogFilePath = os.path.join(Directory_Name, LogFileName)

    try:
        LogFile = open(LogFilePath, 'w')
        LogFile.write("Name\t\tPID\t\tUsername\n")
        LogFile.write("--------------------------------------------------\n")

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                ProcInfo = proc.info

                ProcName = ProcInfo['name']
                ProcPID = ProcInfo['pid']
                ProcUser = ProcInfo['username']

                LogFile.write(f"{ProcName[:15]:<16}{ProcPID:<10}{ProcUser}\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        LogFile.close()
        print("SUCCESS: Process log created at:", LogFilePath)

    except Exception as e:
        print("ERROR: Failed to write log file.", e)

    def SendMail():
        subject = input("Subject: ")
        body = input("Message: ")

        message = MIMEMultipart()
        message["From"] = "pradhumnyakalsait288@gmail.com"
        message["To"] = "kalsaitpc@gmail.com"
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("pradhumnyakalsait288@gmail.com", "kohs eylk erkc tpwy")
        text = str(message)

        server.sendmail("pradhumnyakalsait288@gmail.com","kalsaitpc@gmail.com", text)
        server.quit()

        print("Email sent successfully to:", "kalsaitpc@gmail.com")



def main():
    ArgCount = len(sys.argv)

    if(ArgCount != 2):
        print("Usage: ProcInfoLog.py <DirectoryName>")
        return

    Directory_Name = sys.argv[1]
    CreateProcessLog(Directory_Name)

if(__name__ == "__main__"):
    main()