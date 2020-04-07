import asyncio

from lucifer.session import LuciferSession


# Constants
DAEMON_ID = '5e69fc33a2cc722a2c5b1445'
DAEMON_SECRET = 'KuhhBrfZbe78GBCqRwOoTyqtSvZx5uPghnzJvE2fZh'


# Main
async def main():
    async with LuciferSession(DAEMON_ID, DAEMON_SECRET, tags=['tests']) as session:
        res = await session.get('version')
        print(res)


# Execution
if __name__ == '__main__':
    asyncio.run(main())
