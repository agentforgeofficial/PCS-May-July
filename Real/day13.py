from pydantic import BaseModel
from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

class RoutedAgent(BaseModel):
    user_input : str

def get_weather_data():
    return {
        "condition" : "Sunny",
        "temperature" : "38°C",
        "location" : "local"
}
def get_help_menu():
    return {
        "available commands" : "weather, chat, help"
    }
    
ROUTER_PROMPT = """
You are a routing agent. Analyze user input and classify its intent into strictly ONE of the two categories below:
-WEATHER (if they ask for temperature, rain, forecast or clothing advice for conditions)
-GENERAL (for any other casual conversation or statements)
"""

@app.post("/router")
async def routed_chat(request: RoutedAgent):
    text = request.user_input.strip().lower()
    
    messages = [
        {"role" : "system", "content" : ROUTER_PROMPT},
        {"role" : "user", "content" : text}
    ]
    
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    
    intent = response.choices[0].message.content.strip().lower()
    #Decision Logic
    
    if "weather" in intent:
        return {
            "routed_executed" : "dynamic_weather_function",
            "output" : get_weather_data()
        }
    else:
        return {
            "route_executed" : "dynamic_general_chat",
            "output" : "This is fallback chatter due to incomplete function.",
            "int" : intent
        }
        