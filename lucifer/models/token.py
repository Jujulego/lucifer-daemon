from datetime import datetime
from typing import List

from lucifer.utils.date import json2date

from .document import SubDocument


# Classes
class Token(SubDocument):
    # Attributes
    _from: str
    _created_at: datetime
    tags: List[str]

    # Methods
    def __init__(self, data: dict):
        super(Token, self).__init__(data)

        self._from = data['from']
        self._created_at = json2date(data['createdAt'])
        self.tags = data['tags']

    # Properties
    @property
    def from_(self) -> str:
        return self._from

    @property
    def created_at(self) -> datetime:
        return self._created_at


class TokenHolder:
    # Attributes
    _last_connexion: datetime = None
    _tokens: List[Token]

    # Methods
    def __init__(self, data: dict):
        self._tokens = [Token(tk) for tk in data['tokens']]

        if 'lastConnexion' in data:
            self._last_connexion = json2date(data['lastConnexion'])

    # Properties
    @property
    def last_connexion(self) -> datetime:
        return self._last_connexion
