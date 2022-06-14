# from cmcap import PubMarket



# For excample:
from cmcap import convert

print(convert(amount='1', coin='btc', convert_coin='usdt'))
# 10 ETC = 454,80 USDT

# Get maps from coinmarcetcup
# from cmcap import get_maps
# excange, crypto, fiat = get_maps()

# print(excange[0])
# print(crypto[0])
# print(fiat[0])

# Калькулятор и конвертер криптовалют
# Cryptocurrency Converter Calculator
# https://coinmarketcap.com/converter/
# from cmcap import api
# print(api.price_conversion(amount=1, convert_id=2781, id=1))

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
# from cmcap import api
# from cmcap import parse

# Price conversion
# ex = api.price_conversion(amount=1, convert_id=1111111111, id=1)
# res = parse.price_conversion_parse(ex)
# print(ex)
# print(res)
# am = [0.000001, 0.0001, 0.1, 4]
# for i in am:
#     ex = api.price_conversion(amount=i, convert_id=2781, id=1)
#     res = parse.price_conversion_parse(ex)
#     print(res)



# symbol to id
# from cmcap.map import Symbol_to_Id

# symbol = Symbol_to_Id()
# print(symbol.get_coin_id_by_symbol(symbol="u2sd"))


