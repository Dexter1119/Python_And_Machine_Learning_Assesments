########################################################################
#
# Name:         A23Q10.py
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
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
    }

    df = pd.DataFrame(data)

    print("DataFreame is:")
    print(df)

    df_new = df.drop(columns= ['English'])
    print(df_new)

    
    

def main():
    dataFrame()

if(__name__ == "__main__"):
    main()