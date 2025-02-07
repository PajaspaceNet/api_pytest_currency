import requests

class CurrencyConverter:
    def __init__(self, base_currency="EUR"):
        self.base_currency = base_currency
        self.rates = self.get_exchange_rates()

    def get_exchange_rates(self):
        """Získá směnné kurzy z API."""
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Chyba při načítání směnných kurzů!")
        return response.json()["rates"]

    def convert(self, amount, from_currency, to_currency):
        """Převádí částku mezi měnami."""
        if from_currency != self.base_currency:
            amount = amount / self.rates[from_currency]
        return round(amount * self.rates[to_currency], 2)

# 🟢 Příklad použití
if __name__ == "__main__":
    converter = CurrencyConverter()
    print("100 CZK to EUR:", converter.convert(100, "CZK", "EUR"))
    print("50 USD to GBP:", converter.convert(50, "USD", "GBP"))
