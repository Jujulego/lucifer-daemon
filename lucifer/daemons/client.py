from typing import List, Optional

from lucifer.bases.client import BaseClient
from lucifer.daemons.daemon import SimpleDaemon, Daemon


class DaemonsClient(BaseClient):
    # Methods
    async def list(self) -> List[SimpleDaemon]:
        res = await self._session.get(f'daemons')
        return [SimpleDaemon(r) for r in res]

    async def create(self, name: Optional[str] = None) -> Daemon:
        daemon = {}

        if name is not None:
            daemon['name'] = name

        return Daemon(await self._session.post(f'daemons', data=daemon))

    async def get(self, daemon_id: str) -> Daemon:
        return Daemon(await self._session.get(f'daemons/{daemon_id}'))

    async def delete(self, daemon_id: str) -> Daemon:
        return Daemon(await self._session.delete(f'daemons/{daemon_id}'))