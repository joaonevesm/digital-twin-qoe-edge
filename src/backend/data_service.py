from __future__ import annotations

from datetime import datetime, timedelta
import random
from pathlib import Path

import pandas as pd

from src.config.settings import RAW_TELEMETRY_FILE
from src.core.digital_twin import evaluate_state

COLUMNS = ["timestamp", "rssi_dbm", "heap_bytes", "uptime_s", "voltage_v", "current_raw", "power_raw"]


def generate_simulated_data(samples: int = 60) -> pd.DataFrame:
    now = datetime.now()
    rows = []
    for i in range(samples):
        rssi = random.randint(-90, -50)
        heap = random.randint(220_000, 245_000)
        uptime = i * 5
        voltage = round(random.uniform(3.1, 3.4), 2)
        current = random.randint(100, 400)
        power = random.randint(300, 1200)
        state = evaluate_state(rssi, heap)
        rows.append({
            "timestamp": (now - timedelta(seconds=(samples - i) * 5)).strftime("%Y-%m-%d %H:%M:%S"),
            "rssi_dbm": rssi,
            "heap_bytes": heap,
            "uptime_s": uptime,
            "voltage_v": voltage,
            "current_raw": current,
            "power_raw": power,
            **state,
        })
    return pd.DataFrame(rows)


def read_telemetry(path: Path = RAW_TELEMETRY_FILE) -> pd.DataFrame:
    if path.exists() and path.stat().st_size > 0:
        df = pd.read_csv(path)
        if "timestamp" not in df.columns:
            df.insert(0, "timestamp", pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))
        if "qoe_score" not in df.columns:
            states = df.apply(lambda row: evaluate_state(float(row["rssi_dbm"]), float(row["heap_bytes"])), axis=1)
            state_df = pd.DataFrame(list(states))
            df = pd.concat([df.reset_index(drop=True), state_df], axis=1)
        return df
    return generate_simulated_data()


def get_latest_sample() -> dict:
    df = read_telemetry()
    return df.iloc[-1].to_dict()
