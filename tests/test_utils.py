from datetime import datetime
import pytz

from lucifer.utils.date import json2date


# Tests
def test_utils_date():
    date = datetime(2020, 4, 2, 20, 30, 48, 629000, pytz.utc)
    res = json2date("2020-04-02T20:30:48.629Z")

    assert res == date
