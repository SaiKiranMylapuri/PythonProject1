import pandas as pd
df=pd.read_csv("C:/Users/rm489/PycharmProjects/PythonProject1/practice.csv")
df["city of residence"]=df["city of residence"].fillna("dwaraka")
print(df)