import unittest
from unittest.mock import patch, mock_open
from cmcap import api
import json


# @unittest.skip("skipping macking local data")
class TestMakeLocalJsonData(unittest.TestCase):

    @unittest.skip("skipping price_conversion")
    def test_save_price_conversion(self):
        amount = 1
        id: int = 1  # BTC
        convert_id: int = 825  # USDT

        params: dict = {"amount": amount,
                        "id": id,
                        "convert_id": convert_id}
        result = api._get_request('/tools/price-conversion',
                                  params)

        with open('test_data/price_conversion.json', 'wb') as file:
            file.write(result)

        with open('test_data/price_conversion.json', 'rb') as file:
            read = file.read()

        # print(f"\n {'-' * 20} \n result = {result}")

        self.assertEqual(read, result)


    @unittest.skip("skipping map_all.json")
    def test_save_map_all(self):
        result = api._get_request('/map/all', None)
        with open('test_data/map_all.json', 'wb') as file:
            file.write(result)

        with open('test_data/map_all.json', 'rb') as file:
            read = file.read()

        # print(f"\n {'-' * 20} \n result = {result}")

        self.assertEqual(read, result)


if __name__ == "__main__":
    unittest.main()