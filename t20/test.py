import pandas as pd
import numpy as np
# Importing the dataset
dataset = pd.read_csv('data/1237180.csv')

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
    else:
        avg_rate.append(np.nan)
        tot_run.append(np.nan)
        
    
    









df = pd.DataFrame(X)

df.insert(1,"run_rate",run_rate)
df.insert(2,"avg_rate",avg_rate)
df.insert(3,"tot_rate",tot_run)
df.dropna()
df.to_csv('testCase-1.csv',encoding='utf-8',mode='a')

# new_data = pd.read_csv('testCase-1.csv')
# y = new_data.iloc[:,[1]].values
# print(y)


# while True :
#     for i in X:
# """



#importing 



from sklearn.linear_model import LinearRegression

lr = LinearRegression()

data = pd.read_csv('testCase-1.csv')

data_ = pd.DataFrame(data)
# print(data)


avg = data_.iloc[:,[3]]
print(avg[1])
for j in avg:
        pass
print(avg)
#fitting into model
# lr.fit(avg,tr)


prediction = lr.predict(tr)
print(prediction)

print(avg)