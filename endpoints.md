> :warning: **Disclaimer**:

 > * Before using the endpoints, please check the [API documentation](https://coinmarketcap.com/api/documentation/v1/) to be informed about the latest changes or possible bugs/problems.

 > * Not all parameters are mandatory. Some parameters are only mandatory in specific conditions/types. Check the official documentation the type of each parameter and to know if a parameter is mandatory or optional.

 > * Я нигде не смог найти мануала по apiv3, (возможно плохо искал)

## Api v3

Публичный апи через него работает браузер и мобильное приложение.

* *Базовый урл для всех разпросов*
  * **URI https://api.coinmarketcap.com/data-api/v3**

Данные с главной страницы сайта.

* *Топ-100 Криптовалюты по рыночной капитализации*
  * [URL](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing)
  * **GET /cryptocurrency/listing** (Есть необязательные доп параметры)

    ```python 
    pubmarket.listing()
    ```

* *Рынки криптоактива*
  * Возвращает список бирж где торгуется криптоактив и курсы на них.
  * Требует передачи `suug` или `id` криптовалюты. Например для BTC `slug=bitcoin`, `id=1`.
  * [URL c ID](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?id=1)
  * [URL cо slug](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bitcoin)
  * **GET /cryptocurrency/market-pairs/latest** (Есть обязательный параметр)

    ```python
    # by slug
    pubmarket.listing(slug=zclassic)
    
    # by id
    pubmarket.listing(id=1)
    ```

* *Список существующих бирж*
  * Возвращает список активных (работающих) криптовалютных бирж.
  * Требует передачи `suug` или `id` биржи. Например для Okex `slug=okex`, `id=294`.
  * [URL c ID](https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?id=294)
  * [URL cо slug](https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?slug=okex)
  * **GET /exchange/market-pairs/latest** (Есть обязательный параметр)

    ```python
    # by slug
    pubmarket.listing(slug='okex')
    
    # by id
    pubmarket.listing(id=294)
    ```

* *Список валютных пар на бирже*
  * Возвращает список валютных пар с интересующей биржи.
  * Требует передачи `suug` или `id` биржи. Например для Okex `slug=okex`, `id=294`.
  * [URL c ID](https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?id=294)
  * [URL cо slug](https://api.coinmarketcap.com/data-api/v3/exchange/market-pairs/latest?slug=okex)
  * **GET /exchange/market-pairs/latest** (Есть обязательный параметр)

    ```python
    # by slug
    pubmarket.listing(slug='okex')
    
    # by id
    pubmarket.listing(id=294)
    ```

### [Начало](https:///)

* *Wallet Endpoints*
  * **GET /sapi/v1/system/status** (Fetch system status.)

    ```python
    client.get_system_status()
    ```
