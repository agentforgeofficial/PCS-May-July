from openai import OpenAI
from fastapi import FastAPI
import httpx


client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key= "OPENAI_API_KEY"
)

history = [
    {"role" : "system", "content" : "become annyoing dont ask questions straight make people hooked, be funny sarcastic and a bit teasing(notin the sexual way)."}
]

print ("---Day8 agent online, fire away any queries, type 'exit' to stop.")
while True:
    user_input = input("Ask anything: ")
    
    if user_input.lower() == 'exit':
        print("Disconnecting...")
        break
    
    history.append({"role" : "user", "content" : user_input})
    
    response = client.chat.completions.create(
        model = "openrouter/free",
    messages=history
    )
    
    ai_response = response.choices[0].message.content
    print(f"\n Agent response: {ai_response}\n")
    history.append({"role" : "assistant", "content" : ai_response})