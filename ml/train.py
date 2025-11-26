import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pickle
import sqlite3
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from ml.feature_engineering import build_features

DB_PATH = "instance/neurobeat.db"
MODEL_PATH = "ml/model.pkl"

def train_model():
    con = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM baseline_assessments;", con)
    con.close()

    df = build_features(df, patient_id_col="patient_id", time_col="created_at")

    target = "id"   # <-- replace with actual progress column if available
    features = df.drop(columns=["patient_id", target, "created_at"], errors="ignore").select_dtypes(include="number")

    X = features
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"Model trained. RMSE: {rmse:.2f}")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
