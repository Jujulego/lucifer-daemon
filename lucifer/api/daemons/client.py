from typing import List, Optional, Union

from lucifer.api.bases.client import BaseClient
from lucifer.api.permissions.client import PermissionsMixin
from lucifer.api.users.user import User

from .daemon import SimpleDaemon, Daemon


# Client
class DaemonsClient(BaseClient, PermissionsMixin[Daemon]):
    # Methods
    def __init__(self, *args, **kwargs):
        super(DaemonsClient, self).__init__(*args, **kwargs)

        self._init_permissions(self._session, 'daemons', lambda data: Daemon(data))

    async def list(self) -> List[SimpleDaemon]:
        res = await self._session.get('daemons')
        return [SimpleDaemon(r) for r in res]

    async def create(self, name: Optional[str] = None) -> Daemon:
        daemon = {}

        if name is not None:
            daemon['name'] = name

        return Daemon(await self._session.post('daemons', data=daemon))

    async def get(self, daemon_id: str) -> Daemon:
        return Daemon(await self._session.get(f'daemons/{daemon_id}'))

    async def update(self, daemon_id: str, *, name: Optional[str] = None, user: Optional[Union[str, User]] = None) -> Daemon:
        data = {}

        if name is not None:
            data['name'] = name

        if user is not None:
            data['user'] = user.id if isinstance(user, User) else user

        return Daemon(await self._session.put(f'daemons/{daemon_id}', data=data))

    async def delete(self, daemon_id: str) -> Daemon:
        return Daemon(await self._session.delete(f'daemons/{daemon_id}'))
