import unittest
from unittest.mock import patch
from cmcap import api


class TestApi3(unittest.TestCase):

    # @patch('cmcap.urllib')
    def test_map_all_with_real_connect(self):
        result = api.Api3.map_all()

        self.assertEqual(type(result), dict)
        self.assertEqual("0", result["status"]["error_code"])
        self.assertEqual(type(result["data"]["exchangeMap"]), list)
        self.assertEqual(type(result["data"]["cryptoCurrencyMap"]), list)


unittest.main()