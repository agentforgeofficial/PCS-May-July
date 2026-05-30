from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def check_status():
    return {"status" : "online" , "system" : "Project Clean Slate"}

@app.get("/user/{user_id}")
def access_uid(user_id: int):
    return {"message" : f"Accessing the user id: {user_id}"}

from pydantic import BaseModel
class ChatMessage(BaseModel):
    sender : str
    message : str
    
@app.post("/chat")
def send_message(payload: ChatMessage):
    return {
        "status" : "Processed",
        "Info" : f"Agent {payload.sender} said: {payload.message}"
            }