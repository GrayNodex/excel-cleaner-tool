import pandas as pd
from tkinter import filedialog
from tkinter import Tk
from tkinter import ttk
from tkinter import Toplevel

# UI MOdule

# File Selector Module
# Function:
# Name:
# select_file()

# Responsibility:
# Select input file

# Input:
# None

# Output:
# file_path(str)

# Error:
# No file selected
# Invalid extention

# choose_file():
def choose_file():
# 1. Get the file path
    file_path = filedialog.askopenfilename()
# 2. Verify the file path
# 2.1 If its type is tuple
    if isinstance(file_path, tuple):
#       if its type is None
        if not file_path:
#           return None
            return None
# 2.2 If its an empty str
    if file_path == '':
#       return None
        return None
# 3. If the file path is not None
    if not file_path:
#        Verify the file extention
#       While the file path does not end up with '.xslx'
        while not file_path.endswith('.xslx'):
#           call choose_file()    
            choose_file()
# retrun the file path
    return file_path
# #

# File Cleaner Module
# Function:
# Name:
# clean_file()

# Responsibility:
# Clean input file

# Input:
# file_path(str)

# Output:
# cleaned_file(pd)

# Error:
# File path is empty
# Invalid extention


# File Cleaner Module
def clean_file(file_path):
    df = None
# 1. Verify the file path
#   If it is not str
    if type(file_path) is not str:
        return df
#       if it is empty
        if file_path == '':
#           return None
            return df
#   If it does not end with '.xlsx'
    if not file_path.endswith('.xlsx'):
        return df
    
    df = pd.read_excel(file_path)
# 2. Clean the file content
#   Delete rows with blank
    df = df.dropna(subset=["id", "name"])
#   Delete rows with duplicate id
    df = df.drop_duplicates(subset=["id"], keep="first")
#
# 3. Save the cleaned file
    df.to_excel("~/output/cleaned_file.xlsx", index=False)
    return df

# # 1. Select a file
# def choose_file():
#     # Get the file name
#     file_name = filedialog.askopenfilename()

#     # Fisrt selection
#     if isinstance(file_name, tuple):
#         if not file_name:
#             # Return None if user cancels file selection at first time.
#             return None
#     # Other selections
#     elif file_name == '':
#         # Return None if user cancels file selection after the first time.
#         return None

# df = pd.read_excel("./input/data.xlsx")

# print(df)

# print(type(df["id"]))
# print(df["idd"].get(0))

# print(df.head())   # 前5行
# print(df.shape)    # 行列数
# print(df.columns)  # 列名

# print(df["score"].mean())
# print(df["score"].max())

# print(df.isnull().sum())

# print("人数：", len(df))
# print("平均分:", df["score"].mean())
# print("最高分:", df["score"].max())


# # 清洗
#     # 数据规则
#     # 必需字段: id, name, age, score
#     # 唯一字段: id
#     # 不允许空值

#     # 清洗步骤
#     # 1. 删除含有空值的行
#     # 2. 按id去重
#     # 3. 保留第一行

#     # 验证方式
#     # 是否有空值
#     # 是否有重复id

# # 删除带有空值的行
# # 找到并存储带有空值的行的信息
# to_drop = df[df["id"].isna() | df["name"].isna()]
# to_drop["reason"] = "missing id or name"

# # 删除带有空值的行的信息
# df = df.dropna(subset=["id", "name"])

# # 输出删除的信息
# print("删除信息:\n", to_drop)

# # 删除id重复的行
# # 找到将要被删除的，带有重复id的行
# to_drop = df[df.duplicated(subset=["id"], keep="first")] 
# to_drop["reason"] = "duplicate id"
# # .duplicated() 决定谁重复
# # keep="first" 只记录第二行及以后行

# df = df.drop_duplicates(subset=["id"], keep="first")
# # .drop_duplicates() 决定保留谁
# # keep="first" 只保留第一行

# print("删除信息:\n", to_drop)

# # 将清洗后的数据存储到硬盘中
# df.to_excel("test.xlsx", index=False)