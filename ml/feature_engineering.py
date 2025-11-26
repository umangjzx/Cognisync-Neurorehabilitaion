import pandas as pd

def build_features(df, patient_id_col="patient_id", time_col="created_at"):
    # Sort by patient + time
    if time_col in df.columns:
        df = df.sort_values(by=[patient_id_col, time_col])
    else:
        df["session_index"] = df.groupby(patient_id_col).cumcount()

    # Add rolling averages
    df["session_index"] = df.groupby(patient_id_col).cumcount()
    for col in df.select_dtypes(include='number').columns:
        if col not in [patient_id_col]:
            df[f"{col}_rolling_mean"] = df.groupby(patient_id_col)[col].rolling(3, min_periods=1).mean().reset_index(0, drop=True)

    return df
