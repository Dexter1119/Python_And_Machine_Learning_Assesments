########################################################################
#
# Name:         A23Q4.py
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

    print("Students who scored above 85 in science:")
    names = df[df['Science'] > 85].Name.tolist()
    print(names)
    

def main():
    dataFrame()

if(__name__ == "__main__"):
    main()