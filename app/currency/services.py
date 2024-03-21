import requests
from decouple import config

APIKEY = config("APIKEY")


class CurrencyService:
    def currency_calculate(self, amount, quotation_from, quotation_to) -> float:
        value = (
            amount / quotation_from
        ) * quotation_to  # Realiza o calculo da conversão de acordo com as cotações das moedas escolhidas
        return "{:10.6f}".format(value)

    def currency(self, param_from, amount, to) -> float:

        response = requests.get(
            f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={APIKEY}&symbols={param_from},{to}"
        ).json()  # Transofrma em JSON a response da API CurrencyFreaks, que é responsável por resgatar as cotações atuais das moedas
        rates = response.get("rates")
        result = self.currency_calculate(
            amount, float(rates[param_from]), float(rates[to])
        )
        return float(result)

    def codes_currency(self) -> dict:
        response = requests.get(
            "https://api.currencyfreaks.com/v2.0/currency-symbols"
        ).json()  # Transofrma em JSON a response da API CurrencyFreaks, que retornará os valores das moedas suportadas
        return response["currencySymbols"]
