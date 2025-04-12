from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("rf_model.pkl")

# Dummy day mapping (update as per your dataset)
day_mapping = {
    0: 'Friday',
    1: 'Monday',
    2: 'Saturday',
    3: 'Sunday',
    4: 'Thursday',
    5: 'Tuesday',
    6: 'Wednesday'
}
day_mapping = {v: k for k, v in day_mapping.items()}

# Haversine distance function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))

# Home route - render form
@app.route('/')
def index():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        start_lat = float(data['start_lat'])
        start_lon = float(data['start_lon'])
        end_lat = float(data['end_lat'])
        end_lon = float(data['end_lon'])
        day_of_week = data['day_of_week'].capitalize()
        hour = int(data['hour'])
        minute = int(data['minute'])

        if day_of_week not in day_mapping:
            return jsonify({"error": "Invalid day of week."}), 400

        day_code = day_mapping[day_of_week]
        distance_km = round(haversine(start_lat, start_lon, end_lat, end_lon), 2)

        input_data = [[start_lat, start_lon, end_lat, end_lon, day_code, hour, minute, distance_km]]
        predicted_duration = model.predict(input_data)[0]

        return jsonify({
            "predicted_duration": predicted_duration
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
