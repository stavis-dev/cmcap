from cmcap import PubMarket

m = PubMarket()

# Калькулятор и конвертер криптовалют
# Cryptocurrency Converter Calculator
# https://coinmarketcap.com/converter/
# print(m.convert(amount=1, convert_id=2781, id=1))

# Cryptocurrency Coin info
# example
# https://coinmarketcap.com/currencies/bitcoin/
# print(m.coin_info(id=1))

# Список валютных пар на интересующий бирже
# example
# https://coinmarketcap.com/exchanges/binance/
# print(m.exchanges_market_pairs(slug='binance'))

# Список список бирж тогующих интересующей монетой
# example
# https://coinmarketcap.com/exchanges/binance/
# print(m.coin_markets(slug='monero'))
