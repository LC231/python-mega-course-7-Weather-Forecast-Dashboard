import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "London",
    "appid": "8058b1cd2e087376860df2fd8b9721a4",
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Response:", response.json())
