def LabelEncoder(x):
    if x == 'convertible': 
        return 1
    elif x == 'hatchback':
        return 2
    elif x == 'sedan':
        return 3
    elif x == 'wagon':
        return 4
    else: 
        return 5
def square(x):
    return x ** 2

print(square(100))

import pandas as pd

data = pd.read_csv('datasets_383055_741735_CarPrice_Assignment.csv')

print(data.head(30))