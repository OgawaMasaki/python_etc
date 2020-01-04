#Pandasをインポート
import pandas as pd

#変換したいJSONファイルを読み込む
df = pd.read_json("pokemon_data.json",encoding="utf-8")

#typesカラムを新たに作ったdftypeにコピー
dftypes = df.types

print("======================================")
print(type(dftypes[1]))

#dft = dftypes.str.split(", ")
for i in range(len(dftypes)):
    for j in range(len(dftypes[i])):
        #一つずつ辞書型に格納
        df["type"+str(j)] = dftypes[i][j]

#df.types = df.types.str.split(",", expand=True)
print("======================================")
print(df.type1)
print(df.type2)


#CSVに変換して任意のファイル名で保存
df.to_csv("pokemon_data1.csv",encoding="shift-jis")