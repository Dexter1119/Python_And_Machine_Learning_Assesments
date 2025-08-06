########################################################################
#
# Name:         A25Q9.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################


import pandas as pd
from sklearn.model_selection import train_test_split

def split_data():
    
    data = {
        'Age': [25, 30, 45, 35, 22],
        'Salary': [50000, 60000, 80000, 65000, 45000],
        'Purchased': [1, 0, 1, 0, 1]
    }

    
    df = pd.DataFrame(data)

    
    x = df[['Age', 'Salary']]      
    y = df['Purchased']            

    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print("Training Features:\n", X_train)
    print("Testing Features:\n", X_test)
    print("Training Labels:\n", y_train)
    print("Testing Labels:\n", y_test)
def main():
    split_data()

if(__name__ == "__main__"):
    main()


