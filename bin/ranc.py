import asyncio

from pynetutils import createServer

asyncio.run(createServer('127.0.0.1', 8888))