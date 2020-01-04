import pandas as pd
import numpy as np
import csv
import pprint

df = pd.read_csv('data/src/logs.csv')
df.iloc[1] = np.nan
#print(df)
#欠損値を除外
df = df.dropna()
#listへ変更
df = df.values.tolist()

#classの確認
#print(type(df))
alllist = []

for i in range(len(df)):
    list1 = []
    #区切り文字で分割
    
    #空白を削除
    #df[i] = str(df[i]).replace(' ','')
    df[i] = str(df[i]).replace('^','')
    #\n\rで分割
    list1 = df[i].split('\\r\\n') 
    #appendで追加
    alllist.append(list1)
    #print(type(df[i]))
    #表示
    #print(str(df[i]) + '\n')

for j in range(len(alllist)):
    alllist[j] = str(alllist[j]).replace('\\','')
    print(str(j) + ':' +str(alllist[j]))
#with open('data/output/alllogs.csv','w',newline  ='') as csvFile:

#データの数だけ回す
