########################################################################
#
# Name:         A25Q7.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################


import pandas as pd

def MinMaxScale():
    data = {'Age': 
            [18, 22, 25, 30, 35]
            }
    
    df = pd.DataFrame(data)
    
    df['Age'] = df['Age'] / df['Age'].abs().max()

    print(df)

    
def main():
    MinMaxScale()

if(__name__ == "__main__"):
    main()


