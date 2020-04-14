from datetime import datetime
from typing import List, Optional

from lucifer.utils.date import json2date

from lucifer.bases.document import SubDocument


# Classes
class Token(SubDocument):
    # Methods
    def __init__(self, data: dict):
        super(Token, self).__init__(data)

        # Attributes
        self._from = data['from']  # type: str
        self._created_at = json2date(data['createdAt'])
        self.tags = data['tags']   # type: List[str]

    # Properties
    @property
    def from_(self) -> str:
        return self._from

    @property
    def created_at(self) -> datetime:
        return self._created_at


class TokensHolder:
    # Attributes
    _last_connexion: Optional[datetime] = None

    # Methods
    def _init_tokens(self, data: dict):
        self._tokens = [Token(tk) for tk in data['tokens']]

        if 'lastConnexion' in data:
            self._last_connexion = json2date(data['lastConnexion'])

    # Properties
    @property
    def last_connexion(self) -> Optional[datetime]:
        return self._last_connexion
