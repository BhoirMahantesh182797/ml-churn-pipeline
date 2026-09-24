import logging
import pandas as pd
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_silver_data():
    logging.info("Starting Silver layer data cleaning process..")

    bronze_path = "data/bronze/raw_churn_data.csv"
    silver_dir = "data/silver"
    silver_path = os.path.join(silver_dir, "cleaned_churn_data.csv")

    os.makedirs(silver_dir, exist_ok=True)

    try:
        logging.info(f"Reading raw data from: {bronze_path}")
        df = pd.read_csv(bronze_path)
        logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

        df.columns = df.columns.str.lower().str.replace(' ', '_')
        logging.info("Cleaned cloumn names to snake_case.")

        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
        logging.info("Converted 'totalcharges' to numeric, coercing errors to NaN.")

        df = df.drop_duplicates()
        logging.info(f"Dropped duplicates. Remaining rows: {df.shape[0]}.")

        df.to_csv(silver_path, index=False)
        logging.info(f"Cleaned data successfully saved to: {silver_path}")

    except Exception as e:
        logging.error(f"Failed to clean data: {e}")
        raise

if __name__ == "__main__":
    clean_silver_data()