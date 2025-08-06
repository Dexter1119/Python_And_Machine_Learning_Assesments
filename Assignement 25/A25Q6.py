########################################################################
#
# Name:         A25Q6.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################


import pandas as pd

def Train_test():

    data = {'Grade': 
            ['A+', 'B', 'A', 'C', 'B+']
            }
    df = pd.DataFrame(data)

    
    grades = {'A+': 'Excellent','A': 'Very Good','B+': 'Good','B': 'Average','C': 'Poor'}

    
    df['Grade'] = df['Grade'].map(grades)
    print(df)

    
def main():
    Train_test()

if(__name__ == "__main__"):
    main()


