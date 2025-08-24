
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
USERNAME = getenv('USERNAME')
PIXELA_URL = "https://pixe.la/"

r = requests.post(PIXELA_URL + "v1/users", json={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
})
print(r.text)
