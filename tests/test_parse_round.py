import unittest
from cmcap import parse


class TestParseRound(unittest.TestCase):

    def test_price_rounded_gt1(self):
        test_func = parse._price_round

        self.assertEqual(test_func(1.12345678), '1,12')
        self.assertEqual(test_func(12.12345678), '12,12')
        self.assertEqual(test_func(123.12345678), '123,12')
        self.assertEqual(test_func(1234.12345678), '1 234,12')
        self.assertEqual(test_func(12345.12345678), '12 345,12')
        self.assertEqual(test_func(123456.12345678), '123 456')
        self.assertEqual(test_func(1234567.12345678), '1 234 567')

    def test_price_rounded_lt1(self):
        test_func = parse._price_round

        self.assertEqual(test_func(0.1), '0,1')
        self.assertEqual(test_func(0.01), '0,01')
        self.assertEqual(test_func(0.001), '0,001')
        self.assertEqual(test_func(0.0001), '0,0001')
        self.assertEqual(test_func(0.00001), '0,00001')
        self.assertEqual(test_func(0.000001), '0,000001')
        self.assertEqual(test_func(0.000_000_1), '0,00000010')
        self.assertEqual(test_func(0.000_000_01), '0,00000001')

    def test_price_rounded_ints(self):
        test_func = parse._price_round

        self.assertEqual(test_func(1), '1')
        self.assertEqual(test_func(12), '12')
        self.assertEqual(test_func(123), '123')
        self.assertEqual(test_func(1234), '1 234')
        self.assertEqual(test_func(12345), '12 345')


if __name__ == "__main__":
    unittest.main()
