import pytest
from converter import CurrencyConverter

@pytest.fixture
def converter():
    """Vytvoří instanci konvertoru s testovacími kurzy."""
    test_converter = CurrencyConverter()
    test_converter.rates = {
        "EUR": 1.0,
        "USD": 1.1,
        "CZK": 25.0,
        "GBP": 0.85
    }
    return test_converter

def test_convert_eur_to_usd(converter):
    assert converter.convert(10, "EUR", "USD") == 11.0

def test_convert_czk_to_eur(converter):
    assert converter.convert(100, "CZK", "EUR") == 4.0

def test_convert_usd_to_gbp(converter):
    assert converter.convert(50, "USD", "GBP") == 38.64  # 50/1.1 * 0.85

