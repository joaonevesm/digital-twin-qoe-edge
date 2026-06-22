from src.core.qoe_engine import calculate_qoe_score, classify_qoe


def evaluate_state(rssi_dbm: float, heap_bytes: float) -> dict:
    qoe_score = calculate_qoe_score(rssi_dbm, heap_bytes)
    status, risk_level, recommendation = classify_qoe(qoe_score)
    return {
        "qoe_score": qoe_score,
        "status": status,
        "risk_level": risk_level,
        "recommendation": recommendation,
    }
