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
    pubmarket.markets_by_coin_id(slug=zclassic)
    
    # by id
    pubmarket.markets_by_coin_id(id=1)
    ```

* *Список валютных пар на бирже*
  * Возвращает валютных пар торгующихся на интересующей бирже.
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

* *Информация о криптоактиве*
  * Получает информацию об интересующем криптоактиве.
  * Требует передачи `suug` или `id` биржи. Например для Okex `slug=bitcoin`, `id=1`.
  * [URL c ID](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail?id=1)
  * [URL cо slug](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail?slug=bitcoin)
  * **GET /cryptocurrency/detail?id=1** (Есть обязательный параметр)

    ```python
    # by slug
    m.coin_info(slug='bitcoin')
    
    # by id
    m.coin_info(id=1)
    ```

## Конвертер валют

Cryptocurrency Converter Calculator  

[Web версия](https://coinmarketcap.com/converter/)

 > * Конвертирует один криптоактив в другой.

Требует обязательной передачи параметров:

`amount`: (сумма)
`id`: (id первого криптоактива)
`convert_id`: (id криптоактива в который проводится конвертация)

* *Конвертер криптоактива*
  * Конвертиртер криптовалют.
  * Требует передачи `amount` или `id` биржи. `convert_id`.
  * [URL c ID](https://api.coinmarketcap.com/data-api/v3/tools/price-conversion?amount=1&id=1&convert_id=2781)
  * **GET /tools/price-conversion** ()
  * **GET /tools/price-conversion?amount=1&id=1&convert_id=2781** ()

    ```python
    # пример конвертации btc в usd
    m.price_conversion(amount=1, id=1, convert_id=2781)
    ```
