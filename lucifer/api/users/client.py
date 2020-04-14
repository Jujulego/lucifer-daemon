from typing import List, Optional

from lucifer.api.bases.client import BaseClient
from lucifer.api.permissions.client import PermissionsMixin
from lucifer.api.users.user import SimpleUser, User


# Client
class UsersClient(BaseClient, PermissionsMixin[User]):
    # Methods
    def __init__(self, *args, **kwargs):
        super(UsersClient, self).__init__(*args, **kwargs)

        self._init_permissions(self._session, 'users', lambda data: User(data))

    async def list(self) -> List[SimpleUser]:
        res = await self._session.get('users')
        return [SimpleUser(r) for r in res]

    async def create(self, email: str, password: str) -> User:
        user = {
            'email': email,
            'password': password
        }

        return User(await self._session.post('users', data=user))

    async def get(self, user_id: str) -> User:
        return User(await self._session.get(f'users/{user_id}'))

    async def update(self, user_id: str, *, email: Optional[str] = None, password: Optional[str] = None) -> User:
        data = {}

        if email is not None:
            data['email'] = email

        if password is not None:
            data['password'] = password

        return User(await self._session.put(f'users/{user_id}', data=data))

    async def delete(self, user_id: str) -> User:
        return User(await self._session.delete(f'users/{user_id}'))
