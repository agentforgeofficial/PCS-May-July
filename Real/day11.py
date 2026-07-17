#day 11: Connected LLM to FastAPI route, api key secured in gitignored environment variable, the agent
# has session memory too.

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key = os.getenv("OPENROUTER_API_KEY"),
    base_url= "https://openrouter.ai/api/v1"
)

messagess = [
    {
        "role":"system",
     "content":"You're a helpful assistant."
     }
    ]
class ExplainRequest(BaseModel):
    topic : str
@app.post("/explain")
def explain(request : ExplainRequest):
    
    
    messagess.append(
    {
        "role" : "user",
        "content" : request.topic
     }
    )
    
    response = client.chat.completions.create(
        model="openrouter/free",
        messages = messagess
        #max_tokens=400                                          #add this if it throws a 402
    )
    
    ai_response = response.choices[0].message.content
    messagess.append(
        {"role" : "assistant", "content" : ai_response}
    )
    return {
        "message" : ai_response
        }
    
    