import requests
import os
from datetime import datetime

# header = requests.get('https://httpbin.org/basic-auth/user/pass', auth=("Authorization", 'Basic ZXVuYmFlOjkxOTU='))
APP_ID = "{}"
APP_KEY = "{}"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 190,
    "age": 27
}
today = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X')

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

for ex in result['exercises']:
    sheety_input = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": ex['name'].title(),
            "duration": ex['duration_min'],
            "calories": ex['nf_calories']
        }
    }

sheety_endpoint = "https://api.sheety.co/d8b4d640fe785403eef0cbdd3772a1de/workoutTracking/workouts"

sheety_response = requests.post(url=sheety_endpoint, json=sheety_input, auth=("{}", "{}"))
print(sheety_response.text)
