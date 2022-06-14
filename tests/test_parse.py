import unittest
from unittest.mock import patch
import json

from cmcap.parse import price_conversion_parse, Conversion

class TestParseConverter_mock(unittest.TestCase):

    def test_price_conversion_parse(self):
        with open('test_data/price_conversion.json', "r") as file:
            cmcap_response = json.load(file)

        # print(f"\n {'-' * 20} \n result = {cmcap_response}")

        result = price_conversion_parse(cmcap_response)

        print(f"\n {'-' * 20} \n {result}")



if __name__ == "__main__":
    unittest.main()

