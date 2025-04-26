import smtplib

my_email="manavgoyal2006@gmail.com"
password="buni cleb iety nikv"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="manavideas3075@gmail.com",
        msg="Subject: Hello Python\n\n This is my first python email"
    )


import datetime as dt

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()
print(day_of_week)

date_of_birth=dt.datetime(year=1995,month=12,day=15)
print(date_of_birth)

