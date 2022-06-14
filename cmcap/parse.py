""" Parser data from json coinmarketcap """

from dataclasses import dataclass, field
from decimal import Decimal
# from cmcap import api


@dataclass
class Conversion:
    """ Parser price_conversion """
    symbol: str = "Coin symbol"
    price: int or Decimal = 0
    name: str = "Coin name"
    amount: int or Decimal = 0
    convert_symbol: str = "Convert symbol"
    price_rounded: str = "Rounded price"

    def __repr__(self) -> str:
        return f'{self.amount} {self.symbol} = {self.price_rounded} {self.convert_symbol}'


def price_conversion_parse(elem: dict) -> Conversion:
    try:
        data = elem.get('data')
        quote = data.get('quote')
        symbol = data.get('symbol')
        amount = data.get('amount')
        name = data.get('name')
        if len(quote) == 0:
            convert_symbol = "Error convert symbol"
            price = 0
        else:
            convert_symbol = quote[0].get('symbol')
            price = quote[0].get('price')
            price_rounded = price_round(price)
        return Conversion(symbol=symbol, amount=amount, name=name,
                          convert_symbol=convert_symbol, price=price,
                          price_rounded=price_rounded)
    except Exception:
        return Conversion(symbol="Response error")


def price_round(price) -> str:
    if price >= 1 and price < 100_000:
        price_rounded = f"{round(price, 2):,}".replace(',', ' ').replace('.', ',')
    elif price < 1 and price >= 0.000_001:
        price_rounded = f"{price:,.6f}".rstrip('0').replace('.', ',')
    elif price < 0.000_001:
        price_rounded = f"{price:.8f}".replace('.', ',')
    else:
        price_rounded = f"{int(price):,}".replace(',', ' ')

    return price_rounded