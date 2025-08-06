########################################################################
#
# Name:         A23Q7.py
# Description:  Program which Implemented Pandas assignement -> pie chart
# Author:       Pradhumnya Changdev Kalsait.
# Date:         19/07/25
#
########################################################################

import pandas as pd
import matplotlib.pyplot as plt



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

    marks = df[df['Name'] == 'Amit'][['Math','Science',"English"]].values.flatten()
 
    print(marks)

    subjects = ['Math','Science',"English"]

    plt.plot(subjects,marks,marker ='o')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit Report")
    plt.grid(True)
    plt.show()    

    

def main():
    dataFrame()

if(__name__ == "__main__"):
    main()