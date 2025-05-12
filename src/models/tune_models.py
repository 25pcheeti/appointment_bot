# src/models/tune_models.py
"""
Tune several classifiers (RandomForest, LogisticRegression, 
GradientBoosting)
on the no‑show data.
Outputs:
  - tuned models saved under models/
  - ROC figures under reports/figures/
  - printed classification reports to console
"""
from pathlib import Path
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, RocCurveDisplay
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────────────────────────
# Paths
PROCESSED = (
    Path(__file__).resolve().parents[2]
    / "data" / "processed" / "noshow_clean.csv"
)
MODEL_DIR = Path(__file__).parents[2] / "models"
FIG_DIR   = Path(__file__).parents[2] / "reports" / "figures"
MODEL_DIR.mkdir(exist_ok=True, parents=True)
FIG_DIR.mkdir(exist_ok=True, parents=True)
# ──────────────────────────────────────────────────────────────────────────────

def main():
    # 1) Load cleaned data
    df = pd.read_csv(PROCESSED)

    # 2) Prepare target
    if df["No-show"].dtype == object:
        df = df[df["No-show"].isin(["Yes", "No"])]
        y = df["No-show"].map({"Yes": 1, "No": 0}).astype(int)
    else:
        y = df["No-show"].astype(int)

    # 3) Build feature matrix
    X = df.drop(columns=["No-show"]).copy()
    # convert datetimes to epoch seconds
    for col in ["ScheduledDay", "AppointmentDay"]:
        X[col] = pd.to_datetime(X[col]).astype("int64") // 10**9
    # drop identifiers
    X = X.drop(columns=["PatientId", "AppointmentID"], errors="ignore")
    # one-hot encode categoricals
    X = pd.get_dummies(X, drop_first=True)

    # 4) Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ──────────────────────────────────────────────────────────────────────────
    # 5) Random Forest tuning
    rf = RandomForestClassifier(random_state=42)
    rf_params = {
        "n_estimators": [100, 200],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5],
    }
    rf_gs = GridSearchCV(rf, rf_params, cv=5, scoring="f1", n_jobs=-1, verbose=2)
    rf_gs.fit(X_train, y_train)

    print("\n=== Random Forest ===")
    print("Best params:", rf_gs.best_params_)
    print(classification_report(y_test, rf_gs.predict(X_test)))
    joblib.dump(rf_gs.best_estimator_, MODEL_DIR / "rf_tuned.pkl")
    RocCurveDisplay.from_estimator(rf_gs, X_test, y_test)
    plt.savefig(FIG_DIR / "rf_roc_curve.png")
    plt.close()

    # ──────────────────────────────────────────────────────────────────────────
    # 6) Logistic Regression tuning
    lr = LogisticRegression(max_iter=1000, solver="liblinear")
    lr_params = {
        "C": [0.01, 0.1, 1, 10],
        "class_weight": [None, "balanced"],
        "penalty": ["l1", "l2"],
    }
    lr_gs = GridSearchCV(lr, lr_params, cv=5, scoring="f1", n_jobs=-1, verbose=2)
    lr_gs.fit(X_train, y_train)

    print("\n=== Logistic Regression ===")
    print("Best params:", lr_gs.best_params_)
    print(classification_report(y_test, lr_gs.predict(X_test)))
    joblib.dump(lr_gs.best_estimator_, MODEL_DIR / "lr_tuned.pkl")
    RocCurveDisplay.from_estimator(lr_gs, X_test, y_test)
    plt.savefig(FIG_DIR / "lr_roc_curve.png")
    plt.close()

    # ──────────────────────────────────────────────────────────────────────────
    # 7) Gradient Boosting tuning
    gb = GradientBoostingClassifier(random_state=42)
    gb_params = {
        "n_estimators": [100, 200],
        "learning_rate": [0.01, 0.1],
        "max_depth": [3, 5, 7],
    }
    gb_gs = GridSearchCV(gb, gb_params, cv=5, scoring="f1", n_jobs=-1, verbose=2)
    gb_gs.fit(X_train, y_train)

    print("\n=== Gradient Boosting ===")
    print("Best params:", gb_gs.best_params_)
    print(classification_report(y_test, gb_gs.predict(X_test)))
    joblib.dump(gb_gs.best_estimator_, MODEL_DIR / "gb_tuned.pkl")
    RocCurveDisplay.from_estimator(gb_gs, X_test, y_test)
    plt.savefig(FIG_DIR / "gb_roc_curve.png")
    plt.close()
    # ──────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()

