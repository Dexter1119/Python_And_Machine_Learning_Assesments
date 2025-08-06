########################################################################
#
# Name:         A25Q9.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################


import pandas as pd
import numpy as np

def Replace():

    data = {
            'Marks': 
            [45, 67, 88, 32, 76]
            }
    
    df = pd.DataFrame(data)

    df['Marks'] = df['Marks'].where(df['Marks'] >= 50, 'Fail')


    print(df)
def main():
    Replace()

if(__name__ == "__main__"):
    main()


