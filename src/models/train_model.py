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

# ──────────────────────────────────────────────────────────────────────────────
PROCESSED = Path(__file__).resolve().parents[2] / "data" / "processed" / "noshow_clean.csv"
MODEL_DIR = Path(__file__).parents[2] / "models"
FIG_DIR   = Path(__file__).parents[2] / "reports" / "figures"
MODEL_DIR.mkdir(exist_ok=True, parents=True)
FIG_DIR.mkdir(exist_ok=True, parents=True)
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    # 1️⃣ Load cleaned data
    df = pd.read_csv(PROCESSED)

    # 2️⃣ Build target vector y
    if df["No-show"].dtype == object:
        # strings “Yes”/“No” — keep only those and map to 1/0
        df = df[df["No-show"].isin(["Yes", "No"])]
        y = df["No-show"].map({"Yes": 1, "No": 0}).astype(int)
    else:
        # already numeric 0/1
        y = df["No-show"].astype(int)

    # 3️⃣ Build feature matrix X
    X = df.drop(columns=["No-show"]).copy()
    # convert datetimes to epoch seconds
    for col in ["ScheduledDay", "AppointmentDay"]:
        X[col] = pd.to_datetime(X[col]).astype("int64") // 10**9
    # one‑hot encode categoricals
    X = pd.get_dummies(X, drop_first=True)

    # 4️⃣ Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5️⃣ Train
    model = LogisticRegression(max_iter=1000, class_weight="balanced")

    model.fit(X_train, y_train)

    # 6️⃣ Evaluate
    print(classification_report(y_test, model.predict(X_test)))

    # 7️⃣ Save artifacts
    joblib.dump(model, MODEL_DIR / "logreg.pkl")
    RocCurveDisplay.from_estimator(model, X_test, y_test)
    plt.savefig(FIG_DIR / "roc_curve.png")
    plt.close()

if __name__ == "__main__":
    main()

