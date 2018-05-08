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

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
plt.show()

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4, figsize=(10,7),
            s=housing["population"]/100, 
            c="median_house_value", cmap=plt.get_cmap("jet"))
plt.show()
            