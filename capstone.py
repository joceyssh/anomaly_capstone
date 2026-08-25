from pathlib import Path
import pandas as pd

# Set up project folders
project_root = Path(__file__).parent
(project_root / "data").mkdir(exist_ok=True)
(project_root / "logs").mkdir(exist_ok=True)
(project_root / "output").mkdir(exist_ok=True)

print("Folders created:", list(project_root.iterdir()))

df=pd.read_csv(project_root / "data" / "creditcard.csv") 
#Replace with your actual data file name
print (df.head())
print (df.info())
print (df.shape)

from sklearn.ensemble import IsolationForest

# Use only the anonymized features for scoring (exclude Time, Amount, Class for now)
features = df.drop(columns=["Time", "Amount", "Class"])

# Train the isolation forest
model = IsolationForest(contamination=0.001, random_state=42)
df["anomaly_score"] = model.fit_predict(features)

# -1 = flagged as anomaly, 1 = normal
print(df["anomaly_score"].value_counts())

comparison = pd.crosstab(df["Class"], df["anomaly_score"])
print(comparison)

import csv
from datetime import datetime

# Log every flagged anomaly with a timestamp
log_path = project_root / "logs" / "flagged_transactions.csv"

flagged = df[df["anomaly_score"] == -1].copy()
flagged["logged_at"] = datetime.now().isoformat()

flagged[["Time", "Amount", "Class", "anomaly_score", "logged_at"]].to_csv(
    log_path, index=False
)

print(f"Logged {len(flagged)} flagged transactions to {log_path}")

# Drift check: flag rate across time windows
df["time_window"] = pd.cut(df["Time"], bins=10)
drift_check = df.groupby("time_window", observed=True)["anomaly_score"].apply(
    lambda x: (x == -1).mean()
)

print("Flag rate per time window:")
print(drift_check)

avg_rate = drift_check.mean()
threshold = avg_rate * 2

alerts = drift_check[drift_check > threshold]
print(f"\nAverage flag rate: {avg_rate:.4f}")
print(f"Alert threshold (2x avg): {threshold:.4f}")
print("Windows exceeding threshold (drift alert):")
print(alerts)