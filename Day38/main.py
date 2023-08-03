import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
load_dotenv()


# APP_ID = "0b256c05"
APP_ID =os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = os.environ.get("SHEETY_URL")
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")


TOKEN = os.environ.get("TOKEN")

print(today)
print(time)

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}


exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": "100",
    "height_cm": "189",
    "age": "27"
}


exercise_response = requests.post(url=URL, json=exercise_params, headers=headers)
exercise_data = exercise_response.json()['exercises']
# print(exercise_data)
for each_exercise in exercise_data:
    date = today
    exercise_name = each_exercise['name']
    duration = each_exercise['duration_min']
    calories = each_exercise['nf_calories']
    
    headers2 = {
        "Content-Type": "application/json",
        # basic Auth 하는 방법
        "Authorization": TOKEN
    }
    
    workout_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": int(duration),
            "calories": calories     
        }
    }

    exercise_record_response = requests.post(url=SHEETY_URL, json=workout_params, headers=headers2)
    print(exercise_record_response.text)
    


