import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
df = pd.read_csv("car_prices.csv")

# Filter for Jeep models before doing anything else, assuming 'model' is a column in your CSV
df_jeep = df[df['model'] == 'Jeep']

# Since predicting 'year' as a target with 'year' as a feature doesn't make sense, let's assume the target is 'price'
features = ['year', 'make', 'model', 'mileage', 'color']  # Assuming 'mileage' is also a relevant feature
target = 'price'

# Ensuring the features list only contains columns present in df_jeep and excluding the target
features = [feature for feature in features if feature in df_jeep.columns and feature != target]

# Splitting data into features (X) and target (y) based on the corrected features list
X = df_jeep[features]
y = df_jeep[target]

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model to the training data
rf_model.fit(X_train, y_train)

# Predict on the test data
predictions = rf_model.predict(X_test)

# Creating a DataFrame with actual and predicted prices for comparison
results_df = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': predictions})

# Display the first few rows of the results
print(results_df.head())

# Save the predictions to a CSV file
results_df.to_csv('jeep_model_price_predictions.csv', index=False)
