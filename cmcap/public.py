#!/usr/bin/env python
# import os
import json
from urllib.request import urlopen
from urllib import parse
from decimal import Decimal


class PubMarket:
    """Public api for web v3 """
    __BASE_API_URL = 'https://api.coinmarketcap.com/data-api/v3'

    def __init__(self,
                 base_url=__BASE_API_URL, verbose=False):
        self.base_url = base_url
        self.verbose = verbose

    @classmethod
    def __request(cls, endpoint: str, params: dict = None):
        if params:
            params = parse.urlencode(params)
            req = cls.__BASE_API_URL + endpoint + '?' + params
        else:
            req = cls.__BASE_API_URL + endpoint

        try:
            with urlopen(req, timeout=10) as rsp:
                response = json.loads(rsp.read(), parse_float=Decimal)
        except Exception as err:
            return err
        if response['status']['error_code'] == '0':
            return response['data']
        else:
            return response['status']

    def listing(self, **kwargs):
        """
        https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing
        /info
        https://coinmarketcap.com/
        """
        params: dict = {}
        params.update(kwargs)
        response = self.__request('/cryptocurrency/listing', params=None)
        return response

    @classmethod
    def markets_by_coin_id(cls, id: int = None,
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
        response = cls.__request('/cryptocurrency/market-pairs/latest',
                                  params)
        return response

    def markets_info(self, slug: str, **kwargs):
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
        """
        # if value:
        #     value = '?' + str(value)
        params = {
            'slug': slug
            }
        params.update(kwargs)
        response = self.__request('/exchange/market-pairs/latest',
                                  params)
        return response

    def price_conversion(self, amount, id: int, convert_id: int):
        """
        Cryptocurrency Converter Calculator
        https://coinmarketcap.com/converter/
        Requared: "slug" or "id"
        amount=1,
        convert_id=2781,
        id=1
        """
        params: dict = {"amount": amount,
                        "id": id,
                        "convert_id": convert_id}
        resp = self.__request('/tools/price-conversion',
                              params)
        return resp

    def coin_info(self, id: int):
        """
        Cryptocurrencies Coins Info
        https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
        Requared: "id"
        Example:
        id=1
        """
        params: dict = {"id": id}
        resp = self.__request('/cryptocurrency/detail',
                              params)
        return resp
