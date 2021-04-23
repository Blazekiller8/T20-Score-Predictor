import pandas as pd
import numpy as np
import pickle
def calc(test_file):
    dataset = pd.read_csv(test_file)

    X = dataset.iloc[:,[11]].values

    df = pd.DataFrame(X)
    count_row = df.shape[0]
    sum= 0

    run_rate = []
    avg_rate = []
    agg = np.float64(0)

    tot_run = []
    for i in range(count_row):
        sum += X[i][0]
        runRate = round(sum/((i%36)+1/6),2)   
        run_rate.append(runRate)
        agg += runRate

        if (i>0)and(i%36 == 0) :
            val = round(agg/36,2)
            avg_rate.append(val)
            tot_run.append(sum)
            sum = 0
            # agg = 0
        else:
            avg_rate.append(np.nan)
            tot_run.append(np.nan)
    X1=np.array(run_rate)
    df = pd.DataFrame(X1)
    df.insert(1,"",avg_rate,allow_duplicates=True)
    df.insert(2,"",tot_run,allow_duplicates=True)
    df.dropna()

    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        # print(df)
    df.to_csv('testCase-1.csv',encoding='utf-8',mode='w')