import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).parents[2] / "data" / "raw" / "noshow.csv"

def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load the raw CSV."""
    return pd.read_csv(path)

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Clean & engineer features."""
    df = df.copy()
    # dates
    df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"])
    df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"])
    # no‑show binary
    df["No-show"] = (df["No-show"] == "Yes").astype(int)
    # lead time
    df["lead_time_days"] = (df["AppointmentDay"] - df["ScheduledDay"]).dt.days
    # gender encode
    df["Gender"] = df["Gender"].map({"F": 0, "M": 1}).astype(int)
    # helper features
    df["appointment_day_of_week"] = df["AppointmentDay"].dt.day_name()
    df["appointment_hour"] = df["AppointmentDay"].dt.hour
    return df

if __name__ == "__main__":
    out = Path(__file__).parents[2] / "data" / "processed" / "noshow_clean.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    preprocess(load_raw()).to_csv(out, index=False)
    print(f"Saved cleaned data → {out}")
