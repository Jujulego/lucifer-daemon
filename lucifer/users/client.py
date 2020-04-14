from typing import List

from lucifer.bases.client import BaseClient
from lucifer.users.user import SimpleUser, User


class UsersClient(BaseClient):
    # Methods
    async def list(self) -> List[SimpleUser]:
        res = await self._session.get(f'users')
        return [SimpleUser(r) for r in res]

    async def create(self, email: str, password: str) -> User:
        user = {
            'email': email,
            'password': password
        }

        return User(await self._session.post(f'users', data=user))

    async def get(self, user_id: str) -> User:
        return User(await self._session.get(f'users/{user_id}'))

    async def delete(self, user_id: str) -> User:
        return User(await self._session.delete(f'users/{user_id}'))