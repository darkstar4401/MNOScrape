import pandas as pd
import numpy as np
import itertools


file = "/home/me/Documents/mnoConcat.csv"
cfile = "/home/me/Documents/mnCoins/"
df = pd.read_csv(file)
namegroup = df.groupby('Names')
names = df['Names']
names = list(set(names))
for name in names:
	curr = namegroup.get_group(name)
	curr = curr.sort_values(by=['Dates'], ascending=True)
	name = name.replace(" ","")
	pathname = cfile+name
	print(name)
	curr.to_csv(pathname)


