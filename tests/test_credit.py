from credit import calculate_risk


# ---------- Partie A : cas normaux ----------
def test_high_risk():
    assert calculate_risk(1000, 700) == "HIGH"


def test_medium_risk():
    assert calculate_risk(1000, 400) == "MEDIUM"


def test_low_risk():
    assert calculate_risk(1000, 100) == "LOW"


# ---------- Partie B : cas limites ----------
def test_zero_income():
    assert calculate_risk(0, 500) == -1


def test_negative_income():
    assert calculate_risk(-1000, 500) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0) == "LOW"


def test_ratio_exactly_0_3():
    # 0.3 n'est pas > 0.3, donc LOW
    assert calculate_risk(1000, 300) == "LOW"


def test_ratio_exactly_0_6():
    # 0.6 n'est pas > 0.6, donc MEDIUM
    assert calculate_risk(1000, 600) == "MEDIUM"