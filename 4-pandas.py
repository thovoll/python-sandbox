import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table.
# It is generally the most commonly used pandas object.

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'],
                   'B': np.random.randint(1, 10, 4)})
print("-"*10)
print(df)

# Project by label
p = df[['A']]
print("-"*10)
print(p)
print(type(p))

# Select by index (single row results in Series)
s = df.iloc[0]
print("-"*10)
print(s)
print(type(s))

# Select by index (multiple rows result in DataFrame)
s = df.iloc[0:1]
print("-"*10)
print(s)
print(type(s))

# Select by label (single row results in Series)
s = df.loc[0]
print("-"*10)
print(s)
print(type(s))

# Select by label (multiple rows result in DataFrame)
s = df.loc[0:1]
print("-"*10)
print(s)
print(type(s))

# Select rows and project columns by label
sp = df.loc[0:1, ['A']]
print("-"*10)
print(sp)
print(type(sp))

# Selection by criterion, then projection
s = df[df['B'] > 4]['A']
print("-"*10)
print(s)
print(type(s))

# Group by
gs = df.groupby('A').sum()
print("-"*10)
print(gs)
print(type(gs))

# Pivot table
pt = pd.pivot_table(df, values='B', index=['A'], aggfunc='sum')
print("-"*10)
print(pt)
print(type(pt))

# Plotting
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print("-"*10)
print(ts.head())
ts = ts.cumsum()
ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
print("-"*10)
print(df.head())
df = df.cumsum()
df.plot()
plt.show()

# More: https://pandas.pydata.org/pandas-docs/stable/10min.html
