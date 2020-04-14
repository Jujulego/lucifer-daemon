from abc import ABC

from lucifer.session import LuciferSession


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