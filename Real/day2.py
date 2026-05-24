# Weather Fetcher
import requests
# url = "https://api.open-meteo.com/v1/forecast?latitude=34.0522&longitude=-118.2437&current=temperature_2m,wind_speed_10m"#](https://api.open-meteo.com/v1/forecast?latitude=34.0522&longitude=-118.2437&current=temperature_2m,wind_speed_10m)"
# response = requests.get(url)
# data = response.json()
# print(f"The temperature is {data['current']['temperature_2m']} and the wind speed is {data['current']['wind_speed_10m']}")
# Fake Product Fetcher
# url = "https://fakestoreapi.com/products/1"
# response = requests.get(url)
# if response.status_code == 200: 
#     data = response.json()
#     print(f"Product {data['title']} costs ${data['price']}.")
# else: 
#     print("Target missing or server down.")
# Quote generator -the other link was down
url = "https://zenquotes.io/api/random"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    
    # 4. Clean output execution
    print(f"\"{quote}\" — {author}")
else:
    print("Server down.")