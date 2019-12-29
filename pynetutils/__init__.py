import asyncio

class TCPServer(asyncio.Protocol):
    def __init__(self, TIMEOUT=None):
        loop = asyncio.get_running_loop()
        self.transport = None
        self._can_write = asyncio.Event()
        self._can_write.set()
        if TIMEOUT:
            self.timeout_handle = loop.call_later(TIMEOUT, self._timeout)

    def connection_made(self, transport):
        print(f"Received connection from: {transport.get_extra_info('peername')}")
        self.transport = transport

    def data_received(self, data: bytes) -> None:
         print(f"Received {data!r}")
         self.transport.write(data)

    def connection_lost(self, exc) -> None:
        print(f"Closing connection from {self.transport.get_extra_info('peername')}")
        self.transport.close()

    def pause_writing(self) -> None:
        self._can_write.clear()

    def resume_writing(self) -> None:
        self._can_write.set()
    def _timeout(self):
        print("Closing connection")
        self.transport.close()

    @classmethod
    def createServer(cls, timeout=None):
        return cls(TIMEOUT=timeout)

async def createServer(host, port, timeout=None):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(lambda: TCPServer(timeout), host, port)
    await server.serve_forever()