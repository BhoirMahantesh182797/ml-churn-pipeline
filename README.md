# Customer Churn Data Pipeline

## 📖 Project Overview
This project builds an end-to-end batch pipeline for Customer Churn prediction, prioritizing robust data engineering over ML algorithms. Using the Medallion Architecture (Bronze, Silver, Gold), it ingests, cleans, and engineers telecom data. It emphasizes modular Python, data quality, and scalability.

## 🏗️ Architecture
1. **Bronze (Raw):** Ingests raw data without modifications.
2. **Silver (Cleanse):** Handles missing values, removes duplicates, enforces types.
3. **Gold (Curated):** Aggregates data and engineers features for ML.
4. **Serving:** Trains the model and generates predictions.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Version Control:** Git/GitHub

## 🚀 How to Run
1. Clone repo: `git clone [your-repo-url]`
2. Create env: `python -m venv .venv`
3. Activate & install: `source .venv/bin/activate && pip install -r requirements.txt`

4. Run pipeline: `python src/ingestion/ingest_raw.py`