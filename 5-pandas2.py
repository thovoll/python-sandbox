import pandas as pd
import matplotlib.pyplot as plt

housing=pd.read_csv("data/housing.csv")

print(housing.head())
print(housing.info())
print(housing["ocean_proximity"].value_counts())

housing.hist(bins=50, figsize=(20,15))
plt.show()

housing.plot(kind="scatter", x="longitude", y="latitude")
plt.show()