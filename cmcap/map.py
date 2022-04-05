""" Модуль работы c ID криптовалюты 
    Хз его следует вызывать или однократно во время запуска приложения
    либо делать как положено в sql. 
    Оставил файлы, так как они проще всего для нативного просмотра.
"""

import json
from os.path import dirname, abspath
from os.path import exists, join
from dataclasses import dataclass


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