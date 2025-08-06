########################################################################
#
# Name:         A24Q9.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder


def PdDataFrame():
    
    data = {    
            'Name': ['Amit', 'Sagar', 'Pooja'],
            'Gender' : ['Male','Male','Female'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]
            }  

    df = pd.DataFrame(data)
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis = 1)
    

 

    
    

    df = df.rename(columns={'Math': 'Mathematics'})


    print(df)

def main():
    PdDataFrame()

if(__name__) == "__main__":
    main()