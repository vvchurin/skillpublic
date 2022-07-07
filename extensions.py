import json
import requests
from config import keys, headers

class ConvertionExcepttion(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExcepttion(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExcepttion(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExcepttion(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExcepttion(f'Не удалось обработать количество {amount}.')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        total_base = json.loads(response.content)

        return total_base['result']
