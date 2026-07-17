from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENROUTER_API_KEY"),
    base_url= "https://openrouter.ai/api/v1"
)

system_prompt = """
You are a JSON extracter your work is to extract info from a pragraph and strictly respond in JSON, 
It is the only language you are allowed to speak. Respond in JSON or don't respond at all.
"""
history = [{"role" : "system", "content" : system_prompt}]

user_input = input("Convert to JSON: ")
history.append({"role" : "user", "content" : user_input})


response = client.chat.completions.create(
    model= "openrouter/free",
    messages=history,
    response_format= {"type" : "json_object"}
    #max_tokens=400                                          #add this if it throws a 402
)
ai_response = response.choices[0].message.content 
print(ai_response)
history.append({"role":"assistant", "content":ai_response})