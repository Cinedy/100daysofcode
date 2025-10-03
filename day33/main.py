#API = Application Programming Interfaces
#API is a set of commands, functions, protocols and objects that programmers can use to create software or interact with an external system.
#API endpoint - usually an url

import requests
from datetime import datetime

MY_LAT = 60.318216
MY_LONG = 5.353218

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
data = sun_response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now)