import unittest
from unittest.mock import patch, MagicMock
from cmcap import api


# @unittest.skip("skipping real connect test")
class TestPriceConversion(unittest.TestCase):

    # @unittest.skip("skipping price_conversion")
    def test_price_conversion_ok(self):
        amount = 1
        id: int = 1  # BTC
        convert_id: int = 825  # USDT

        expected_symbol = "BTC"
        expected_convert_symbol = "USDT"
        expected_cerror_code = "0"

        result = api.price_conversion(amount, id, convert_id)
        # print(f"\n {'-' * 20} \n result = {result}")

        self.assertEqual(expected_cerror_code, result["status"]["error_code"])
        self.assertEqual(expected_symbol, result["data"]["symbol"])
        self.assertEqual(expected_convert_symbol, result["data"]["quote"][0]["symbol"])

    # @unittest.skip("skipping price_conversion")
    def test_price_conversion_wrong_id(self):
        amount = 1
        id: int = 99999  # BTC
        convert_id: int = 2781  # USD
        expected_cerror_code = "500"

        result = api.price_conversion(amount, id, convert_id)
        self.assertEqual(expected_cerror_code, result["status"]["error_code"])

    # @unittest.skip("skipping price_conversion wrong_convert_id")
    def test_price_conversion_wrong_convert_id(self):
        amount = 1
        id: int = 1  # BTC
        convert_id: int = 99999  # USD

        expected_cerror_code = "0"
        expected_len_quote_list = 0

        result = api.price_conversion(amount, id, convert_id)
        len_qute_list = len(result["data"]["quote"])
        # print(f"\n {'-' * 20} \n result = {result}")
        # print(f'Len quote list = { len_qute_list }')

        self.assertEqual(expected_cerror_code, result["status"]["error_code"])
        self.assertEqual(expected_len_quote_list, len_qute_list)

    # @unittest.skip("skipping wrong_amount price_conversion ")
    def test_price_conversion_wrong_amount(self):
        amount = -1
        id = 1  # BTC
        convert_id: int = 2781  # USD

        expected_cerror_code = "500"

        result = api.price_conversion(amount, id, convert_id)
        # print(f"\n {'-' * 20} \n result = {result}")

        self.assertEqual(expected_cerror_code, result["status"]["error_code"])


if __name__ == "__main__":
    unittest.main()