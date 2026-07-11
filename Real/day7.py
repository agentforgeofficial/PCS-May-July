from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import asyncio
app = FastAPI()

@app.get("/learn")
async def new_learn():
    async with httpx.AsyncClient() as client:
        quote_response = await client.get("https://dummyjson.com/quotes/random")
        quote_data = quote_response.json()
        fact_response = await client.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
        fact_data = fact_response.json()
        return {
            "Quote" : f"{quote_data['quote']} - {quote_data['author']}",
            "Fact" : f"{fact_data['text']}"
        }
        #in the above code we used await in front of client.get("x.com"), but that waits and the code
        #stops and fact response will fire only after quote is fired and completed to fire both at the same time
        #consider using the example below:
@app.get("/LearnFast")
async def fast_learn():
    async with httpx.AsyncClient() as client:
        quote_fast, fact_fast = await asyncio.gather(
            client.get("https://dummyjson.com/quotes/random"),
            client.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
        )
        quote_data = quote_fast.json()
        fact_data = fact_fast.json()
        return {
            "Quote" : f"{quote_data['quote']} - {quote_data['author']}.",
            "Fact" : f"{fact_data['text']}"
        }