# backend/tests/test_app.py

import unittest
import json
from app import app

class PredictPriceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_linear_regression(self):
        payload = {
            "bedroom": 3,
            "bathroom": 2,
            "carport": 1,
            "land_area": 150,
            "build_area": 100,
            "type_villa": 1,
            "type_rumah": 0,
            "method": "linear_regression"
        }
        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('prediction', data)

    def test_predict_random_forest(self):
        payload = {
            "bedroom": 2,
            "bathroom": 1,
            "carport": 1,
            "land_area": 120,
            "build_area": 80,
            "type_villa": 0,
            "type_rumah": 1,
            "method": "random_forest"
        }
        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('prediction', data)

    def test_predict_gradient_boosting(self):
        payload = {
            "bedroom": 4,
            "bathroom": 3,
            "carport": 2,
            "land_area": 200,
            "build_area": 150,
            "type_villa": 1,
            "type_rumah": 0,
            "method": "gradient_boosting"
        }
        response = self.app.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('prediction', data)

if __name__ == '__main__':
    unittest.main()
