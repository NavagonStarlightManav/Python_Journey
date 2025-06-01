import requests
import os

from datetime import *


MY_LAT=24.363588
MY_LONG=88.624138
MY_API_ID="ddba2baa68407c090921c2f4a29c1658"
TOTAL=4

from twilio.rest import Client
account_sid="ACa3305e5e0e5d40f8a36f2758788cf4b8"
auth_token="885b105c913ab2bffa189164409b64ad"

parameter_weather={
    'lat':MY_LAT,
    'lon':MY_LONG,
    'appid':MY_API_ID,
    'cnt':TOTAL

}
response = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast?",params=parameter_weather)
response.raise_for_status()
data = response.json()
print(data)

def time_check():
    time_after=datetime(hour=17, minute=15, second=15)
    time_current=datetime.now()
    if time_current>=time_after:
        return True

will_rain=False
for hour_data in data['list']:
    print(f"{hour_data['dt_txt']} with {hour_data['weather']}")
    condition_code=hour_data['weather'][0]['id']
    if int(condition_code)<700:
        will_rain=True

if not will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It can rain buddy , have your umbrella',
        from_='+15076045786',
        to='+919501929416'
    )

print(message.status)

