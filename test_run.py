import unittest
from unittest.mock import patch
from cmcap import api

# from tests.test_save_test_data import TestMakeLocalJsonData
# from tests.test_api import TestPriceConversion
from tests.test_parse_round import TestParseRound
# from tests.test_parse import TestParseConverter_mock


# TestMakeLocalJsonData()

# TestPriceConversion()
TestParseRound()
# TestParseConverter_mock()


@unittest.skip("skipping mock connect test")
class TestApiwithMock(unittest.TestCase):

    @patch.object(api, '_request')
    def test_test_map_all_mock(self, request_mock):
        request_mock.return_value = 'good'

        amount = 1
        id: int = 1  # BTC
        convert_id: int = 2781  # USD

        result = api.price_conversion(amount, id, convert_id)

        print(f"\n {'-' * 20} \n result = {result}")


if __name__ == "__main__":
    unittest.main()
