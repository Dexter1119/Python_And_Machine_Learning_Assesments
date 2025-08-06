########################################################################
#
# Name:         A25Q4.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################



import numpy as np
import pandas as pd

def Encode():

   data = {'Department': 
           ['HR', 'IT', 'Finance', 'HR', 'IT']
           }
   
   df = pd.DataFrame(data)

   encode = pd.get_dummies(df,columns=['Department'])
   print(encode)

def main():
    Encode()


if(__name__ == "__main__"):
    main()


