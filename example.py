# from cmcap import PubMarket
# from cmcap import api
# from cmcap import parse


# For excample:
from cmcap import convert

print(convert(amount=10, coin='etc', convert_coin='usdt'))
# 10 ETC = 454,80 USDT

# Калькулятор и конвертер криптовалют
# Cryptocurrency Converter Calculator
# https://coinmarketcap.com/converter/
# print(PubMarket().price_conversion(amount=1, convert_id=2781, id=1))

# Cryptocurrency Coin info
# example
# https://coinmarketcap.com/currencies/bitcoin/
# print(PubMarket().coin_info(id=1))

# Список валютных пар на интересующий бирже
# example
# https://coinmarketcap.com/exchanges/binance/
# print(PubMarket().exchanges_market_pairs(slug='binance'))

# Список список бирж тогующих интересующей монетой
# example
# https://coinmarketcap.com/exchanges/binance/
# print(PubMarket().coin_markets(slug='monero'))


# Через модуль api
# Price conversion
# ex = api.price_conversion(amount=2, convert_id=2781, id=1)
# am = [0.000001, 0.0001, 0.1, 4]
# for i in am:
#     ex = api.price_conversion(amount=i, convert_id=2781, id=1)
#     res = parse.price_conversion_parse(ex)
#     print(res)


# from cmcap.map import Symbol_to_Id

# symbol = Symbol_to_Id()
# print(symbol.get_coin_id_by_symbol(symbol="usd"))


