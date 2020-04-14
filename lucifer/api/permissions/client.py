from typing import Callable, Generic, Optional, TypeVar

from lucifer.api.session import LuciferSession

from .permission import PermissionsHolder, PLvl

# Type vars
H = TypeVar('H', bound=PermissionsHolder)


# Client mixin
class PermissionsMixin(Generic[H]):
    # Methods
    def _init_permissions(self, session: LuciferSession, resource: str, factory: Callable[[dict], H]):
        self._factory = factory
        self._resource = resource
        self._session = session

    # Calls
    async def grant(self, holder_id: str, name: str, level: PLvl) -> H:
        data = {
            'name': name,
            'level': level
        }

        return self._factory(await self._session.put(f'{self._resource}/{holder_id}/grant', data=data))

    async def elevate(self, holder_id: str, admin: Optional[bool] = None) -> H:
        data = {}

        if admin is not None:
            data['admin'] = admin

        return self._factory(await self._session.put(f'{self._resource}/{holder_id}/elevate', data=data))

    async def revoke(self, holder_id: str, name: str) -> H:
        data = {
            'name': name
        }

        return self._factory(await self._session.put(f'{self._resource}/{holder_id}/revoke', data=data))
