# Governance Charter — Transaction Anomaly Detection

## 1. Scope Statement
This project implements an unsupervised anomaly detection system for identifying
potentially fraudulent transactions in financial data. It uses Isolation Forest
to flag statistical outliers, paired with a drift-monitoring layer that tracks
whether flagging behavior changes over time.

**In scope:** anomaly scoring, logging, drift detection, alert thresholds.
**Out of scope:** production deployment, real-time processing, real customer
data (this project uses a public/synthetic dataset), automated decision-making
without human review.

## 2. Roles (RACI)
| Role | Responsibility | Assigned To |
|---|---|---|
| Model Owner | Builds, maintains, and validates the scoring model | Jocelyn Saw   |
| Reviewer | Validates flagged transactions before action is taken | Jocelyn Saw
| Escalation Owner | Decides response when a drift alert triggers | Jocelyn Saw

## 3. Escalation Criteria
- Alert triggers when a time window's flag rate exceeds **2x the rolling
  average** flag rate across all windows.
- Triggered windows are logged separately and require review before being
  dismissed or acted on.
- The first response to a drift alert is to rule out technical causes: check whether the data pipeline changed (new data source, schema change, missing fields) before assuming the underlying transaction behavior actually shifted.
- After pipeline review is cleared, reviewer re-examines the flagged transactions in that window manually, checking whether the pattern reflects genuine anomalous activity or a data quality issue (e.g., a batch upload error, a change in transaction volume from a business event, missing values).

## 4. Milestone Plan
- Phase 1 (complete): Data ingestion, cleaning, anomaly scoring
- Phase 2 (complete): Logging, drift detection, alert threshold
- Phase 5 (this document): Governance framing
- Phase 6: Documentation polish, repository finalization

## 5. Known Limitations
- Model caught approximately 25% of known fraud cases in this dataset
  (122 of 492) at current settings — not production-ready performance 
- Contamination rate (0.001) was set as an estimate, not calibrated against
  a validation process.
- No human-in-the-loop review interface was built in this version — flagged
  transactions are logged but not routed to an actual reviewer.
