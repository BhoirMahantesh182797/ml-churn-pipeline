import logging
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_and_evaluate_model():
    logging.info("Starting Model Training process...")

    gold_path = "data/gold/ml_ready_churn_data.csv"
    model_dir = "models"
    model_path = os.path.join(model_dir, "churn_prediction.pkl")

    os.makedirs(model_dir, exist_ok=True)

    try:
        # Step 1 Load the Gold Dataset
        logging.info("Loading ML-ready data from: {gold_path}")
        df = pd.read_csv(gold_path)

        # Step 2 Seperate features (x) and target (y)
        y = df["churn"]
        X = df.drop(columns=["churn"])

        logging.info(f"Features (X) Shape: {X.shape}")
        logging.info(f"Target (y) shape: {y.shape}")

        # Step 3 Split into Training and Testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logging.info("Split data into training (80%) and testing (20%) sets.")

        # Step 4 Train the Machine Learning Model
        logging.info("Training Random Forest Classifier...")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        logging.info("Model training complete.")

        # Step 5 Evaluate the Model
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        logging.info(f"Model Accuracy: {accuracy * 100:.2f}%")

        logging.info("Classification Report:\n" + classification_report(y_test, y_pred))

        # Step 6 Save the Model
        joblib.dump(model, model_path)
        logging.info(f"Model successfully saved to: {model_path}")

    except Exception as e:
        logging.error(f"Failed to train model: {e}")
        raise

if __name__ == "__main__":
    train_and_evaluate_model()