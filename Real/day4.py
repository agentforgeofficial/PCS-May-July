#--------------Core Syntax------------------
#import httpx

# async def fetch_ai_data():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("example.com")
#         return response.json()

from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/async-weather")
async def get_async_weather():
    async with httpx.AsyncClient() as client:
        response = await client.get ("https://api.open-meteo.com/v1/forecast?latitude=34.0522&longitude=-118.2437&current=temperature_2m")
        data = response.json()
        return {
            "status" : "Success",
            "extracted temp" : data["current"]["temperature_2m"],
            "Agent Note" : "Telementry successfully intercepted asynchronously "
        }
