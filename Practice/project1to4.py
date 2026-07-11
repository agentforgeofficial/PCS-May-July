from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import requests
app=FastAPI()
class CryptoCheck(BaseModel):
    coin_ticker : str
    
@app.post("/check-price")
async def CheckPrice(payload: CryptoCheck):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={payload.coin_ticker.upper()}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {"asset" : data['symbol'],
                "live_price_usd" : data['price'],
                "agent_status" : "Market verified successfully"
                }