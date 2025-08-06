########################################################################
#
# Name:         A23Q9.py
# Description:  Program which Implemented Pandas assignement -> pie chart
# Author:       Pradhumnya Changdev Kalsait.
# Date:         19/07/25
#
########################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def dataFrame():
    data = {
        'Name': ['Amit','Sagar','pooja'],
        'Math': [np.nan, 90, 78],
        'Science': [92, np.nan, 80],
        
    }

    df = pd.DataFrame(data)

    print("DataFreame is:")
    print(df)

    df.fillna(df.mean(numeric_only = True),inplace = True)
    print("DataFreame is:")
    print(df)

    
    

def main():
    dataFrame()

if(__name__ == "__main__"):
    main()