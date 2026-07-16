import asyncio
class Agent:
    def __init__(self, name: str):
        self.name = name
        self.inbox = asyncio.Queue()

    async def receive(self):
        return await self.inbox.get()

    def __repr__(self):
        return f"Agent({self.name})"     