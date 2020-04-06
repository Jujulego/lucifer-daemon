from .document import Document
from .permission import PermissionsHolder
from .token import TokensHolder


# Class
class User(Document, PermissionsHolder, TokensHolder):
    # Attributes
    email: str
    _lrn: str

    # Methods
    def __init__(self, data: dict):
        super(User, self).__init__(data)
        super(User, self)._init_permissions(data)
        super(User, self)._init_tokens(data)

        self.email = data['email']
        self._lrn = data['lrn']

    # Properties
    @property
    def lrn(self):
        return self._lrn
