import random
import pandas as pd
import pprint
from collections import OrderedDict
import csv

df = pd.read_csv('data/src/codeerror.csv',names=("エラー","コード"),encoding="shift-jis")

#print(df["エラー"].sum())
#sumerror = df["エラー"].sum()
print(len(df))
sumerror = len(df)


#連数
for i in range(10):
    print("\n")
    rand = random.randint(0,sumerror)
    print(str(i) + ":" + str(rand))
    print(df.at[rand,"コード"])
    print("------------------------")
    print(df.at[rand,"エラー"])
    print("========================")

csvlist = [[0]*3]*10
with open('data/output/error7_post4.csv', 'w') as f:
        #タグ設定
        csvlist[0][0]=("番号")
        csvlist[0][1]=("コード")
        csvlist[0][2]=("エラー")

        writer = csv.writer(f, lineterminator="\n") # 改行コード（\n）を指定しておく
        writer.writerow(csvlist[0])
        for w in range(9):
            #rand = random.randint(0,sumerror)
            i = 0
            while i < 3:
                rand = random.randint(0,sumerror)
                if "エラー" in df.at[rand,"エラー"]: 
                    csvlist[w+1][0] = w
                    csvlist[w+1][1] = df.at[rand,"コード"]
                    csvlist[w+1][2] = df.at[rand,"エラー"]
                    print(csvlist[w])
                    break
                    
                else:
                    continue

            writer.writerow(csvlist[w])