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
