# backend/app.py
import logging
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow all origins for debugging

api = Api(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

# Load models and data
models = {
    'linear_regression': joblib.load('models/linear_regression.pkl'),
    'random_forest': joblib.load('models/random_forest.pkl'),
    'gradient_boosting': joblib.load('models/gradient_boosting.pkl')
}

feature_names = joblib.load(os.path.join(os.path.dirname(__file__), 'models/feature_names.pkl'))
scaler = joblib.load(os.path.join(os.path.dirname(__file__), 'models/scaler.pkl'))
min_price_threshold = joblib.load(os.path.join(os.path.dirname(__file__), 'models/min_price_threshold.pkl'))
kabupaten_list = ["Badung", "Denpasar", "Gianyar", "Tabanan", "Bangli", "Buleleng", "Jembrana", "Karangasem", "Klungkung"]

def validate_input(data):
    required_fields = ['bedroom', 'bathroom', 'carport', 'land_area', 'build_area', 'type_villa', 'type_rumah', 'method']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

class Predict(Resource):
    def post(self):
        try:
            data = request.get_json()
            validate_input(data)

            bedroom = data['bedroom']
            bathroom = data['bathroom']
            carport = data['carport']
            land_area = data['land_area']
            build_area = data['build_area']
            type_villa = data['type_villa']
            type_rumah = data['type_rumah']
            method = data['method']

            logging.info(f"Received data: {data}")

            if method not in models:
                return jsonify({'error': 'Invalid prediction method specified'})

            model = models[method]
            predictions = {}
            for kabupaten in kabupaten_list:
                location_features = [1 if k == kabupaten else 0 for k in kabupaten_list]
                input_data = [bedroom, bathroom, carport, land_area, build_area, type_villa or type_rumah] + location_features

                logging.info(f"Expected number of features: {len(feature_names)}")
                logging.info(f"Number of input features: {len(input_data)}")

                if len(input_data) != len(feature_names):
                    logging.error(f"Feature mismatch: {len(input_data)} input features, {len(feature_names)} expected features")
                    return jsonify({'error': 'The number of input features does not match the model.'})

                input_data = scaler.transform([input_data])
                X = pd.DataFrame(input_data, columns=feature_names)
                logging.info(f"Predicting for {kabupaten} with input: {input_data}")
                prediction = model.predict(X)
                price = max(float(prediction[0]), float(min_price_threshold))  # Ensure predictions are not below threshold
                predictions[kabupaten] = price

            logging.info(f"Predictions: {predictions}")
            return jsonify(predictions)
        except Exception as e:
            logging.error(f"Error: {e}")
            return jsonify({'error': str(e)}), 500

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
