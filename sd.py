import asyncio

class MiniAgent():
    def __init__(self, name):
        self.name = name
        self.log = []
    async def ping(self, target:str):
        await asyncio.sleep(1)
        self.log.append(f"Pinged {target}")
        return f"Success: {target}"
async def main():
    Gablo = MiniAgent("Gabriel")
    result = await Gablo.ping("Matrix")
    print(result)
    
asyncio.run(main())