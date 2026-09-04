import sys
import os
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
from ethiopian_calendar import EthiopicDate

class TestEthiopicDate(unittest.TestCase):
    
    def test_leap_year(self):
        d1 = EthiopicDate(2015, 13, 6)
        self.assertTrue(d1.is_leap_year)
        
        d2 = EthiopicDate(2014, 13, 5)
        self.assertFalse(d2.is_leap_year)

    def test_gregorian_conversion(self):
        eth_date = EthiopicDate(2015, 1, 1)
        greg_date = eth_date.to_gregorian()
        self.assertEqual(greg_date, date(2022, 9, 11))

        converted_back = EthiopicDate.from_gregorian(date(2022, 9, 11))
        self.assertEqual(converted_back.year, 2015)
        self.assertEqual(converted_back.month, 1)
        self.assertEqual(converted_back.day, 1)

if __name__ == "__main__":
    unittest.main()