from appointment_bot.features.build_features import load_raw, preprocess

def test_preprocess_adds_expected_columns():
    df = preprocess(load_raw())
    assert {"lead_time_days", "appointment_day_of_week", "appointment_hour"}.issubset(df.columns)
