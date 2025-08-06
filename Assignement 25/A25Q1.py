########################################################################
#
# Name:         A25Q1.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################
"""
The Interquartile Range (IQR) method is a statistical technique used to identify outliers in a dataset and to understand the spread of the middle 50% of the data. 
It involves calculating the difference between the third quartile (Q3) and the first quartile (Q1) of a dataset. 
"""


import numpy as np

def CalculateIQR():

    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
    
    Q1 = np.percentile(data['Salary'], 25)            # Calculate Q1 (25th percentile)

    
    Q3 = np.percentile(data['Salary'], 75)            # Calculate Q3 (75th percentile)

    
    IQR = Q3 - Q1                                   # Calculate IQR

    print(f"The 25th percentile Quartile is {Q1}")
    print(f"The 75th percentile Quartile is {Q3}")
    print(f"IQR: {IQR}")

def main():
    CalculateIQR()


if(__name__ == "__main__"):
    main()


