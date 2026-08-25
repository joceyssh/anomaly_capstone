# Transaction Anomaly Detection

A portfolio project applying unsupervised anomaly detection and observability
monitoring to financial transaction data — built as part of a pivot toward
AI/data governance roles.

## What this project does
- Loads and inspects a transaction dataset (284,807 rows, 31 features)
- Flags potentially fraudulent transactions using Isolation Forest
  (unsupervised anomaly detection — no fraud labels used during training)
- Logs every flagged transaction with a timestamp for audit purposes
- Monitors drift: tracks whether the flag rate changes across time windows
- Triggers an alert when a window's flag rate exceeds 2x the rolling average

See [GOVERNANCE.md](./GOVERNANCE.md) for scope, roles, escalation criteria,
and known limitations.

## Results (this run)
- 285 transactions flagged out of 284,807
- 122 of 492 known fraud cases caught (~25%)
- 2 time windows flagged for drift (exceeding 2x average flag rate)



## How to run it

**1. Clone the repo and enter the folder**
```bash
git clone https://github.com/joceyssh/anomaly_capstone.git
cd anomaly_capstone
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv capstone_env
source capstone_env/bin/activate
```

**3. Install dependencies**
```bash
pip install pandas scikit-learn
```

**4. Add the dataset**
Download the "Credit Card Fraud Detection" dataset from Kaggle (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place
`creditcard.csv` inside the `data/` folder. (Not included in this repo —
see note below.)

**5. Run the script**
```bash
python3 capstone.py
```

## Project structure
```
anomaly_capstone/
├── capstone.py          # main script — data load, scoring, logging, drift check
├── GOVERNANCE.md         # governance charter — scope, RACI, escalation, limitations
├── data/                 # dataset (not tracked in git — see setup step 4)
├── logs/                 # flagged transaction logs, generated on run
└── output/               # reserved for future output/reports
```

## Why the dataset isn't included
The dataset is publicly available on Kaggle but not redistributed here to
keep the repo lightweight and respect Kaggle's terms. Download it directly
from the source linked above.

## Next steps / future iterations
- Add a human-in-the-loop review interface for flagged transactions
- Calibrate the contamination rate against a validation process rather than
  an estimate
- Expand drift detection with a statistical test (e.g., Kolmogorov-Smirnov)
  for more rigorous comparison between time windows

## Author
Jocelyn Saw — built as part of a pivot toward AI/data governance roles.
Linked link www.linkedin.com/in/jocelyn-saw-8a412a3b 
