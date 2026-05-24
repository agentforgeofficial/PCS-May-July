# def greeter(name, place):
#     return f"Hello {name}, from {place}."

# data = greeter("Hadi", "Hyderabad")
# print(data)

# def respond(prompt, model="Deepseek 2o"):
#     return f"Using {model} to process: {prompt}"
# print(respond("Write a poem", "Gpt-4o"))
# print(respond("Write a poem"))

# def create_task(task_name: str, priority:int=1):
#     return f"Task '{task_name}' created with priority {priority}."

# print(create_task("Fix Bug"))

# dict1 = {
#     "agent name":"Altair",
#     "status" : "Active"
# }

# dict1["agent name"] = "Ezio Auditore"
# print(dict1["agent name"])
# dict1["Location"] = "Assassin's Creed 1"
# print(dict1["Location"])
# Weapons=["SMG","LMG","RPG","Assault Rifle"]
# for Weapon in Weapons:
#     print(f"Current Weapon : {Weapon}.")

# Far_Cry_5= {
#     "Protagonist" : "Deputy",
#     "Antagonist" : "Joseph Seed",
#     "Location" : "Hope County, Montana, USA",
# }
# Allies = Far_Cry_5.get("Allies", "Hurk Drubman Jr.")
# print(Allies)
# for key in Far_Cry_5:
#     print(key)
# print(Far_Cry_5)
# for key, value in Far_Cry_5.items():
#     print(f"{key} is set to {value}.")
    
# tools = [
#       {
#         "name": "weather",
#         "type": "API",
#         "Idea": "Gemini"
#     },
#     {
#         "name": "Cloud",
#         "type": "Advanced API",
#         "Idea": "Self"
#     }
# ]
# for tool in tools:
#     print(f"Loading Tool: {tool["name"]} (type: {tool["type"]}) by {tool["Idea"]}")
# class Agent():
#     def __init__(self, name):
#         self.name = name
#         self.memory = []
#     def speak(self, message):
#         return f" {self.name} says: {message}"

# Gemmer = Agent("MrGem")
# print(Gemmer.name)
# print(Gemmer.speak("Hello there!"))
class Agent():
    def __init__ (self, name):
        self.name = name
        self.memory = []
    def add_memory(self, text):
        self.memory.append(text)
    def show_memory(self):
        return self.memory
    
Michael_De_Santa = Agent("Mike")
Michael_De_Santa.add_memory("Born In Los Santos")
Michael_De_Santa.show_memory()