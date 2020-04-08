from abc import ABC
from typing import List, Optional

from .models.version import APIVersion
from .session import LuciferSession


# Classes
class BaseClient(ABC):
    # Methods
    def __init__(self, session: LuciferSession):
        self._session = session

    async def __aenter__(self):
        await self._session.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()

    # Property
    @property
    def connected(self):
        return self._session.connected


class LuciferClient(BaseClient):
    # Methods
    def __init__(self, daemon_id: str, secret: str, *, auto_logout: bool = True, tags: Optional[List[str]] = None):
        session = LuciferSession(daemon_id, secret, auto_logout=auto_logout, tags=tags)

        super(LuciferClient, self).__init__(session)

    # - api calls
    @property
    async def version(self):
        res = await self._session.get('version')
        return APIVersion(**res)
