import requests
import datetime
import os
from openpyxl import Workbook
from dotenv import load_dotenv


load_dotenv("Sensitive.env")

application_id = os.environ.get("application_id")
application_key = os.environ.get("application_key")
sheety_bearer = os.environ.get("sheety_bearer")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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

Sheet_endpoint = "https://api.sheety.co/698eceba8cb124c9fa5db42221d59c68/manavPersonalWorkouts/workouts"

bearer_headers = {
    "Authorization": f"Bearer {sheety_bearer}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(
        Sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheet_response.text)
