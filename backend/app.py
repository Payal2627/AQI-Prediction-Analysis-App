from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os
import requests

app = Flask(__name__)
CORS(app)

# =========================
# LOAD MODEL & SCALER
# =========================

MODEL_PATH = os.path.join(os.path.dirname(__file__), "aqi_model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# =========================
# AQI CATEGORY
# =========================

def aqi_category(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Satisfactory"

    elif aqi <= 200:
        return "Moderate"

    elif aqi <= 300:
        return "Poor"

    elif aqi <= 400:
        return "Very Poor"

    return "Severe"


# =========================
# HEALTH ADVICE
# =========================

def health_advice(aqi):

    if aqi <= 50:
        return "Air quality is excellent. Outdoor activities are safe."

    elif aqi <= 100:
        return "Air quality is acceptable for most people."

    elif aqi <= 200:
        return "Sensitive people should reduce prolonged outdoor activity."

    elif aqi <= 300:
        return "Limit outdoor activities and wear a mask if needed."

    elif aqi <= 400:
        return "Avoid prolonged outdoor exposure. Wear an N95 mask."

    return "Stay indoors whenever possible and use air purifiers."


# =========================
# HOME ROUTE
# =========================

@app.route("/")
def home():
    return "AQI Backend Running Successfully"


# =========================
# PREDICT AQI
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json(force=True)

        if not data:
            return jsonify({
                "error": "No data received"
            }), 400

        if "features" not in data:
            return jsonify({
                "error": "features key missing"
            }), 400

        features = data["features"]

        if len(features) != 6:
            return jsonify({
                "error": "Exactly 6 features required"
            }), 400

        features = [float(x) for x in features]

        if any(x < 0 for x in features):
            return jsonify({
                "error": "Negative values are not allowed"
            }), 400

        features = np.array(features).reshape(1, -1)

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)[0]

        prediction = max(0, prediction)

        return jsonify({
            "predicted_aqi": round(float(prediction), 2),
            "category": aqi_category(prediction),
            "advice": health_advice(prediction)
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================
# LOCATION AQI
# =========================

@app.route("/location_aqi")
def location_aqi():

    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({
            "error": "Latitude and Longitude required"
        }), 400

    API_KEY = "5f2efa4e75dbaea60ed6180385571fed"

    try:

        url = (
            f"https://api.openweathermap.org/data/2.5/air_pollution"
            f"?lat={lat}&lon={lon}&appid={API_KEY}"
        )

        response = requests.get(url)

        data = response.json()

        print(data)

        if "list" not in data:

            return jsonify({
                "error": data.get(
                    "message",
                    "Unable to fetch air quality data"
                )
            }), 400

        pollution_index = data["list"][0]["main"]["aqi"]

        categories = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }

        return jsonify({
            "aqi": pollution_index,
            "category": categories.get(
                pollution_index,
                "Unknown"
            )
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)