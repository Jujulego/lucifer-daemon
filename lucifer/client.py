from abc import ABC
from typing import List, Optional

from .models.daemon import Daemon, SimpleDaemon
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


class DaemonClient(BaseClient):
    # Methods
    async def all(self) -> List[SimpleDaemon]:
        res = await self._session.get(f'daemons')
        return [SimpleDaemon(r) for r in res]

    async def create(self, name: Optional[str] = None) -> Daemon:
        daemon = {}

        if name is not None:
            daemon['name'] = name

        return Daemon(await self._session.post(f'daemons', data=daemon))

    async def get(self, daemon_id: str) -> Daemon:
        return Daemon(await self._session.get(f'daemon/{daemon_id}'))

    async def delete(self, daemon_id: str) -> Daemon:
        return Daemon(await self._session.delete(f'daemon/{daemon_id}'))


class LuciferClient(BaseClient):
    # Methods
    def __init__(self, daemon_id: str, secret: str, *, auto_logout: bool = True, tags: Optional[List[str]] = None):
        session = LuciferSession(daemon_id, secret, auto_logout=auto_logout, tags=tags)

        # Attributes
        super(LuciferClient, self).__init__(session)
        self._daemons = DaemonClient(session)

    async def version(self):
        res = await self._session.get('version')
        return APIVersion(**res)

    # Properties
    @property
    def daemons(self):
        return self._daemons
