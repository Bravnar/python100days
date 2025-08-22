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
    "appid": API_KEY
}
# ---------------------------------------------- #

# with requests.get(CURRENT_WEATHER, params=PARAMS) as r:
#     weather_data = r.json()
#     print(weather_data)

with requests.get(FIVE_DAY_3H, params=PARAMS) as r:
    five_day_data = r.json()
    print(five_day_data)
    avg_temp = round(mean([float(x['main']['temp']) for x in five_day_data['list'][ : 4]]), 1)
    rain = []
    for forecast in five_day_data['list'][:4]:
        ts = int(forecast['dt'])
        chance_rain = forecast.get('rain')
        date_time = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        if chance_rain and float(chance_rain['3h']) >= 1.0:
            rain.append((chance_rain, date_time.split(":")[0]))
        # print(f"Expected rain: {rain}") if rain and float(rain['3h']) >= 1.0 else print(f"Rain not expected.")

if rain:
    rain_message = f"It might rain today at {rain[1]}!\nTake an umbrella :)"
else:
    rain_message = f"Looks like it won't rain"

sms_template = f"""

Good Morning!

Today's average temperature will be {avg_temp}C.

{rain_message}

"""

print(sms_template)



