""" Public web api site of coinmarketcap.com """

import json
from urllib.request import urlopen
from urllib import parse
from decimal import Decimal


class Api3:
    """Public api for web v3 """
    __BASE_API_URL = 'https://api.coinmarketcap.com/data-api/v3'

    def __init__(self,
                 base_url=__BASE_API_URL, verbose=False):
        self.base_url = base_url
        self.verbose = verbose

    @classmethod
    def _request(cls, endpoint: str, params: dict = None):
        if params:
            params = parse.urlencode(params)
            req = cls.__BASE_API_URL + endpoint + '?' + params
        else:
            req = cls.__BASE_API_URL + endpoint
        try:
            with urlopen(req, timeout=10) as rsp:
                return json.loads(rsp.read(), parse_float=Decimal)
        except Exception as err:
            print(err)
            raise Exception("!!!!! Some error !!!")

    @classmethod
    def _request_data(cls, endpoint: str, params: dict = None):
        """ requests with status errros filter """
        response = cls._request(endpoint=endpoint, params=params)
        if response['status']['error_code'] == '0':
            return response['data']
        else:
            raise Exception(response['status'])

    @classmethod
    def map_all(cls, **kwargs):
        """
        возвращает json с 2 списками (list):
            exchangeMap: список с ID криптобирж
            cryptoCurrencyMap: список с ID криптовалют и их slug
        https://api.coinmarketcap.com/data-api/v3/map/all
        """
        params: dict = {}
        params.update(kwargs)
        response = cls._request('/map/all', params=None)
        return response

    @classmethod
    def cryptocurrency_market_pairs(cls, id: int = None,
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
        response = cls._request_data('/cryptocurrency/market-pairs/latest',
                                  params)
        return response

    @classmethod
    def cryptocurrency_detail(cls, id: int):
        """
        Cryptocurrencies Coins Info
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        Requared: "id"
        Example:
        id=1
        """
        params: dict = {"id": id}
        resp = cls._request('/cryptocurrency/detail',
                              params)
        return resp

    @classmethod
    def exchange_market_pairs(cls, id: int = None,
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
        response = cls._request_data('/exchange/market-pairs/latest',
                                  params)
        return response

    @classmethod
    def price_conversion(cls, amount, id: int, convert_id: int):
        """
        Cryptocurrency Converter Calculator
        https://coinmarketcap.com/converter/
        https://api.coinmarketcap.com/data-api/v3/tools/price-conversion
        Requared: "slug" or "id"
        amount=1,
        convert_id=2781,
        id=1
        """
        params: dict = {"amount": amount,
                        "id": id,
                        "convert_id": convert_id}
        resp = cls._request('/tools/price-conversion',
                              params)
        return resp


def map_all(**kwargs):
    """
    возвращает json с 2 списками (list):
        exchangeMap: список с ID криптобирж
        cryptoCurrencyMap: список с ID криптовалют и их slug
    https://api.coinmarketcap.com/data-api/v3/map/all
    """
    params: dict = {}
    params.update(kwargs)
    response = Api3()._request('/map/all', params=None)
    return response


def cryptocurrency_market_pairs(id: int = None,
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
    response = Api3()._request_data('/cryptocurrency/market-pairs/latest',
                                params)
    return response


def exchange_market_pairs(id: int = None,
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
    response = Api3()._request_data('/exchange/market-pairs/latest',
                                params)
    return response


def cryptocurrency_detail(id: int):
        """
        Cryptocurrencies Coins Info
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        Requared: "id"
        Example:
        id=1
        """
        params: dict = {"id": id}
        resp = Api3()._request('/cryptocurrency/detail',
                              params)
        return resp


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
        resp = Api3()._request('/tools/price-conversion',
                              params)
        return resp