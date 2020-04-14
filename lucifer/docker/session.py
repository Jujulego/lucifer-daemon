import docker
from typing import Optional


# Class
class DockerSession:
    # Attributes
    _client: Optional[docker.DockerClient] = None

    # Methods
    async def open(self):
        self._client = docker.from_env()

    async def close(self):
        self._client.close()
        self._client = None

    # Properties
    @property
    def client(self) -> docker.DockerClient:
        return self._client

    @property
    def connected(self) -> bool:
        return self._client is not None
