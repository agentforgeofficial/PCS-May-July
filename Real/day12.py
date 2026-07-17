#day 12: Implemented multi-user session memory using an in-memory dictionary, anchored the system prompt, 
# and added sliding window context truncation to prevent token overflow.

from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()
app = FastAPI()
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

class ChatRequest(BaseModel):
    session_id : str
    topic : str

session_db = {}

@app.post("/chat")
async def chat_with_memory(request: ChatRequest):
    sid = request.session_id
    
    if sid not in session_db:
        session_db[sid] = [{"role" : "system", "content" : "You're a helpful assistant."}]
    if len(session_db[sid]) > 11:      #here, len =length~
        session_db[sid] = [session_db[sid][0]] + session_db[sid][-10:]
    session_db[sid].append (
        {"role" : "user", "content" : request.topic}
    )
    
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages= session_db[sid],
        # max_tokens=400
    )
    ai_response = response.choices[0].message.content
    session_db[sid].append(
        {"role" : "assistant", "content" : ai_response}
    )
    return{
        "message" : ai_response
    }