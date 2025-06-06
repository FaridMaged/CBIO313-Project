# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and preprocessor
try:
    model = joblib.load('model.pkl')
    preprocessor = joblib.load('preprocessor.pkl')
    print("Model and preprocessor loaded successfully")
except Exception as e:
    print(f"Error loading model or preprocessor: {str(e)}")
    raise

@app.route('/')
def home():
    return "Diabetes Readmission Prediction API - POST to /predict"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input from request
        data = request.get_json(force=True)
        
        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Transform using preprocessor
        processed_data = preprocessor.transform(df)

        # Make prediction
        prediction = model.predict(processed_data)[0]

        # Return result
        return jsonify({
            'prediction': int(prediction),
            'readmitted': '<30' if prediction == 1 else 'NO'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=True only during development