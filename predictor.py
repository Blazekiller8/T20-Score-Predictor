import pickle
from calculations import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error

def predictRuns(file_name):
    calc(file_name)
    data = pd.read_csv('testCase-1.csv')
    data = data.dropna()
    data = data.reset_index(drop=True)
    X = data.iloc[:,[2]].values
    Y = data.iloc[:,[3]].values
    train_X, val_X, train_Y, val_Y = train_test_split(X, Y, random_state = 1)
    # print(x)
    lr = LinearRegression()
    lr.fit(train_X,train_Y)
    y_pred = lr.predict(val_X)
    prediction = round(np.sum(y_pred)/y_pred.size)
    return(prediction)
    # return prediction