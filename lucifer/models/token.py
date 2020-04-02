from datetime import datetime
from typing import List

from lucifer.utils.date import json2date

from .document import SubDocument


# Classes
class Token(SubDocument):
    # Attributes
    _from: str
    _createdAt: datetime
    _tags: List[str]

    # Methods
    def __init__(self, data: dict):
        super(Token, self).__init__(data)

        self._from = data['from']
        self._createdAt = json2date(data['createdAt'])
        self._tags = data['tags']
