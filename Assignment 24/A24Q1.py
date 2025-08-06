########################################################################
#
# Name:         A24Q1.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def PdDataFrame():
    
    data = {    
            'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]
            }  

    df = pd.DataFrame(data)
    print(df.head())

    print(df.describe())

    sns.displot(df['Math']);
    plt.show()

    #Max Scalling

    # value // max Value

    df['Math'] = df['Math'] / df['Math'].abs().max()

    print(df)
        
     

def main():
    PdDataFrame()

if(__name__) == "__main__":
    main()