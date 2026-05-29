from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def check_status():
    return {"status" : "online" , "system" : "Project Clean Slate"}