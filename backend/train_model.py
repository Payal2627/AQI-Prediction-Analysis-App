import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Load dataset
df = pd.read_csv("final_dataset.csv")

# Features used by frontend
FEATURES = [
    "PM2.5",
    "PM10",
    "NO2",
    "SO2",
    "CO",
    "Ozone"
]

TARGET = "AQI"

# Remove missing values
df = df.dropna()

X = df[FEATURES]
y = df[TARGET]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scale data
scaler = RobustScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = GradientBoostingRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)

# Train
model.fit(X_train_scaled, y_train)

# Evaluate
predictions = model.predict(X_test_scaled)

print("\n========== MODEL PERFORMANCE ==========")
print("R2 Score :", round(r2_score(y_test, predictions), 4))
print("MAE      :", round(mean_absolute_error(y_test, predictions), 4))
print("=======================================")

# Save files
joblib.dump(model, "aqi_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nModel saved successfully.")
print("Generated:")
print(" - aqi_model.pkl")
print(" - scaler.pkl")