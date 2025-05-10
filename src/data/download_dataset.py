"""
Download the Medical Appointment No‑Shows dataset from Kaggle.

Requires: kaggle API key in ~/.kaggle/kaggle.json
Usage:
    python src/data/download_dataset.py
"""
from pathlib import Path
import subprocess

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

def main() -> None:
    cmd = [
        "kaggle",
        "datasets",
        "download",
        "-d", "joniarroba/noshowappointments",
        "-p", str(RAW_DIR),
        "--unzip",
    ]
    subprocess.check_call(cmd)
    print("Dataset downloaded to", RAW_DIR)

if __name__ == "__main__":
    main()
