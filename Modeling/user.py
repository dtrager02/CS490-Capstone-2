import os
import csv
import pandas as pd
#import plotly.express as px

cwd = os.getcwd()  # Get the current working directory (cwd)
#print(cwd)
df = pd.read_csv(cwd + "\Data\orders.csv")
#print(df.head(10))
df = df["user_id"].drop_duplicates().sort_values()
print(df.head(10))
tfile = open('users.txt', 'w')
tfile.write(df.to_string(header = True, index = False))
tfile.close()
old = cwd + "\\users.txt"
new = cwd + "\\users.user"
os.rename(old, new)
