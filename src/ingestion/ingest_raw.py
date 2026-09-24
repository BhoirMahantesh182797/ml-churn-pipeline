import logging
import pandas as pd
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ingest_raw_data():
    logging.info("Starting ingestion of raw data...")

    data_url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

    bronze_dir = "data/bronze"
    output_path = os.path.join(bronze_dir, "raw_churn_data.csv")

    os.makedirs(bronze_dir, exist_ok=True)

    try:
        logging.info(f"Fetching data from {data_url}...")

        df = pd.read_csv(data_url)

        logging.info(f"successfully ingested data with shape {df.shape}. Saving to {output_path}...")

        df.to_csv(output_path, index=False)

        logging.info(f"Raw data successfully saved to {output_path}. Ingestion complete.")
    
    except Exception as e:
        logging.error(f"Failed to ingest raw data: {e}")

        raise

if __name__ == "__main__":
    ingest_raw_data()