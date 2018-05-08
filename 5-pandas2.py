import pandas as pd
import matplotlib.pyplot as plt

housing=pd.read_csv("data/housing.csv")

print("-"*10)
print(housing.head())
print("-"*10)
print(housing.info())
print("-"*10)
print(housing.describe())
print("-"*10)
print(housing.sort_values(by='population', ascending=False).head()[['population', 'median_income']])
print("-"*10)
print(housing["ocean_proximity"].value_counts())
print("-"*10)

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

corr = housing.corr()
print(corr["median_house_value"].sort_values())

from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12,8))
plt.show()

housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
plt.show()

            