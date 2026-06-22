def normalize_rssi(rssi_dbm: float) -> float:
    """Normalize RSSI from [-90, -50] dBm to [0, 100]."""
    score = (rssi_dbm + 90) / 40 * 100
    return max(0, min(100, score))


def normalize_heap(heap_bytes: float, min_heap: float = 200_000, max_heap: float = 260_000) -> float:
    score = (heap_bytes - min_heap) / (max_heap - min_heap) * 100
    return max(0, min(100, score))


def calculate_qoe_score(rssi_dbm: float, heap_bytes: float) -> float:
    """Simple QoE score combining network and device conditions."""
    network_score = normalize_rssi(rssi_dbm)
    compute_score = normalize_heap(heap_bytes)
    qoe = 0.7 * network_score + 0.3 * compute_score
    return round(qoe, 2)


def classify_qoe(qoe_score: float) -> tuple[str, str, str]:
    if qoe_score >= 75:
        return "Healthy", "Low", "Maintain current operation"
    if qoe_score >= 50:
        return "Attention", "Moderate", "Monitor connection and reduce sending frequency"
    return "Critical", "High", "Reduce load, change network/cell, or migrate processing"
