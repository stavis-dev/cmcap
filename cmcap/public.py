#!/usr/bin/env python
import os
import json
import tempfile
from requests_cache import CachedSession  # pip install requests-cache
# https://github.com/reclosedev/requests-cache


class PubMarket:
    _session = None
    __DEFAULT_BASE_URL = 'https://api.coinmarketcap.com/data-api/v3'
    __DEFAULT_TIMEOUT = 30
    __TEMPDIR_CACHE = True

    def __init__(self,
                 base_url=__DEFAULT_BASE_URL,
                 request_timeout=__DEFAULT_TIMEOUT,
                 tempdir_cache=__TEMPDIR_CACHE):
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.cache_filename = 'coinmarketcap_cache'
        if tempdir_cache:
            self.cache_name = os.path.join(tempfile.gettempdir(),
                                           self.cache_filename)
        else:
            self.cache_name = self.cache_filename

    @property
    def session(self) -> CachedSession:
        if not self._session:
            self._session = CachedSession(cache_name=self.cache_name,
                                          backend='sqlite',
                                          expire_after=120)
            self._session.headers.update({'Accept': 'application/json'})
            self._session.headers.update({'Accept-Encoding': 'deflate, gzip'})
            self._session.headers.update({'User-agent': 'coinmarketcap - python \
                                          wrapper apiv3 coinmarketcap.'})
        return self._session

    def __request(self, endpoint: str, params: dict):
        # print('url is', self.base_url + endpoint, params)
        # exit()
        rsp_object = self.session.get(self.base_url + endpoint,
                                      params=params,
                                      timeout=self.request_timeout)
        try:
            response = json.loads(rsp_object.text)
            if isinstance(response, list) and rsp_object.status_code == 200:
                response = [dict(item, **{u'cached': rsp_object.from_cache})
                            for item in response]
            if isinstance(response, dict) and rsp_object.status_code == 200:
                response[u'cached'] = rsp_object.from_cache
        except Exception as err:
            return err
        return response

    def listing(self, **kwargs):
        """
        https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing
        /info
        https://coinmarketcap.com/
        """
        params: dict = {}
        params.update(kwargs)
        response = self.__request('/cryptocurrency/listing', params)
        return response

    def market_pairs(self, **kwargs):
        """
        Requared "slug" or "id"
        Example:
        slug=zclassic
        id=1
        &start=1&limit=6
        """
        params: dict = {}
        params.update(kwargs)
        response = self.__request('/cryptocurrency/market-pairs/latest',
                                  params)
        return response

    def exchanges(self, slug: str, **kwargs):
        """
        https://coinmarketcap.com/ru/rankings/exchanges/
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
