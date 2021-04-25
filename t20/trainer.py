import pandas as pd
import numpy as np

def convert(tar_file):
    dataset = pd.read_csv(tar_file)
    df = pd.DataFrame(dataset)
    team_encoding = {
    "M Chinnaswamy Stadium":0,
    "Punjab Cricket Association IS Bindra Stadium, Mohali":1,
    "Feroz Shah Kotla":2,
    "Eden Gardens":3,
    "Wankhede Stadium":4,
    "Sawai Mansingh Stadium":5,
    "MA Chidambaram Stadium, Chepauk":6,
    "Rajiv Gandhi International Stadium, Uppal":7,
    "Dr DY Patil Sports Academy":8,
    "Newlands":9,
    "SuperSport Park":10,
    "Buffalo Park":11,
    "Kingsmead":12,
    "New Wanderers Stadium":13,
    "St George's Park":14,
    "Dubai International Cricket Stadium":15,
    "Sheikh Zayed Stadium":16,
    "Sharjah Cricket Stadium":17,
    "Arun Jaitley Stadium":18,
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium":19,
    "JSCA International Stadium Complex":20,
    "Brabourne Stadium":21,
    "Barabati Stadium":22,
    "Subrata Roy Sahara Stadium":23,
    "OUTsurance Oval":24,
    "Nehru Stadium":25,
    "Saurashtra Cricket Association Stadium":26,
    "M.Chinnaswamy Stadium":27,
    "Holkar Cricket Stadium":28,
    "De Beers Diamond Oval":29,
    "Himachal Pradesh Cricket Association Stadium":30,
    "Punjab Cricket Association IS Bindra Stadium":31,
    "Green Park":32,
    "Vidarbha Cricket Association Stadium, Jamtha":33,
    "Wankhede Stadium, Mumbai":34,
    "Shaheed Veer Narayan Singh International Stadium":35,
    "Sardar Patel Stadium, Motera":36,
    "Rajiv Gandhi International Stadium":37,
    "Maharashtra Cricket Association Stadium":38,
    "MA Chidambaram Stadium, Chepauk, Chennai":39,
    "MA Chidambaram Stadium":40,
    "Punjab Cricket Association Stadium, Mohali":41
    }

    team_encoding_dict ={
    "venue":team_encoding,
    }
    df.replace(team_encoding_dict,inplace=True)
    return df

def train():
    dataset = pd.read_csv("all_matches.csv")
    df = convert("all_matches.csv") 
    y = df.iloc[:,[3]].values  
    X = df.iloc[:,[11]].values
    count_row = y.shape[0]
    sum = [[0] * 2 for i in range(42)]
    tot_6 = [[]  for i in range(42)]
    for i in range(count_row):
        sum[y[i][0]][0] += X[i][0]
        sum[y[i][0]][1] += 1
        if sum[y[i][0]][1]==36:
            tot_6[y[i][0]].append(sum[y[i][0]][0])
            sum[y[i][0]][0] = 0
            sum[y[i][0]][1] = 0
    y=np.array(y)
    y = y.flatten()
    y = np.unique(y).tolist()
    df = pd.DataFrame(y)
    df.insert(1,"",tot_6,allow_duplicates=True)
    df.dropna()
    df.to_csv('testCase-1.csv',encoding='utf-8',mode='w')
