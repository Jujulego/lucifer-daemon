import enum

from .document import SubDocument


# Enumerations
@enum.unique
class PLvl(enum.IntFlag):
    NONE   = 0b0000
    CREATE = 0b1000
    READ   = 0b0100
    UPDATE = 0b0010
    DELETE = 0b0001

    ALL = CREATE | READ | UPDATE | DELETE


# Classes
class Permission(SubDocument):
    # Methods
    def __init__(self, data: dict):
        super(Permission, self).__init__(data)

        # Attributes
        self.name = data['name']  # type: str
        self.level = PLvl(data['level'])


class PermissionsHolder:
    # Methods
    def _init_permissions(self, data: dict):
        self.admin = data['admin']  # type: bool
        self.permissions = [Permission(perm) for perm in data['permissions']]
