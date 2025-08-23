from dotenv import load_dotenv
from os import getenv
import requests
from datetime import datetime
from statistics import mean

# --------- ENV -------------------------------- #
load_dotenv()
API_KEY = getenv('API_KEY_WEATHER', '')
LAT = float(getenv('LAT', 0.0))
LNG = float(getenv('LNG', 0.0))

# --------- API -------------------------------- #

CURRENT_WEATHER = "https://api.openweathermap.org/data/2.5/weather" #?lat={lat}&lon={lon}&appid={API key}
FIVE_DAY_3H = "https://api.openweathermap.org/data/2.5/forecast" #lat={lat}&lon={lon}&appid={API key}"
PARAMS = {
    "lat": LAT,
    "lon": LNG,
    "units": "metric",
    "cnt": 4,
    "appid": API_KEY
}
# ---------------------------------------------- #

# with requests.get(CURRENT_WEATHER, params=PARAMS) as r:
#     weather_data = r.json()
#     print(weather_data)

# ----------------- BUILDING THE SMS ------------------------------ #

with requests.get(FIVE_DAY_3H, params=PARAMS) as r:
    r.raise_for_status()
    weather_data = r.json()
    avg_temp = round(mean([float(x['main']['temp']) for x in weather_data['list']]), 1)
    rain = []
    for forecast in weather_data['list']:
        ts = int(forecast['dt'])
        chance_rain = forecast.get('rain')
        date_time = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        if chance_rain and float(chance_rain['3h']) >= 1.0:
            rain.append((chance_rain, date_time.split(":")[0]))

if rain:
    rain_times = []
    for occ in rain:
        rain_times.append(f"{occ[1]}:00") 

    rain_message = f"It might rain today at {rain_times}!\nTake an umbrella :)"
else:
    rain_message = "Doesn't look like it will rain today."

sms_template = f"""
Good Morning!

Today's average temperature will be {avg_temp}C.

{rain_message}

"""
# print(sms_template)

# ------------------- TWILIO ---------------------------------------#

from twilio.rest import Client

account_sid = getenv('ACCOUNT_SID')
auth_token = getenv('AUTH_TOKEN')
messaging_service_sid = getenv('MSG_SID')
phone_number = getenv('PHONE_NUMBER')

client = Client(account_sid, auth_token)
message = client.messages.create(
    messaging_service_sid=messaging_service_sid,
    body=sms_template,
    to=phone_number
)
print(message.sid)


