########################################################################
#
# Name:         A25Q2.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################



import numpy as np
import pandas as pd

def ShowAge():

    data = {
            'Name': ['A', 'B', 'C'], 
            'Age': [21.0, 22.0, 23.0]
            }
    
    df = pd.DataFrame(data)

    df['Age'] = df['Age'].astype(int)
    
    print(df)

def main():
    ShowAge()


if(__name__ == "__main__"):
    main()


