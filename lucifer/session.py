import aiohttp
from typing import Optional

from lucifer.base.session import BaseSession


# Class
class LuciferSession(BaseSession):
    # Attributes
    _daemon: Optional[str] = None
    _token: Optional[str] = None
    _session: Optional[aiohttp.ClientSession] = None

    # Methods
    def __init__(self, id: str, secret: str):
        # Attributes
        self._id = id
        self._secret = secret

    async def _login(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.endpoint}/daemons/login', json={'id': self._id, 'secret': self._secret}) as resp:
                data = await resp.json()

                self._token = data['token']
                self._daemon = data['daemon']

    async def open(self):
        # Already opened
        if self._session is not None:
            return

        # Connected ?
        if self._token is None:
            await self._login()

        # Open session
        headers = {
            'Authorization': f'Bearer {self._token}'
        }

        self._session = aiohttp.ClientSession(headers=headers)

    async def close(self):
        if self._session is None:
            return

        # Close session
        await self._session.close()
        self._session = None

    # Properties
    @property
    def endpoint(self):
        return 'http://localhost:4200/api'
