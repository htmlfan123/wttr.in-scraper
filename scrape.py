import requests

url = "https://wttr.in/London?format=j1"
response = requests.get(url, timeout=10)
response.raise_for_status()

weather = response.json()
current = weather["current_condition"][0]

print("Temperature:", current["temp_C"], "°C")
print("Conditions:", current["weatherDesc"][0]["value"])
