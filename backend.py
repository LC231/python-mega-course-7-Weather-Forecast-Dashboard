import requests

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "London",
    "appid": "0d2755d801d0009bdcc676798735385d",
    "units": "metric"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Response:", response.json())
