#Project Rain Alert

import requests

MY_LAT = 60.391262
MY_LONG = 5.322054
api_key = "4db618e2edb7cb767e04a59fc63a2887"
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OMW_Endpoint, params=parameters)
response.raise_for_status()
print(f"Status code: {response.status_code}")

weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
