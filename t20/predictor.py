from trainer import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def predictRuns(file_name):
    train()
    data = pd.read_csv('testCase-1.csv')
    data = data.dropna()
    data = data.reset_index(drop=True)
    X = data.iloc[:,[0]].values
    Y = data.iloc[:,[1]].values
    train_X, val_X, train_Y, val_Y = train_test_split(X, Y, random_state = 0)
    # print(x)
    lr = LinearRegression()
    lr.fit(train_X,train_Y)
    inp = convert(file_name)
    y = inp.iloc[:,[0]].values
    y_pred = lr.predict(y)
    prediction = round(np.sum(y_pred)/y_pred.size)
    return(prediction)