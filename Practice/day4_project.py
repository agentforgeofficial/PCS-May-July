from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()


class TrafficLog(BaseModel):
    source_ip: str
    protocol: str
    destination_port: int


@app.post("/analyse-traffic")
async def TrafficAnalyser(payload: TrafficLog):
    url = f"http://ip-api.com/json/{payload.source_ip}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

        # 1. Handle API Failure instantly
        if data.get("status") == "fail":
            return {
                "firewall_action": "BLOCKED",
                "reason": "Anonymous or unroutable IP infrastructure source",
                "telemetry": {"status": "fail"},
            }

        # 2. Extract telemetry data points
        country = data.get("countryCode")
        isp = data.get("isp")

        # 3. Decision Matrix (We just set variables here, WE DO NOT RETURN YET!)
        if payload.destination_port == 22 and country != "PK":
            action = "BLOCKED"
            reason = f"Unauthorized foreign access attempt to Management Port 22 from {country}"
        else:
            action = "ALLOWED"
            reason = "Traffic clears structural perimeter rule check."

        # 4. The Single Grand Finale Return (This runs no matter what!)
        return {
            "firewall_action": action,
            "security_verdict": reason,
            "telemetry": {
                "source_country": country,
                "provider_isp": isp,
                "requested_port": payload.destination_port,
                "protocol_utilized": payload.protocol,
            },
        }