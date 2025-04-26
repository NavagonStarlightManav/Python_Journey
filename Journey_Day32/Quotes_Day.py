import smtplib

import pandas as pd
import random
import datetime as dt

MY_EMAIL="manavgoyal2006@gmail.com"
MY_PASSWORD="buni cleb iety nikv"

now = dt.datetime.now()
weekday=now.weekday()

if weekday==4:
    with open("quotes.txt") as quote_file:
        all_Quotes=quote_file.readlines()
        quote=random.choice(all_Quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="manavideas3075@gmail.com",
            msg=f"Subject:Friday Motivation\n\n{quote}"
        )


