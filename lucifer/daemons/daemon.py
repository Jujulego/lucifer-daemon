from typing import Optional

from lucifer.utils.style import style

from lucifer.bases.document import Document
from lucifer.permissions.permission import PermissionsHolder
from lucifer.tokens.token import TokensHolder


# Classes
class SimpleDaemon(Document):
    # Methods
    def __init__(self, data: dict):
        super(SimpleDaemon, self).__init__(data)

        # Attributes
        self.name = data.get('name', None)  # type: Optional[str]
        self._user = data['user']           # type: str
        self._lrn = data['lrn']             # type: str

    def __repr__(self):
        return style.blue(f'<{self.__class__.__qualname__}: {self.name or self.id}>')

    # Properties
    @property
    def lrn(self):
        return self._lrn


class Daemon(SimpleDaemon, PermissionsHolder, TokensHolder):
    # Methods
    def __init__(self, data: dict):
        super(Daemon, self).__init__(data)
        super(Daemon, self)._init_permissions(data)
        super(Daemon, self)._init_tokens(data)
