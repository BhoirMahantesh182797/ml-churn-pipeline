import logging
import pandas as pd
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def build_gold_features():
    logging.info("Starting Gold Layer feature engineering process...")

    silver_path = "data/silver/cleaned_churn_data.csv"
    gold_dir = "data/gold"
    gold_path = os.path.join(gold_dir, "ml_ready_churn_data.csv")

    os.makedirs(gold_dir, exist_ok=True)

    try:
        # Step 1 Read the silver data
        logging.info(f"Reading cleaned data from: {silver_path}")
        df = pd.read_csv(silver_path)
        logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

        # Step 2 Drop non-predictive columns
        df = df.drop(columns = ['customerid'])
        logging.info("Dropped 'customerid' column (non-predictive).")

        # Step 3 Feature Engineering
        bins = [0,12,36,72]
        labels = ['new', 'mid', 'long-term']
        df['tenure_group'] = pd.cut(df['tenure'], bins=bins, labels=labels, include_lowest=True)
        logging.info("Created 'charge_per_tenure' ratio feature.")

        # Step 4 Encode the Target Variable
        df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})
        logging.info("Encoded target variable 'churn' (Yes = 1, No = 0).")

        # Step 5 One-hot encode categorical variables
        df = pd.get_dummies(df, drop_first=True)

        bool_cols = df.select_dtypes(include = ['bool']).columns
        df[bool_cols] = df[bool_cols].astype(int)

        logging.info(f"One-hot enoded categorical variables. Final shape: {df.shape}")

        # Step 6 Data Quality validation

        null_count = df.isnull().sum().sum()
        if null_count > 0:
            logging.warning(f"Found {null_count} null values in the Gold dataset!")
            df = df.dropna()
            logging.info(f"Dropped rows with nulls. New Shape: {df.shape}")
        else:
            logging.info("Data quality check passed: No missing values found.")

        # Step 7 Save the Gold dataset
        df.to_csv(gold_path, index=False)
        logging.info(f"ML-ready data successfully saved to: {gold_path}")
        logging.info(f"Final dataset: {df.shape[0]} rows and {df.shape[1]} columns.")

    except Exception as e:
        logging.error(f"Failed to build Gold features: {e}")
        raise

if __name__ == "__main__":
    build_gold_features()