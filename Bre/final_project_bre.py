import numpy as pd #liner algebra
import pandas as pd #data processing, CSV file final_project2

import os

import pandas as pd 
from sklearn.model_selection import train_test_split

# DataFrame 'df'
df = pd.read_csv("car_prices.csv")

# Ket features and target 
features = ['year', 'make', 'model', 'color', 'price']
target = 'year'

# Split data into features (X) and target (y)
X = df[features]
y = df[target]

# Split the dataset into training and test sets
X-train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Jeep model vehicles only
df = df[['model']= 'Jeep']

# dropping columns
df = df.drop(columns=['year', 'model', 'color', 'price'])

# dropping nuls 
df = df.dropna()

# reduce data 
df = df.sample(frac=.5,random_state=42)
# creating dataframe for year

df.head()



year_df = cleaned_df.drop(columns= make)

# data predictions
year_pred = rf_model.predict(X_year)


# create a random forest refressor 
rf_model = RandomForestRegressor(n_estimators=100, random_state_42)

# Model fit data
rf_model.fit(X_year_train, y_year_train)

# Predict on all data
Year_pred = rf_model.predict(X_year)

# Creating dataframe with predictions included
final_df = df
final_df['decade prediction'] = year_pred
final_df['model prediction'] = model_pred
final_df['price prediction'] = no_pred

final_df


# Pushing dataframe with predictions to a csv
final_df.to_csv('final_predictions_dodge.csv', index=False)

