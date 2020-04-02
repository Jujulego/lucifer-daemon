from datetime import datetime
import pytz


# Utils
def json2date(date: str) -> datetime:
    if date.endswith('Z'):
        return datetime.fromisoformat(date[:-1]).replace(tzinfo=pytz.utc)

    return datetime.fromisoformat(date)
