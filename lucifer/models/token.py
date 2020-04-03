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


class TokenHolder:
    # Attributes
    _lastConnexion: datetime = None
    _tokens: List[Token]

    # Methods
    def __init__(self, data: dict):
        self._tokens = [Token(tk) for tk in data['tokens']]

        if 'lastConnexion' in data:
            self._lastConnexion = json2date(data['lastConnexion'])
