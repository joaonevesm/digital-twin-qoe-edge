from dataclasses import dataclass

@dataclass
class TelemetrySample:
    timestamp: str
    rssi_dbm: float
    heap_bytes: float
    uptime_s: float
    voltage_v: float | None = None
    current_raw: float | None = None
    power_raw: float | None = None
