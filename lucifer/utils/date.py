from datetime import datetime
import pytz


# Utils
def json2date(date: str) -> datetime:
    if date.endswith('Z'):
        return datetime.fromisoformat(date).replace(tzinfo=pytz.utc)

    return datetime.fromisoformat(date)
