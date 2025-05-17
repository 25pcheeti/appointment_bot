# Appointment Bot Project

This repository contains a data science project designed to automate and 
optimize customer interactions and appointment scheduling, specifically 
predicting no-shows for medical appointments. The solution leverages 
predictive modeling and AI-driven approaches.

## 🚀 Quickstart

```bash
git clone https://github.com/25pcheeti/appointment_bot.git
cd appointment_bot
conda env create -f environment.yml   # Alternatively:
# python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 📥 Data Acquisition & Preprocessing

```bash
python src/data/download_dataset.py           # Fetches raw CSV from 
Kaggle
python -m appointment_bot.features.build_features
# Processed data output: data/processed/noshow_clean.csv
```

### ⚙️ Model Training & Evaluation

**Baseline Logistic Regression:**

```bash
python src/models/train_model.py
```

* Trains Logistic Regression
* Saves model: `models/logreg.pkl`
* ROC curve: `reports/figures/roc_curve.png`

**Advanced Model Tuning (Sprint 3 addition):**

```bash
python src/models/tune_models.py
```

* Optimizes and evaluates Random Forest, Logistic Regression, Gradient 
Boosting
* Saves best model: `models/rf_tuned.pkl`
* ROC curves and metrics in `reports/figures/`

### 🔮 Run Inference

```bash
python -m appointment_bot.modeling.predict \
  --model models/rf_tuned.pkl \
  --input data/processed/noshow_clean.csv
```

## 🛠️ Dependencies

* **Python:** ≥ 3.9
* **Libraries:**

  * pandas, numpy, scikit‑learn, matplotlib, seaborn
  * python‑dotenv, loguru
  * kaggle (data acquisition)
  * joblib (model persistence)

Check `environment.yml` or `requirements.txt` for exact versions.

## 📚 Project Background & Sprints

Detailed information on the problem statement, related work, 
methodologies, and the comprehensive coverage of **Sprints 1, 2, & 3** are 
documented in:

👉 [docs/00\_project\_background.md](docs/00_project_background.md)

### Sprint Overview

* **Sprint 1:** Problem framing, initial data acquisition, and scope 
definition
* **Sprint 2:** Data cleaning, visualization, initial feature engineering, 
baseline modeling
* **Sprint 3:** Enhanced feature engineering, hyperparameter tuning, 
detailed evaluation of multiple models, ethical considerations, and model 
deployment strategy

---

Feel free to reach out with questions or suggestions!

