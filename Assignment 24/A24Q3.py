########################################################################
#
# Name:         A24Q3.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################

import pandas as pd

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
    
    print(df)

    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

    # Fit and transform the 'Gender' column
    encoded_data = encoder.fit_transform(df[['Gender']])

    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Gender']))

    Avg_By_Gender = df.groupby('Gender')['Total'].mean()
    print(Avg_By_Gender)

def main():
    PdDataFrame()

if(__name__) == "__main__":
    main()