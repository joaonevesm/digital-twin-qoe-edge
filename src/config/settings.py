from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_TELEMETRY_FILE = RAW_DATA_DIR / "telemetry_raw.csv"
PROCESSED_TELEMETRY_FILE = PROCESSED_DATA_DIR / "telemetry_processed.csv"

SERIAL_PORT = "COM3"
SERIAL_BAUD_RATE = 115200
SERIAL_TIMEOUT = 2

DASHBOARD_TITLE = "Digital Twin for QoE Monitoring in Edge Devices"
