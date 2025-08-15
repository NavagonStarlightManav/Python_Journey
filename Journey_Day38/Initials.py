import requests
import datetime
import os
from openpyxl import Workbook


application_id = "dc01167d"
application_key = "0b3c9311f757ac2aabeb06097f1267d4"
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID = os.environ.get("application_id")
print(APP_ID)

nutrition_headers = {
    "x-app-id": application_id,
    "x-app-key": application_key
}

exercise_text = input("Tell me which exercises you did: ")


user_param = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 180,
    "age": 19
}

response = requests.post(url=nutrition_endpoint, headers=nutrition_headers, json=user_param)
result = response.json()


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")



wb = Workbook()
ws = wb.active
ws.title = "Workout Data"


ws.append(["Date", "Time", "Exercise", "Duration (min)", "Calories Burned"])


for exercise in result["exercises"]:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    print(f"{today_date} {now_time} - {exercise_name} | Duration: {duration} min | Calories: {calories}")
    ws.append([today_date, now_time, exercise_name, duration, calories])


wb.save("workout_data.xlsx")
print("\n Data saved to workout_data.xlsx")
