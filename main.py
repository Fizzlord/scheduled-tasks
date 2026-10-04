import requests
import os

MY_LATITUDE = float(os.environ.get("MY_LATITUDE"))
MY_LONGITUDE = float(os.environ.get("MY_LONGITUDE"))
MY_API_KEY = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": MY_API_KEY,
    "cnt": 4,
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()

weather_data = response.json()

Raining = False

len_of_list = len(weather_data["list"])
for index in range(len_of_list):
    weather_code = weather_data["list"][index]["weather"][0]["id"]
    if weather_code < 700:
        Raining = True
print(Raining)
if Raining:
    print("yes")
    res = requests.post(
        'https://api.textbee.dev/api/v1/gateway/send-sms',
        headers={'x-api-key':os.environ.get("TEXTBEE_API")},
        json={
            'deviceId': os.environ.get("DEVICE_ID"),
            'recipients': [os.environ.get("MY_PHONE_NUMBER")],
            'message': "It's Raining outside. Bring an Umbrella ☔",
        },
    )
