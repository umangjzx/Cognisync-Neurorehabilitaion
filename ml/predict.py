import pickle
import sqlite3
import pandas as pd
from ml.feature_engineering import build_features

DB_PATH = "instance/neurobeat.db"
MODEL_PATH = "ml/model.pkl"

def predict_progress(patient_id: int):
    # Load model
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    # Load data
    con = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM baseline_assessments WHERE patient_id = ?;", con, params=(patient_id,))
    con.close()

    if df.empty:
        return {"patient_id": patient_id, "prediction": None, "error": "No data available"}

    df = build_features(df, patient_id_col="patient_id", time_col="created_at")

    features = df.drop(columns=["patient_id", "id", "created_at"], errors="ignore").select_dtypes(include="number")
    latest_features = features.iloc[[-1]]

    prediction = model.predict(latest_features)[0]
    return {"patient_id": patient_id, "prediction": float(prediction)}
