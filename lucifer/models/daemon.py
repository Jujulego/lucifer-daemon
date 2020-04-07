from typing import Optional

from lucifer.utils.style import style

from .document import Document
from .permission import PermissionsHolder
from .token import TokensHolder


# Class
class Daemon(Document, PermissionsHolder, TokensHolder):
    # Methods
    def __init__(self, data: dict):
        super(Daemon, self).__init__(data)
        super(Daemon, self)._init_permissions(data)
        super(Daemon, self)._init_tokens(data)

        # Attributes
        self.name = data.get('name', None)  # type: Optional[str]
        self._user = data['user']           # type: str
        self._lrn = data['lrn']             # type: str

    def __repr__(self):
        return style.blue(f'<Daemon: {self.name or self.id}>')

    # Properties
    @property
    def lrn(self):
        return self._lrn
