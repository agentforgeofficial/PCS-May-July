import asyncio
class TaskSystem():
    def __init__(self, name):
        self.name = name
        self.finished_tasks = []
    
    async def perform_task(self, task_name):
        print(f"Starting Task: {task_name}...")
        await asyncio.sleep(2)
        self.finished_tasks.append(task_name)
        return f"Task {task_name} has been completed."
async def main():
    CLI = TaskSystem("Interface1")
    print("Interface is Online.")
    
    while True:
        cmd = input("Type a task or 'exit' to stop: ")
        if cmd.lower() == 'exit':
            print("Shutting Down...")
            break
        
        result = await CLI.perform_task(cmd)
        print(result)
        print(f"Task History: {CLI.finished_tasks}")
if __name__ == "__main__":
    asyncio.run(main())