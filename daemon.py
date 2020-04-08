import asyncio

from lucifer.client import LuciferClient


# Constants
DAEMON_ID = '5e69fc33a2cc722a2c5b1445'
DAEMON_SECRET = 'KuhhBrfZbe78GBCqRwOoTyqtSvZx5uPghnzJvE2fZh'


# Main
async def main():
    async with LuciferClient(DAEMON_ID, DAEMON_SECRET, tags=['Tests']) as client:
        print(await client.version)


# Execution
if __name__ == '__main__':
    asyncio.run(main())
