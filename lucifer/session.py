import aiohttp
from typing import List, Optional
from urllib.parse import urljoin

from lucifer.base.session import BaseSession


# Class
class LuciferSession(BaseSession):
    # Attributes
    _daemon: Optional[str] = None
    _token: Optional[str] = None
    _session: Optional[aiohttp.ClientSession] = None

    # Methods
    def __init__(self, id: str, secret: str, *, auto_logout: bool = False, tags: Optional[List[str]] = None):
        # Attributes
        self._id = id
        self._secret = secret
        self._tags = tags or []  # type: List[str]
        self._auto_logout = auto_logout

    def __repr__(self):
        if self.connected:
            return f'<LuciferSession: {self.endpoint} (connected)>'

        return f'<LuciferSession: {self.endpoint}>'

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

    async def request(self, method: str, path: str, *_, **kwargs):
        try:
            async with self._session.request(method, self._url(path), **kwargs) as resp:
                if resp.content_length == 0:
                    return

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

    async def login(self):
        data = await self.post('daemons/login', data={
            'id': self._id,
            'secret': self._secret,
            'tags': self._tags
        })

        self._token = data['token']
        self._daemon = data['daemon']

    async def logout(self):
        await self.delete('logout')

        self._token = None

    async def close(self):
        if self._session is None:
            return

        # Disconnect
        if self._auto_logout:
            await self.logout()

        # Close session
        await self._session.close()
        self._session = None

    # Properties
    @property
    def connected(self):
        return self._token is not None

    @property
    def endpoint(self):
        return 'http://localhost:8000/api/'

    @property
    def headers(self):
        if not self.connected:
            return None

        return {
            'Authorization': f'Bearer {self._token}'
        }
