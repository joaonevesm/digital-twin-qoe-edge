import csv
import time
from datetime import datetime

import serial

from src.config.settings import RAW_TELEMETRY_FILE, SERIAL_BAUD_RATE, SERIAL_PORT, SERIAL_TIMEOUT

HEADER = ["timestamp", "tempo_s", "rssi_dbm", "heap_bytes", "voltage_v", "current_raw", "power_raw"]


def collect_from_serial(port: str = SERIAL_PORT, baud_rate: int = SERIAL_BAUD_RATE) -> None:
    RAW_TELEMETRY_FILE.parent.mkdir(parents=True, exist_ok=True)

    ser = serial.Serial(port, baud_rate, timeout=SERIAL_TIMEOUT)
    time.sleep(2)

    file_is_empty = not RAW_TELEMETRY_FILE.exists() or RAW_TELEMETRY_FILE.stat().st_size == 0

    with open(RAW_TELEMETRY_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file_is_empty:
            writer.writerow(HEADER)

        print(f"Collecting serial data from {port} at {baud_rate} bps...")

        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()

            if not line or "tempo_s" in line:
                continue

            parts = line.split(",")

            if len(parts) == 6:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, *parts])
                file.flush()
                print([timestamp, *parts])


if __name__ == "__main__":
    collect_from_serial()
