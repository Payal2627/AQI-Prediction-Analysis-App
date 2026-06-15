# 🌍 Air Quality Index Prediction & Analysis System

A Machine Learning-powered web application that predicts Air Quality Index (AQI) based on major air pollutants and provides real-time air quality information for the user's current location.

## 🚀 Features

* 📊 AQI Prediction using Machine Learning
* 🌎 Real-time AQI for Current Location
* 📈 AQI Trend Visualization with Charts
* 🎯 AQI Category Classification (Good, Moderate, Poor, etc.)
* 🩺 Health Recommendations based on AQI Levels
* 📱 Responsive and Modern User Interface
* ⚡ Flask REST API Backend
* 📍 Geolocation-based Air Quality Monitoring
* 🗂 Prediction History Tracking

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Backend

* Python
* Flask
* Flask-CORS

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### API Integration

* OpenWeather Air Pollution API

---

## 📂 Project Structure

```text
AQI-Prediction-Analysis-App
│
├── backend
│   ├── app.py
│   ├── train_model.py
│   ├── aqi_model.pkl
│   ├── scaler.pkl
│   └── final_dataset.csv
│
├── frontend
│   ├── landing.html
│   └── index.html
│
└── README.md
```

---

## 🤖 Machine Learning Model

The model is trained using air pollution parameters:

* PM2.5
* PM10
* NO₂
* SO₂
* CO
* Ozone

### Target Variable

* AQI (Air Quality Index)

### Model Pipeline

1. Data Cleaning
2. Feature Selection
3. Data Scaling using RobustScaler
4. Model Training using Gradient Boosting Regressor
5. Model Serialization using Joblib

---

## 🌍 AQI Categories

| AQI Range | Category     |
| --------- | ------------ |
| 0 - 50    | Good         |
| 51 - 100  | Satisfactory |
| 101 - 200 | Moderate     |
| 201 - 300 | Poor         |
| 301 - 400 | Very Poor    |
| 401+      | Severe       |

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Payal2627/AQI-Prediction-Analysis-App.git
```

### 2. Navigate to Project

```bash
cd AQI-Prediction-Analysis-App
```

### 3. Install Dependencies

```bash
pip install flask flask-cors pandas numpy scikit-learn joblib requests
```

### 4. Run Backend

```bash
cd backend
python app.py
```

Backend runs at:

```text
http://127.0.0.1:5000
```

### 5. Run Frontend

Open `landing.html` using Live Server in VS Code.

---

## 📍 Current Location AQI

The application uses the OpenWeather Air Pollution API to fetch:

* Real-time Air Quality Data
* AQI Category
* Location-based Pollution Information

---

## 🎯 Future Enhancements

* AQI Forecasting
* City-wise AQI Comparison
* User Authentication
* AQI Alerts & Notifications
* Weather Integration
* Deployment on Cloud

---

## 👩‍💻 Author

**Payal Malandkar**

GitHub: https://github.com/Payal2627

---

## ⭐ Acknowledgements

This project was enhanced and customized with:

* Improved Machine Learning Model Training
* UI/UX Enhancements
* Real-time AQI Integration
* Flask Backend Improvements
* Interactive Data Visualization

If you found this project useful, consider giving it a ⭐ on GitHub.
