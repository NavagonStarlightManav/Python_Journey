import pandas as pd
import datetime as dt
import random
import smtplib


df=pd.read_excel("Birthday_File.xlsx")
print(df.head())

birthday_dict=df.to_dict(orient="records")
print(birthday_dict[0])


date_today=dt.datetime.now()
day=date_today.day
month=date_today.month
year=date_today.year


MY_EMAIL="manavgoyal2006@gmail.com"
MY_PASSWORD="buni cleb iety nikv"

for dates in birthday_dict:
    if dates['day']==day and dates['month']==month:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=dates['email'],
                msg=f'''
                  Subject:Loving Day of life
                  
                  Dear {dates['name']},

                  Happy birthday

                  All the best for the year

                  Manav Goyal loves you a lot
               '''
            )


# you can also proceed with creating dictionary from dataset using dictionary comprehension
birthday_dict={(data_row['month'],data_row['day']):data_row for (index,data_row) in df.iterrows()}

today_tuple=(dt.datetime.now().day,dt.datetime.now().month)

# other approach was sending a letter by opening a letter