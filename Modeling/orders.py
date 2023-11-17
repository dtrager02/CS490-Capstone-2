import os
import csv
import pandas as pd
#import plotly.express as px

cwd = os.getcwd()  # Get the current working directory (cwd)
#print(cwd)
df = pd.read_csv(cwd + "\orders.inter", sep = '\t')
#print(df.head(10))
df['label:float'] = 1.0
print(df.head(10))
f_path = cwd+'\\orders2.txt'
print(f_path)
df.to_csv(f_path,header=True,index = False, sep = '\t')
print("here0")
#f = open(f_path, 'w')
#print("here")
#t_s = df.to_string(header = True, index = False)
print("here1")
#f.write(t_s)
#print("here2")
#f.close()
#print("here3")
old = f_path
new = cwd+"\dataset\orders\orders.inter"
print(old)
print(new)
os.rename(old, new)
