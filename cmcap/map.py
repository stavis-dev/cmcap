""" Модуль работы c ID криптовалюты 
    Хз его следует вызывать или однократно во время запуска приложения
    либо делать как положено в sql. 
    Оставил файлы, так как они проще всего для нативного просмотра.
"""

import json
from os.path import dirname, abspath
from os.path import exists, join
from dataclasses import dataclass


import re
import json
from urllib.request import urlopen
from typing import List, Dict, Tuple


def _get_js_file(url_js_file: str):
    try:
        with urlopen(url_js_file, timeout=10) as rsp:
          return rsp.read().decode("utf-8")
    except Exception as err:
        print(err)
        raise Exception("!!!!! Some error !!!")


def get_map_fiat(js: str) -> List[dict]:
    """ спарсил файл
        https://files.coinmarketcap.com/static/widget/currency.js
        return list of dicts like:
          {id:2781,name:"United States Dollar",symbol:"usd",token:"$"}
    """
    def add_quotes(match_obj) -> str:
        if match_obj.group():
            repl = f'"{match_obj.group()}"'
            return repl

    pattern_fiat_in_js = r"(?<=\({1:function\(e,a,n\)).*?a\.a=(?P<fiat>.*?\}\})(?=\},)"
    result = re.search(pattern_fiat_in_js, js)
    if result:
        raw_fiat = result.group('fiat')
    else:
        raise Exception("Not found fiat in js file") 

    res_str = re.sub(r"(\w*)(?=\:)", add_quotes, raw_fiat).replace("so'm", "som")
    return json.loads(res_str)


def parse_crypto_exchanges_map(data) -> Tuple[ List[dict], List[dict] ]:
    """ Получает 2 dicts с кодами криптовалют с сайта
        https://api.coinmarketcap.com/data-api/v3/map/all
        return tuple with 2 lists in it
            exchange_map: dict like
              {"id":16,"name":"Poloniex","slug":"poloniex","is_active":1,"status":"active","first_historical_data":"2018-04-26T00:45:00.000Z","last_historical_data":"2022-05-01T17:15:12.000Z"}
            crypto_currency_map: dict like
              {"id":1027,"name":"Ethereum","symbol":"ETH","slug":"ethereum","token_address":"0x6c862f803fF42A97D4A483AB761256ad8c90f4F8"},"rank":8347}
        ...
    """
    return (data.get('data').get('exchangeMap'),
            data.get('data').get('cryptoCurrencyMap'))



def parse_map_currencies_exchanges(data: dict):
    """ Получает dict с кодами криптовалют с сайта
        https://api.coinmarketcap.com/data-api/v3/map/all
        return tuple with 2 dicts in it
            crypto_map_sort: dict like
              {'btc': {'id': 1, 'name': 'Bitcoin', 'slug': 'bitcoin', 'symbol': 'BTC'}} 
        ...
    """
    cryptoCurrencies = data.get('data').get('cryptoCurrencyMap')
    exchanges = data.get('data').get('exchangeMap')

    crypto_map = {}
    for i in cryptoCurrencies:
      if i.get('is_active'):
        low_symb = i.get('symbol').lower()
        crypto_map.update({f'{low_symb}':{
            'name': i.get('name'),
            'id': i.get('id'),
            'symbol': i.get('symbol'),
            'slug': i.get('slug'),
        }})
    crypto_map_sort = {key: val for key, val in sorted(crypto_map.items(), key = lambda ele: ele[0])}

    exchanges_map = {}
    for i in exchanges:
      if i.get('is_active'):
        low_symb = i.get('slug').lower()
        exchanges_map.update({f'{low_symb}':{
            'name': i.get('name'),
            'id': i.get('id'),
            'slug': i.get('slug'),
        }})
    exchanges_map_sort = {key: val for key, val in sorted(exchanges_map.items(), key = lambda ele: ele[0])}
    return crypto_map_sort, exchanges_map_sort



class Symbol_to_Id():
    """ Convert Symbol to ID from data/*.json files """
    # fiat: dict 
    # exchange_map: dict
    # cryptocurrency_map: dict

    def __init__(self) -> None:
        self.get_datas_from_jsons()

    def get_datas_from_jsons(self):
        self.__cryptocurrency_map: dict = {}
        self.__exchange_map: dict = {}
        self.__fiat: dict = {}
        """ load IDs from json files """
        cur_dir = dirname(abspath(__file__))
        maps = {
            'cmcap_cryptocurrency_map_mini.json': self.__cryptocurrency_map,
            'cmcap_exchange_map_mini.json': self.__exchange_map,
            'cmcap_fiat_mini.json': self.__fiat
        }
        for file, var in maps.items():
            json_path = join(cur_dir, 'maps', file)
            # logging.debug(f'Текущий путь к файлу: {json_path}')
            try:
                with open(json_path, 'r') as f:
                    # var = json.load(f)
                    var.update(json.load(f))
                    # print(self.__fiat)
            except Exception as err:
                raise Exception(err)

    def get_exchange_id_by_slug(self, slug: str) -> int:
        """ Return id exchnge by it slug name
            Arguments:
                slug: str - slug name of exchange
            Example:
                slug='binance' -> 270
                slug='exmo' -> 844
                slug='nice-hash' -> 50
        """
        return self.__exchange_map.get(slug.lower(), None)

    def get_coin_id_by_symbol(self, symbol):
        """ Возвращает id актива по его символу symbol
            Для него необходимы переменные CRYPTO, FIAT
        """
        # print(symbol)
        for i in (self.__cryptocurrency_map,
                  self.__fiat):
            # print(i)
            id = i.get(symbol.upper(), None)
            if id:
                return id
        if id is None:
            return -1
    
    @property
    def fiat(self, symbol: str = None):
        """ Return dict fiat when key is symbol ad value is ID """
        if symbol:
            return self.get_coin_id_by_symbol(symbol=symbol)
        return self.__fiat

    @property
    def exchanges(self):
        return self.__exchange_map

    @property
    def crypto(self):
        return self.__exchange_map