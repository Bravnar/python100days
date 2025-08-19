import requests

ISS_API = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=ISS_API)
response.raise_for_status()

decoded_data = response.json()

longitude = decoded_data["iss_position"]["longitude"] 
latitude = decoded_data["iss_position"]["latitude"] 

iss_position = (latitude, longitude)

print(iss_position)

