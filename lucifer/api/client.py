from collections import namedtuple
from typing import List, Optional

from .bases.client import BaseClient
from .daemons.client import DaemonsClient
from .session import LuciferSession
from .users.client import UsersClient


# Tuple
APIVersion = namedtuple('APIVersion', ['version', 'commit'])


# Classes
class LuciferClient(BaseClient):
    # Methods
    def __init__(self, daemon_id: str, secret: str, *, auto_logout: bool = True, tags: Optional[List[str]] = None):
        session = LuciferSession(daemon_id, secret, auto_logout=auto_logout, tags=tags)

        # Attributes
        super(LuciferClient, self).__init__(session)

        self._daemons = DaemonsClient(session)
        self._users = UsersClient(session)

    # Calls
    async def version(self):
        res = await self._session.get('version')
        return APIVersion(**res)

    # Properties
    @property
    def daemons(self):
        return self._daemons

    @property
    def users(self):
        return self._users
