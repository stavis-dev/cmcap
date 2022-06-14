import unittest
from unittest.mock import patch
from cmcap import api


# @unittest.skip("skipping test map_all")
class TestMapAll(unittest.TestCase):

    # @patch('cmcap.urllib')
    def test_map_all_with_real_connect(self):
        result = api.Api3.map_all()

        self.assertEqual(type(result), dict)
        self.assertEqual("0", result["status"]["error_code"])
        # check tables of excanges
        self.assertEqual(type(result["data"]["exchangeMap"]), list)
        # check tables of crypto Currency
        self.assertEqual(type(result["data"]["cryptoCurrencyMap"]), list)


if __name__ == "__main__":
    unittest.main()
