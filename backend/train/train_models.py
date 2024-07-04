import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np
import os

def preprocess_data(data):
    data['type'] = data['type'].map({'villa': 1, 'rumah': 0})
    location_encoder = OneHotEncoder()
    location_features = location_encoder.fit_transform(data[['location']]).toarray()
    location_feature_names = location_encoder.get_feature_names_out(['location'])
    X = np.hstack([data[['bedroom', 'bathroom', 'carport', 'land_area', 'build_area', 'type']], location_features])
    feature_names = ['bedroom', 'bathroom', 'carport', 'land_area', 'build_area', 'type'] + list(location_feature_names)
    
    # Normalisasi fitur
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    y = data['price']
    return X, y, feature_names, scaler

# Load data
data = pd.read_csv('data_rumah_clean.csv')
X, y, feature_names, scaler = preprocess_data(data)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
models = {
    'linear_regression': LinearRegression(),
    'random_forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'gradient_boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
}

mse_results = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f'../models/{model_name}.pkl')
    
    # Predict and calculate MSE
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mse_results[model_name] = mse
    print(f'Model: {model_name}, MSE: {mse}')

# Save feature names, scaler and minimum threshold
os.makedirs('../models', exist_ok=True)
joblib.dump(feature_names, '../models/feature_names.pkl')
joblib.dump(scaler, '../models/scaler.pkl')
min_price_threshold = data['price'].min() * 0.1  # Set minimum threshold to 10% of the minimum price
joblib.dump(min_price_threshold, '../models/min_price_threshold.pkl')

# Save MSE results
mse_df = pd.DataFrame(list(mse_results.items()), columns=['Model', 'MSE'])
mse_df.to_csv('../models/mse_results.csv', index=False)
