# Appointment Bot

An end‑to‑end data‑science pipeline that downloads medical no‑show data, 
cleans & featurizes it, trains a logistic‑regression model to predict 
missed appointments, and produces evaluation figures.

---

## 🚀 Quickstart

### 1. Clone & activate
```bash
git clone https://github.com/25pcheeti/appointment_bot.git
cd appointment_bot
conda env create -f environment.yml   # or: python3 -m venv .venv && 
source .venv/bin/activate
pip install -r requirements.txt

### 2. Download & preprocess dat
python src/data/download_dataset.py           # pulls raw CSV from Kaggle
python -m appointment_bot.features.build_features
Processed data will land in data/processed/noshow_clean.csv

### 3. Train & evaluate
python src/models/train_model.py
Trains a logistic regression

Saves model to models/logreg.pkl

Writes ROC curve to reports/figures/roc_curve.png

### 4. Run inference
python -m appointment_bot.modeling.predict \
  --model models/logreg.pkl \
  --input data/processed/noshow_clean.csv

🛠️ Dependencies
Python >= 3.9

pandas, numpy, scikit‑learn, matplotlib, seaborn

python‑dotenv, loguru

kaggle (for data download)

joblib (model persistence)

See environment.yml or requirements.txt for pinned versions.
