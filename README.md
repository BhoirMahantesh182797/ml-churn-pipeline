# Customer Churn Data Pipeline

## 📖 Project Overview
This project implements an end-to-end batch data pipeline to support a Customer Churn prediction model. Prioritizing robust data engineering over ML algorithms, the pipeline ingests raw telecom data, applies the Medallion Architecture (Bronze, Silver, Gold) to clean, validate, and engineer features, and ultimately trains and serializes a predictive model. 

## 🏗️ Architecture (Medallion)
1. **Bronze (Raw):** Ingests raw CSV data without modifications.
2. **Silver (Cleanse):** Enforces `snake_case`, handles missing values (`pd.to_numeric`), and drops duplicates.
3. **Gold (Curated):** Drops non-predictive IDs, bins tenure, creates ratio features, and one-hot encodes categorical variables.
4. **Serving (ML):** Splits data, trains a Random Forest Classifier, evaluates accuracy, and serializes the model using `joblib`.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn
* **Version Control:** Git/GitHub

## 📂 Project Structure
```text
ml-churn-pipeline/
├── data/
│   ├── bronze/      # Raw ingested data (Ignored by Git)
│   ├── silver/      # Cleaned data (Ignored by Git)
│   └── gold/        # ML-ready features (Ignored by Git)
├── models/          # Serialized .pkl models (Ignored by Git)
├── src/
│   ├── ingestion/   # Bronze layer scripts
│   ├── transform/   # Silver & Gold layer scripts
│   └── ml/          # Model training and evaluation
├── .gitignore
├── requirements.txt
└── README.md

🚀 How to Run
Clone repo: git clone https://github.com/BhoirMahantesh182797/ml-churn-pipeline.git
Navigate to folder: cd ml-churn-pipeline
Create env: python -m venv .venv
Activate & install: source .venv/bin/activate && pip install -r requirements.txt
Run the pipeline sequentially:
 python src/ingestion/ingest_raw.py
 python src/transform/clean_silver.py
 python src/transform/feature_gold.py
 python src/ml/train_model.py

Commit and push this final README:
```bash
git add README.md
git commit -m "Docs: Finalize README with complete pipeline architecture"
git push origin main
