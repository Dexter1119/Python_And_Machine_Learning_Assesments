########################################################################
#
# Name:         A25Q3.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################



import numpy as np
import pandas as pd

def LabelEncode():

   data = {'city': 
           ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']
           }
   
   df = pd.DataFrame(data)

   city = {'Pune': 0, 'Mumbai': 1, 'Delhi': 2}

   df['city'] = df['city'].map(city)

   print(df)
def main():
    LabelEncode()


if(__name__ == "__main__"):
    main()


