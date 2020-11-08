import pandas as pd 
import numpy as np
from sklearn import preprocessing
from sklearn.manifold import LocallyLinearEmbedding as LLE

class StandardScaler(object):
    '''Implement standard scaling ((x - mean) / std) scaling.'''
    def __init__(self):
        self.mean = None
        self.std = None

    def fit(self, x):
        self.mean = x.mean()
        self.std = x.std()
    
    def transform(self, x):
        result = x.astype(float)
        result -= self.mean
        result /= self.std
        return result

    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)

class NormalizationScaler(object):
    '''Implement normalization scaling ((x - minValue) / (maxValue - minValue)) scaling.'''
    def __init__(self):
        self.minValue = None
        self.maxValue = None 

    def fit(self, x):
        self.maxValue = max(x)
        self.minValue = min(x)

    def transform(self, x):
        range = self.maxValue - self.minValue
        result = x.astype(float)
        result -= self.minValue
        result /= range
        return result
    
    def fit_transform(self, x):
        self.fit(x)
        return self.transform(x)


class Make_Model:
    '''Create a column for the make and model and return a new dataframe'''
    
    def __init__(self):
        self.CarName = None
    def fit(self):
        ''' Initialize the lambda function '''
        self.make = lambda CarName: CarName.split()[0]
        self.model = lambda CarName: ' '.join(CarName.split()[1:])    
    def transform(self, x):
        x['Make'] = x['CarName'].apply(self.make)
        x['Model'] = x['CarName'].apply(self.model)
        return x
    def fit_transform(self, x):
        self.fit()
        return self.transform(x)


class LabelEncode:
    def __init__(self, df, columns = None):
        self.df = df
        self.columns = columns
        
    def LabelEncode(self):
        '''This function takes in a DataFrame and list of columns to encode.

        Input:
            df: DataFrame
            columns: list of columns to encode. If None, all the columns will
                be encoded
        Output: Encoded DataFrame
        '''
        le = preprocessing.LabelEncoder()
        if self.columns == None:
            for nm in self.df.columns:
                self.df[nm] = le.fit_transform(self.df[nm])
        elif type(self.columns) == list:
            for nm in self.columns:
                self.df[nm] = le.fit_transform(self.df[nm])
        else:
            self.df[columns] = le.fit_transform(self.df[columns])
        return self.df


def One_Hot_Encode(df, columns):
    pass

def Embedding:
    pass

