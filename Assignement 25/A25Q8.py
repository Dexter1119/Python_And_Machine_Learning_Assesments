########################################################################
#
# Name:         A25Q8.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################


import pandas as pd
import numpy as np

def FillMissing():

    data = {'Marks':
             [85, np.nan, 90, np.nan, 95]
             }
    
    df = pd.DataFrame(data)
    df['Marks'] = df['Marks'].interpolate()
    print(df)
    
def main():
    FillMissing()

if(__name__ == "__main__"):
    main()


