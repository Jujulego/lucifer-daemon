from datetime import datetime
import pytz


# Utils
def json2date(date: str) -> datetime:
    return datetime.fromisoformat(date[:-1]).replace(tzinfo=pytz.utc)
