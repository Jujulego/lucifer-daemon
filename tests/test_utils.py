from datetime import datetime
import pytz
import unittest

from lucifer.utils.date import json2date


# Test case
class TestUtils(unittest.TestCase):
    # Test
    def test_date(self):
        date = datetime(2020, 4, 2, 20, 30, 48, 629000, pytz.utc)
        res = json2date("2020-04-02T20:30:48.629Z")

        self.assertEqual(res, date)
