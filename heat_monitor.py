import datetime
import json
import requests

today = datetime.date.today().strftime("%Y-%m-%d")

arpa_value = 37

try:
    r = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=45.46&longitude=9.19&hourly=temperature_2m",
        timeout=5
    )
    data_api = r.json()
    arpa_value = data_api.get("hourly", {}).get("temperature_2m", [37])[-1]
except:
    pass

if arpa_value > 35:
    ministero = 3
elif arpa_value > 30:
    ministero = 2
else:
    ministero = 1

# 🔴 LIVE DATA FILE
data = {
    "date": today,
    "arpa": float(arpa_value),
    "ministero": ministero
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

print("DATA UPDATED")
