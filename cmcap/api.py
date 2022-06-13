""" Public web api site of coinmarketcap.com """

import json
from urllib.request import urlopen
from urllib import parse
from decimal import Decimal

__BASE_API_URL = 'https://api.coinmarketcap.com/data-api/v3'


def map_all():
    """
    возвращает json с 2 списками (list):
        exchangeMap: список с ID криптобирж
        cryptoCurrencyMap: список с ID криптовалют и их slug
    https://api.coinmarketcap.com/data-api/v3/map/all
    """
    return _request('/map/all')


def __cryptocurrency_market_pairs(id: int = None,
                        slug: str = None, **kwargs):
    """
    Возвращает список бирж торгующие интересующей монетой id
    Market Pairs Latest
    https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?id=1
    https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMarketpairsLatest
    Requared "slug" or "id"
    Example:
    slug=zclassic
    id=1
    &start=1&limit=6
    """
    if id is None and slug is None:
        raise
    elif id:
        params: dict = {
            'id': id,
        }
    elif slug:
        params: dict = {
            'slug': slug,
        }
    elif id and slug:
        raise

    params.update(kwargs)
    response = _request_data('/cryptocurrency/market-pairs/latest',
                                params)
    return response


def __exchange_market_pairs(id: int = None,
                            slug: str = None, **kwargs):
    """
    Возвращает список валютных пар на интересующей бирже id
    https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMarketpairsLatest
    Cryptocurrency Converter Calculator
    https://coinmarketcap.com/ru/rankings/exchanges/
    category=spot - Спот (по умолчанию)
    category=perpetual - Бессрочные
    category=futures - Фьючерсы
    slug=kraken&category=spot&start=1&limit=100
    Requared "slug" or "id"
    Example:
    slug=okex
    id=1
    &start=1&limit=6
    limit - 1000 max
    """
    if id is None and slug is None:
        raise
    elif id:
        params: dict = {
            'id': id,
        }
    elif slug:
        params: dict = {
            'slug': slug,
        }
    elif id and slug:
        raise
    params.update(kwargs)
    response = _request_data('/exchange/market-pairs/latest',
                                params)
    return response


def __cryptocurrency_detail(id: int):
        """
        Cryptocurrencies Coins Info
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        Requared: "id"
        Example:
        id=1
        """
        params: dict = {"id": id}
        resp = _request('/cryptocurrency/detail',
                              params)
        return resp


def __listing():
    """
    Index page of coinmarketcap
    https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing
    /info
    https://coinmarketcap.com/
    """
    return _request('/cryptocurrency/listing')


def price_conversion(amount, id: int, convert_id: int):
        """
        Cryptocurrency Converter Calculator
        https://coinmarketcap.com/converter/
        https://api.coinmarketcap.com/data-api/v3/tools/price-conversion
        Requared: "slug" or "id"
        amount=1,
        convert_id=2781,
        id=1
        https://api.coinmarketcap.com/data-api/v3/tools/price-conversion?id=1&amount=1&convert_id=2781
        """
        params: dict = {"amount": amount,
                        "id": id,
                        "convert_id": convert_id}
        resp = _request('/tools/price-conversion',
                              params)
        return resp


def _request(endpoint: str, params: dict = None):
        response = _get_request(endpoint=endpoint, params=params)
        return _json_load(response)


def _get_request(endpoint: str, params: dict):
        if params:
            params = parse.urlencode(params)
            request = __BASE_API_URL + endpoint + '?' + params
        else:
            request = __BASE_API_URL + endpoint
        try:
            with urlopen(request, timeout=10) as response:
                return response.read()
        except Exception as err:
            print(err)
            raise Exception("Error getting request")


def _json_load(response):
    return json.loads(response, parse_float=Decimal)


def _request_data(endpoint: str, params: dict = None):
    """ requests with status errros filter """
    response = _request(endpoint=endpoint, params=params)

    if response['status']['error_code'] == '0':
        return response['data']
    else:
        raise Exception(response['status'])