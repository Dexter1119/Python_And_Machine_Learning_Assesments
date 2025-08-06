########################################################################
#
# Name:         A25Q5.py
# Description:  Program which Implemented Pandas assignement -> 
# Author:       Pradhumnya Changdev Kalsait.
# Date:         20/07/25
#
########################################################################



from sklearn.model_selection import train_test_split

import pandas as pd

def Train_test():

   data = {'Age':
            [22, 25, 47, 52, 46, 56], 
           'Purchased': 
           [0, 1, 1, 0, 1, 0]}
   
   df = pd.DataFrame(data)

   
   X = df['Age']
   Y = df['Purchased']

   x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size= 0.2, random_state= 42)

   print(f"The x_train is:\n{x_train}")
   print(f"The x_test is:\n{x_test}")
   print(f"The y_train is:\n {y_train}")
   print(f"The y_test is:\n{y_test}")
   
   
def main():
    Train_test()

if(__name__ == "__main__"):
    main()


