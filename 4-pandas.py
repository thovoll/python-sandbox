import numpy as np
import pandas as pd

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table.
# It is generally the most commonly used pandas object.

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'],
                   'B': np.random.randint(1, 10, 4)})
print(df)

pt = pd.pivot_table(df, values='B', index=['A'], aggfunc='sum')
print(pt)

# More: https://pandas.pydata.org/pandas-docs/stable/10min.html
