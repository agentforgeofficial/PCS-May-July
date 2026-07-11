from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class NetworkPacket(BaseModel):
    source_ip : str
    destination_port : int
    protocol : str

@app.post("/analyze-packet")
async def analyze_packet(packet : NetworkPacket):
    """
    Asynchorously intercepts network packets, resolves geographic telemetry
    and applies automated firewall perimeter rules.
    """
    external_api_url = f"http://ip-api.com/json/{packet.source_ip}"
    async with httpx.AsyncClient() as client:
        response = await client.get(external_api_url)
        telemetry_Data = response.json()
        
        if telemetry_Data.get("status") == "fail":
            return {
                "firewall_action" : "DENIED",
                "security_verdict" : "Unroutable or anonymous infrastructure detected",
                "telemetry" : {"status" : "fail"}
            }
        country = telemetry_Data.get("countryCode")
        isp = telemetry_Data.get("isp")
        
        if packet.destination_port == 22 and country != "PK":
            action = "BLOCKED"
            verdict = f"Unauthorized foreign attempt to access management port 22 from {country}"
        else:
            action = "ALLOWED"
            verdict = "Traffic clears all structural perimeter security rules."
            
        return {
            "firewall_action" : action,
            "security_verdict" : verdict,
            "telemetry" : {
                "origin_country" : country,
                "infrastructure_provider" : isp,
                "protocol_utilized" : packet.protocol
            }
        }