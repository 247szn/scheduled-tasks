import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_api_key = os.environ.get("API_KEY")
from_number= os.environ.get("WHATSAPP_NUM")
to_number = os.environ.get("MY_NUMBER")
parameter= {
    "lat":29.951886,
    "lon":-95.194955,
    "appid":my_api_key,
    "cnt":4,
}

# rainy_weather = [for ]



response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
data = response.json()



will_rain = False
for value in data["list"]:
    weather_id = value["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain= True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is rainy,bring an umbrella!!!",
        from_=from_number,
        to=to_number,
    )

    print(message.status)

