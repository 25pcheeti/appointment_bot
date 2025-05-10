"""
Train a logistic‑regression model to predict no‑shows.
Outputs:
  - models/logreg.pkl
  - reports/figures/roc_curve.png
"""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import RocCurveDisplay, classification_report
import matplotlib.pyplot as plt
import numpy as np

PROCESSED = Path(__file__).resolve().parents[2] / "data" / "processed" / "noshow_clean.csv"
MODEL_DIR = Path(__file__).parents[2] / "models"
FIG_DIR   = Path(__file__).parents[2] / "reports" / "figures"
MODEL_DIR.mkdir(exist_ok=True, parents=True)
FIG_DIR.mkdir(exist_ok=True, parents=True)

def main() -> None:

    df = pd.read_csv(PROCESSED)
#   df = df.dropna(subset=["No‑show"])
    # ----------  FEATURE ENCODING  ----------
    # target: 1 = "Yes" (no‑show), 0 = "No"
    
    df = df.dropna(subset=["No-show"])

    
    y = df["No-show"].map({"Yes": 1, "No": 0}).astype(int)

    X = df.drop(columns=["No-show"]).copy()

    # a) convert datetime columns to seconds since epoch
    for col in ["ScheduledDay", "AppointmentDay"]:
        X[col] = pd.to_datetime(X[col]).astype("int64") // 10**9

    # b) one‑hot encode remaining categoricals
    X = pd.get_dummies(X, drop_first=True)
    # ----------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test)))

    # save model
    joblib.dump(model, MODEL_DIR / "logreg.pkl")

    # ROC curve
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.savefig(FIG_DIR / "roc_curve.png")
    plt.close()

if __name__ == "__main__":
    main()
