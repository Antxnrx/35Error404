# 🚗 ETA Prediction Web App (Bangalore)

This is a machine learning-based **ETA (Estimated Time of Arrival) predictor** for Bangalore, India. The app uses a trained **Random Forest Regressor** model to estimate travel time based on:
- Start & End coordinates
- Day of the week
- Time of the day
- Haversine distance

The project includes a **Flask backend** and a simple **HTML/CSS/JS frontend**, and it's deployable on platforms like **Render**.

---

## 🔧 Features

- Predict ETA in minutes using real coordinates and time.
- Distance calculated using the Haversine formula.
- Frontend form to collect user input.
- Backend API using Flask.
- Model loading using `joblib`.

---

## 🧠 ML Model

- **Model**: Random Forest Regressor
- **Libraries**: scikit-learn, pandas
- **Target Variable**: `duration_min`
- **Input Features**:
  - `start_lat`, `start_lon`
  - `end_lat`, `end_lon`
  - `day_of_week`, `hour`, `minute`
  - `distance_km` (Haversine)



