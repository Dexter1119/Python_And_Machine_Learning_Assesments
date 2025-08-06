########################################################################
#
# Name:         A24Q4.py
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
    print(df)

    marks =  df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].values.flatten()
    labels = ['Maths','Science','English']

    plt.pie(marks, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.title("Sagar's Subject-wise Marks Distribution")
    plt.axis('equal')  
    plt.show()
    

def main():
    PdDataFrame()

if(__name__) == "__main__":
    main()