import pandas as pd
import numpy as np
import csv
import re

def lfc():
    setx = 'エラー'

    df = pd.read_csv('data/src/logs.csv')
    df.iloc[1] = np.nan
    #print(df)
    #欠損値を除外
    df = df.dropna()
    #listへ変更
    df = df.values.tolist()

    alllist = []
    list1 = []
    errorlist = []


    for i in range(len(df)):

        #空白を削除
        df[i] = str(df[i]).replace(' ','')
        #矢印を削除
        df[i] = str(df[i]).replace('^','')
        #\n\rで分割
        list1 = df[i].split('\\r\\n')
        #appendで追加
        for k in range(len(list1)):
            alllist.append(list1[k])

    for j in range(len(alllist)):
        #無駄な文字列を削除（識別に必要ないもの 例：main.c:1:12）
        if 'main.c' in alllist[j]: 
            #deriteflag = 1 
            alllist[j] = str(alllist[j]).lstrip("main.c""1""2""3""4""5""6""7""8""9""0"":""[""\"""\'")
            
            #'の間のやつ削除 
            '''(ここコメントアウト外すとエラーの種類での分別になる) '''
            alllist[j] = re.sub("\'[^\']+\'", "", alllist[j])

            #'''\を削除'''
            alllist[j] = str(alllist[j]).replace("\\","")

            '''エラーだけを取り出したいなら'''
            if setx in alllist[j]: 
               errorlist.append(alllist[j])

    #errorの分別
    
    allerror = []
    flag = 0
    errorsum = [1]*10000

    for i in range(len(errorlist)):
        for j in range(len(allerror)):
            #同じものがあれば
            if str(errorlist[i]) == str(allerror[j]):
                flag = 1
                #総数に1追加
                errorsum[j] = errorsum[j] + 1
            else:
                continue
        #一回も出てこなかったら
        if flag == 0:
            allerror.append(errorlist[i])
        #初期化
        flag = 0

    csvlist = [[0]*3]*len(allerror)


    with open('data/output/.csv', 'w') as f:
        #タグ設定
        csvlist[0][0]=("番号")
        csvlist[0][1]=("エラー数")
        csvlist[0][1]=("エラー名")

        writer = csv.writer(f, lineterminator="\n") # 改行コード（\n）を指定しておく
        writer.writerow(csvlist[0])
        for w in range(len(allerror)):
            csvlist[w+1][0] = w
            csvlist[w+1][1] = errorsum[w]
            csvlist[w+1][1] = allerror[w]
            print(csvlist[w])

            writer.writerow(csvlist[w])

if __name__ == '__main__':
    lfc()

print('モジュール名：{}'.format(__name__))