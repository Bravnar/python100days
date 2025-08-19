import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

ISS_API = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"

LAT = float(os.getenv('LAT', '0'))
LNG = float(os.getenv('LNG', '0'))
TIMEZONE = os.getenv("TIMEZONE", "Europe/Berlin")

USER = os.getenv('APP_USER')
PASSWD = os.getenv('APP_PASS')
SMTP_PORT = os.getenv('SMTP_PORT')
RECIPIENTS = tuple(os.getenv('RECIPIENTS').split(','))

LAT_RANGE = (LAT - 5, LAT + 5)
LNG_RANGE = (LNG - 5, LNG + 5)

# ------------------- GET API DATA ---------------------------#

try:
    r_sun = requests.get(
        url=SUNRISE_SUNSET_API,
        params={
            "lat": LAT,
            "lng": LNG,
            "tzid": TIMEZONE,
            "formatted": 0
        }
    )
    r_iss = requests.get(url=ISS_API)
    r_sun.raise_for_status()
    r_iss.raise_for_status()
except requests.exceptions.HTTPError as err:
    SystemExit(err)

sunrise_hour = int(r_sun.json()['results']['sunrise'].split("T")[1].split(":")[0])
sunset_hour = int(r_sun.json()['results']['sunset'].split("T")[1].split(":")[0])

longitude = float(r_iss.json()['iss_position']['longitude'])
latitude = float(r_iss.json()['iss_position']['latitude'])

# ----------------- SEND EMAIL -------------------------------#

def notify():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWD)
        message = f"Subject: ISS is visible!\n\nThe ISS should be visible right NOW: {datetime.now().hour}:{datetime.now().minute}!\nBest,\nBravPy3"
        connection.sendmail(from_addr=USER, to_addrs=RECIPIENTS, msg=message)

# ----------------- CHECK IF OVERHEAD ------------------------#

hour_now = datetime.now().hour

is_night = hour_now >= sunset_hour or hour_now <= sunrise_hour

within_lat = LAT_RANGE[0] <= latitude <= LAT_RANGE[1]
within_lng = LNG_RANGE[0] <= longitude <= LNG_RANGE[1]

while True:
    time.sleep(60)
    if is_night and within_lat and within_lng:
        print("ISS is visible, e-mail sent to recipients")
        notify()
