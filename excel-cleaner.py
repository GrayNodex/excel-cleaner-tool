import pandas as pd

df = pd.read_excel("data.xlsx")

print(df)

print(df.head())   # 前5行
print(df.shape)    # 行列数
print(df.columns)  # 列名