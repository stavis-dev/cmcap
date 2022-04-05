from .public import PubMarket


def convert(amount, coin: str, convert_coin: str):
    """ Return Cryptocurrency Converter Calculator from coinmarketcap.com 
        amount: amount of coins to convert
        coin: symbol of coin ("btc", "zec", "eth", ...)
        convert_coin: coin to convert ("usd", "eur", "zec", ...)
    """
    from .map import Symbol_to_Id
    from .api import price_conversion
    from .parse import price_conversion_parse

    symbol = Symbol_to_Id()
    id: int
    convert_id: int

    id = symbol.get_coin_id_by_symbol(symbol=coin)
    convert_id = symbol.get_coin_id_by_symbol(symbol=convert_coin)
    ex = price_conversion(amount=amount, id=id, convert_id=convert_id,)
    return price_conversion_parse(ex)
