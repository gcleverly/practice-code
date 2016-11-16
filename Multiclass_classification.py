## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
print(cars.head())
unique_regions = cars["origin"].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
print(cars.head())
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)
cars = cars.drop("year", axis=1)
cars = cars.drop("cylinders", axis=1)
print(cars.head())

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
highest_train_row = int(cars.shape[0] * .70)
train = shuffled_cars.iloc[0:highest_train_row]
test = shuffled_cars.iloc[highest_train_row:]