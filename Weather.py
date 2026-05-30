from fastapi import FastAPI
from datetime import datetime
import requests
import random

app = FastAPI()

cold_recs = ["Brew some hot coffee.", "Hit the gym indoors.", "Boot up the PC and game."]
good_recs = ["Go for a run.", "Work from a coffee shop patio.", "Take a walk."]
hot_recs  = ["Blast the AC.", "Chug ice water.", "Stay inside and code."]

@app.get("/weather")
def get_weather():
    clean_time = datetime.now().strftime("%d-%b-%Y %H:%M")
    
    url_weather = "https://api.open-meteo.com/v1/forecast?latitude=25.3960&longitude=68.3578&current=temperature_2m"
    url_quote = "https://zenquotes.io/api/random"

    data_w = requests.get(url_weather).json()
    data_q = requests.get(url_quote).json()

    
    clean_temperature = data_w["current"]["temperature_2m"]
    
    if clean_temperature < 15:
        comment = "It's absolutely freezing out there."
        recommendation = random.choice(cold_recs)
    
    elif 15 <= clean_temperature <= 25:
        comment = "The weather is perfect right now."
        recommendation = random.choice(good_recs)
        
    else:  
        comment = "It's a complete scorcher out there."
        recommendation = random.choice(hot_recs)
    
    return {
        "Date & Time" : clean_time,
        "Temperature Celcius" : clean_temperature,
        "Agent's Comment" : comment,
        "Recommendation" : recommendation,
        "Life Quote" : f"\"{data_q[0]['q']}\" - {data_q[0]['a']}"
    }
        
