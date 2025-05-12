# src/models/tune_models.py
"""
Tune several classifiers (e.g. RandomForest) on the no-show data.
Outputs:
  - tuned models saved under models/
  - figures under reports/figures/
"""
from pathlib import Path
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, RocCurveDisplay
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────────────────────────
# Paths
PROCESSED = (Path(__file__).resolve()
                 .parents[2] / "data" / "processed" / "noshow_clean.csv")
MODEL_DIR = Path(__file__).parents[2] / "models"
FIG_DIR   = Path(__file__).parents[2] / "reports" / "figures"
MODEL_DIR.mkdir(exist_ok=True, parents=True)
FIG_DIR.mkdir(exist_ok=True, parents=True)
# ──────────────────────────────────────────────────────────────────────────────

def main():
    # 1) Load cleaned data
    df = pd.read_csv(PROCESSED)

    # 2) Prepare target vector
    if df["No-show"].dtype == object:
        df = df[df["No-show"].isin(["Yes", "No"])]
        y = df["No-show"].map({"Yes": 1, "No": 0}).astype(int)
    else:
        y = df["No-show"].astype(int)

    # 3) Build features
    X = df.drop(columns=["No-show"]).copy()
    # convert datetimes to epoch seconds
    for col in ["ScheduledDay", "AppointmentDay"]:
        X[col] = pd.to_datetime(X[col]).astype("int64") // 10**9
    # drop identifier columns
    X = X.drop(columns=["PatientId", "AppointmentID"], errors="ignore")
    # one-hot encode categoricals
    X = pd.get_dummies(X, drop_first=True)

    # 4) Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5) RandomForest hyperparameter tuning
    rf = RandomForestClassifier(random_state=42)
    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5],
    }
    gs = GridSearchCV(rf, param_grid, cv=5, scoring="f1", n_jobs=-1, verbose=2)
    gs.fit(X_train, y_train)

    # 6) Evaluation & save
    print("Best RF params:", gs.best_params_)
    print(classification_report(y_test, gs.predict(X_test)))
    joblib.dump(gs.best_estimator_, MODEL_DIR / "rf_tuned.pkl")

    # 7) ROC curve
    RocCurveDisplay.from_estimator(gs, X_test, y_test)
    plt.savefig(FIG_DIR / "rf_roc_curve.png")
    plt.close()

if __name__ == "__main__":
    main()

