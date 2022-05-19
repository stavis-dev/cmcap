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
    price_rounded: str = field(init=False, repr=True)

    def __repr__(self) -> str:
        return f'{self.amount} {self.symbol} = {self.price_rounded} {self.convert_symbol}'

    def __post_init__(self):
        if self.price >= 1 and self.price < 100000:
            self.price_rounded = "{0:,}".format(round(self.price, 2)).replace(',', ' ').replace('.', ',')
        elif self.price < 1:
            self.price_rounded = "{0:,}".format(round(self.price, 6)).replace(',', ' ').replace('.', ',')
        else:
            self.price_rounded = "{0:,}".format(int(self.price)).replace(',', ' ')


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
        return Conversion(symbol=symbol, amount=amount, name=name,
                          convert_symbol=convert_symbol, price=price)
    except Exception:
        return Conversion(symbol="Response error")
