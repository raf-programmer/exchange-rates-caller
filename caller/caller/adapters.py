import urllib.parse

import requests


class ExchangeRatesAdapter:
    domain = "http://exchange-rates-service:5000/"

    async def get_converted_value(self, call):
        url = f"{self.domain}exchange_rates/convert_currencies?_from={call.from_currency}&to={call.to_currency}&amount={call.amount}"
        if call.when:
            url += f"{url}&when={urllib.parse.quote(str(call.when))}"
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.json()["result"], response.status_code
        else:
            return None, response.status_code
