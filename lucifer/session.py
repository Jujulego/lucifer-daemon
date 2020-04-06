import aiohttp
from typing import Optional
from urllib.parse import urljoin

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

    def _url(self, path: str):
        return urljoin(self.endpoint, path)

    async def open(self):
        # Already opened
        if self._session is not None:
            return

        # Open session
        self._session = aiohttp.ClientSession()

        # Connect
        if self._token is None:
            await self.login()

    async def login(self):
        data = await self.post('/daemons/login', data={'id': self._id, 'secret': self._secret})

        self._token = data['token']
        self._daemon = data['daemon']

    async def request(self, method: str, path: str, *_, **kwargs):
        try:
            async with self._session.request(method, self._url(path), **kwargs) as resp:
                return await resp.json()

        except aiohttp.ClientResponseError as err:
            if err.status == 401:
                self._token = ''

            raise

    async def get(self, path: str, *, params: dict = None):
        return await self.request('get', path, params=params, headers=self.headers)

    async def post(self, path: str, *, data: dict, params: dict = None):
        return await self.request('post', path, params=params, headers=self.headers, json=data)

    async def put(self, path: str, *, data: dict, params: dict = None):
        return await self.request('put', path, params=params, headers=self.headers, json=data)

    async def delete(self, path: str, *, params: dict = None):
        return await self.request('delete', path, params=params, headers=self.headers)

    async def close(self):
        if self._session is None:
            return

        # Close session
        await self._session.close()
        self._session = None

    # Properties
    @property
    def endpoint(self):
        return 'http://localhost:8000/api'

    @property
    def headers(self):
        return {
            'Authorization': f'Bearer {self._token}' if self._token else None
        }
