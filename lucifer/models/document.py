# Classes
class SubDocument:
    # Attributes
    _id: str

    # Methods
    def __init__(self, data: dict):
        self._id = data['_id']

    def __repr__(self):
        return f'<{self.__class__.__qualname__}: {self._id}>'

    def __eq__(self, other):
        if isinstance(other, SubDocument):
            return self._id == other._id

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # Properties
    @property
    def id(self):
        return self._id


class Document(SubDocument):
    # Attributes
    _v: int

    # Methods
    def __init__(self, data: dict):
        super(Document, self).__init__(data)
        self._v = data['__v']

    def __eq__(self, other):
        if isinstance(other, Document):
            return self._id == other._id and self._v == other._v

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # Properties
    @property
    def v(self):
        return self._v
