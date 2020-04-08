import asyncio

from lucifer.client import LuciferClient


# Constants
DAEMON_ID = '5e69fc33a2cc722a2c5b1445'
DAEMON_SECRET = 'KuhhBrfZbe78GBCqRwOoTyqtSvZx5uPghnzJvE2fZh'


# Utils
async def log_version(client: LuciferClient):
    version, commit = await client.version()

    if commit is None:
        print(f'API version: {version}')
    else:
        print(f'API version: {version} (@{commit})')


# Main
async def main():
    async with LuciferClient(DAEMON_ID, DAEMON_SECRET, tags=['Tests']) as client:
        await log_version(client)

        # Get daemon's data
        daemons = await client.daemons.all()
        for daemon in daemons:
            print('-', daemon)


# Execution
if __name__ == '__main__':
    asyncio.run(main())
