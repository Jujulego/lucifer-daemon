import enum
from typing import List

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
    # Attributes
    name: str
    level: PLvl

    # Methods
    def __init__(self, data: dict):
        super(Permission, self).__init__(data)

        self.name = data['name']
        self.level = PLvl(data['level'])


class PermissionsHolder:
    # Attributes
    admin: bool
    permissions: List[Permission]

    # Methods
    def _init_permissions(self, data: dict):
        self.admin = data['admin']
        self.permissions = [Permission(perm) for perm in data['permissions']]
