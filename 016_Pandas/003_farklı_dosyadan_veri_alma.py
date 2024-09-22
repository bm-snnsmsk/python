import pandas as pd
import sqlite3

df = pd.read_csv("DataSets/sample.csv")
df = pd.read_json("DataSets/sample.json", encoding="UTF-8")
df = pd.read_excel("DataSets/sample.xlsx")        ##  pip install xlrd bu çalışmadı## pip install openpyxl

conn = sqlite3.connect("DataSets/sample.db")
df = pd.read_sql_query("SELECT * FROM students", conn)  ##  pip install pysqlite3 ve import sqlite3



# print(conn)
print(df)