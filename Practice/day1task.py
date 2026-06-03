import asyncio
class Agent():
    def __init__(self, name):
        self.name = name
        self.memory = []
    async def call_api(self, target):
        print(f"{self.name} is reaching out to {target}...")
        await asyncio.sleep(1)
        return f"Connection to {target} has been established successfully."
async def main():
    Mike = Agent("Mike Erhmantrout")
    result = await Mike.call_api("Youtube.com")
    print(result)

asyncio.run(main())