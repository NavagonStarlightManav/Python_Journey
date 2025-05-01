import requests
from datetime import *
import pytz
import smtplib
import time


MY_LAT=30.733315
MY_LONG=76.779419
MY_EMAIL = "manavgoyal2006@gmail.com"
MY_PASSWORD = "buni cleb iety nikv"

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

def position_check_coordinates():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if MY_LAT-10 <= iss_latitude <= MY_LAT +10 and MY_LONG-10 <= iss_longitude <= MY_LONG+10:
        return True

def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # Split and Pick the First Part of Lists created and again apply split on them

    # Convert to dateime objects
    sunrise_utc = datetime.fromisoformat(sunrise)
    sunset_utc = datetime.fromisoformat(sunset)

    # Defining UTC AND IST time zones
    utc_zone = pytz.utc
    ist_zone = pytz.timezone("Asia/Kolkata")

    # Convert UTC datetime to IST
    sunrise_itc = sunrise_utc.replace(tzinfo=utc_zone).astimezone(ist_zone)
    sunset_itc = sunset_utc.replace(tzinfo=utc_zone).astimezone(ist_zone)

    time_now=datetime.now(ist_zone)

    if time_now>=sunset_itc or time_now<sunrise_itc:
        return True

while True:
    time.sleep(60)
    if position_check_coordinates() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="manavideas3075@gmail.com",
                msg="Subject: Look Up in the Sky sir ISS is above you now in the sky"
            )


