"""Évaluation du risque de crédit."""

HIGH_RISK_RATIO = 0.6
MEDIUM_RISK_RATIO = 0.3


def calculate_risk(income, debt):
    """Retourne le niveau de risque ("HIGH", "MEDIUM", "LOW") ou -1 si le revenu est invalide."""
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > HIGH_RISK_RATIO:
        return "HIGH"
    if ratio > MEDIUM_RISK_RATIO:
        return "MEDIUM"
    return "LOW"