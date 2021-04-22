# from calculations import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predictRuns():
    data = pd.read_csv('testCase-1.csv')
    data = data.dropna()
    data = data.reset_index(drop=True)
    x = data.iloc[:,[2]].values
    y = data.iloc[:,[3]].values
    # print(x)
    lr = LinearRegression()
    lr.fit(x,y)
    prediction = lr.predict(y)
    print(prediction)
    

predictRuns()