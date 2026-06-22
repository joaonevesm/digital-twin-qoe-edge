from src.core.qoe_engine import calculate_qoe_score, classify_qoe


def test_qoe_score_range():
    score = calculate_qoe_score(-70, 230000)
    assert 0 <= score <= 100


def test_qoe_classification():
    status, risk, recommendation = classify_qoe(80)
    assert status == "Healthy"
    assert risk == "Low"
    assert isinstance(recommendation, str)
