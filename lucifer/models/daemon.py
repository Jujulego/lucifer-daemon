from .document import Document
from .permission import PermissionsHolder
from .token import TokensHolder


# Class
class Daemon(Document, PermissionsHolder, TokensHolder):
    # Attributes
    name: str
    user: str
    _lrn: str

    # Methods
    def __init__(self, data: dict):
        super(Daemon, self).__init__(data)
        super(Daemon, self)._init_permissions(data)
        super(Daemon, self)._init_tokens(data)

        self.name = data.get('name', None)
        self._user = data['user']
        self._lrn = data['lrn']

    # Properties
    @property
    def lrn(self):
        return self._lrn
