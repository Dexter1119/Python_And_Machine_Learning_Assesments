########################################################################
#
# Name:         A23Q6.py
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

    print("Adding New Column as total:")
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    

    print("Sorting Data Frame")
    df_new = df.sort_values(by='Total', ascending = False)
    print(df_new)
    

def main():
    dataFrame()

if(__name__ == "__main__"):
    main()