from .document import Document
from .permission import PermissionsHolder
from .token import TokensHolder


# Class
class User(Document, PermissionsHolder, TokensHolder):
    # Methods
    def __init__(self, data: dict):
        super(User, self).__init__(data)
        super(User, self)._init_permissions(data)
        super(User, self)._init_tokens(data)

        # Attributes
        self.email = data['email']  # type: str
        self._lrn = data['lrn']     # type: str

    # Properties
    @property
    def lrn(self):
        return self._lrn