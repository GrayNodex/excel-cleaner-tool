import pandas as pd

df = pd.read_excel("data.xlsx")

print(df)

print(type(df["id"]))
print(df["id"].get(0))

print(df.head())   # 前5行
print(df.shape)    # 行列数
print(df.columns)  # 列名

print(df["score"].mean())
print(df["score"].max())

print(df.isnull().sum())

print("人数：", len(df))
print("平均分:", df["score"].mean())
print("最高分:", df["score"].max())


# 清洗
    # 数据规则
    # 必需字段: id, name, age, score
    # 唯一字段: id
    # 不允许空值

    # 清洗步骤
    # 1. 删除含有空值的行
    # 2. 按id去重
    # 3. 保留第一行

    # 验证方式
    # 是否有空值
    # 是否有重复id

# 删除带有空值的行
# 找到并存储带有空值的行的信息
to_drop = df[df["id"].isna() | df["name"].isna()]
to_drop["reason"] = "missing id or name"

# 删除带有空值的行的信息
df = df.dropna(subset=["id", "name"])

# 输出删除的信息
print("删除信息:\n", to_drop)

# 删除id重复的行
# 找到将要被删除的，带有重复id的行
to_drop = df[df.duplicated(subset=["id"], keep="first")] 
to_drop["reason"] = "duplicate id"
# .duplicated() 决定谁重复
# keep="first" 只记录第二行及以后行

df = df.drop_duplicates(subset=["id"], keep="first")
# .drop_duplicates() 决定保留谁
# keep="first" 只保留第一行

print("删除信息:\n", to_drop)

# 将清洗后的数据存储到硬盘中
df.to_excel("test.xlsx", index=False)