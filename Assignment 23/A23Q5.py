########################################################################
#
# Name:         A23Q5.py
# Description:  Program which Implemented Pandas assignement
# Author:       Pradhumnya Changdev Kalsait.
# Date:         19/07/25
#
########################################################################
import pandas as pd


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

    print("Changing name Pooja to puja")
    df.loc[df['Name'] == 'pooja', 'Name'] = 'puja'

    #df['Name'] = df['Name'].replace('pooja','puja')

    print(df)
    

def main():
    dataFrame()

if(__name__ == "__main__"):
    main()