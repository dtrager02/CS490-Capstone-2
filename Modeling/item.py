import os
import csv
import pandas as pd
#import plotly.express as px

cwd = os.getcwd()  # Get the current working directory (cwd)
#print(cwd)
df = pd.read_csv(cwd + "\Data\products\products.csv")
#print(df.head(10))
df = df.drop_duplicates().sort_values("product_id")
print(df.head(10))
tfile = open('items.txt', 'w', encoding='utf-8')
tfile.write(df.to_string(header = True, index = False))
tfile.close()
old = cwd + "\\items.txt"
new = cwd + "\\items.item"
os.rename(old, new)
