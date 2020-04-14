from datetime import datetime
import pytz

from lucifer import json2date


# Tests
def test_utc_date():
    date = datetime(2020, 4, 2, 20, 30, 48, 629000, pytz.utc)
    res = json2date("2020-04-02T20:30:48.629Z")

    assert res == date
