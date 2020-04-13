from lucifer.utils.style import style

from .document import Document
from .permission import PermissionsHolder
from .token import TokensHolder


# Classes
class SimpleUser(Document):
    # Methods
    def __init__(self, data: dict):
        super(SimpleUser, self).__init__(data)

        # Attributes
        self.email = data['email']  # type: str
        self._lrn = data['lrn']     # type: str

    def __repr__(self):
        return style.blue(f'<{self.__class__.__qualname__}: {self.email}>')

    # Properties
    @property
    def lrn(self):
        return self._lrn


class User(SimpleUser, PermissionsHolder, TokensHolder):
    # Methods
    def __init__(self, data: dict):
        super(User, self).__init__(data)
        super(User, self)._init_permissions(data)
        super(User, self)._init_tokens(data)
