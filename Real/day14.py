#Day 14: its all about combining everything we learned so far and make a complex agent
# multi user session id
# 
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

class MegaChat(BaseModel):
    session_id: str
    input: str

session_db = {}

system_prompt = "You're {role} and your task is {task}."
agent_role = "Research Assistant"
agent_work = "Research topics and summarize findings."
system_prompt_final = system_prompt.format(role=agent_role, task=agent_work)

@app.post("/chat")
async def prime_chat(request: MegaChat):
    sid = request.session_id
    
    # 1. Initialize session with a LIST of messages
    if sid not in session_db:
        session_db[sid] = [{"role": "system", "content": system_prompt_final}]
    
    # 2. Append the new user message
    session_db[sid].append({"role": "user", "content": request.input})
    
    # 3. Trim context (keep system prompt + last 10 messages)
    if len(session_db[sid]) > 11:
        session_db[sid] = session_db[sid][0:1] + session_db[sid][-10:]
    
    # 4. Call OpenAI/OpenRouter API
    response = client.chat.completions.create(
        model="openrouter/free",  # Note: Ensure this model identifier is valid in OpenRouter
        messages=session_db[sid],
    )
    
    final_response = response.choices[0].message.content
    
    # 5. Append assistant reply to session history
    session_db[sid].append({"role": "assistant", "content": final_response})
    
    return {
        "response": final_response
    }