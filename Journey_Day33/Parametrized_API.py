import requests
from datetime import *
import pytz

MY_LAT=30.733315
MY_LON=76.779419

parameters={
    "lat":MY_LAT,
    "lng":MY_LON,
    "formatted":0,
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()

sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
# Split and Pick the First Part of Lists created and again apply split on them


# Convert to dateime objects
sunrise_utc=datetime.fromisoformat(sunrise)
sunset_utc=datetime.fromisoformat(sunset)

# Defining UTC AND IST time zones
utc_zone=pytz.utc
ist_zone=pytz.timezone("Asia/Kolkata")

# Convert UTC datetime to IST
sunrise_itc=sunrise_utc.replace(tzinfo=utc_zone).astimezone(ist_zone)
sunset_itc=sunset_utc.replace(tzinfo=utc_zone).astimezone(ist_zone)


print(sunrise_itc)
print(sunset_itc)


time_now=datetime.now()
print(time_now.hour)
