import requests

r = requests.get("https://www.ggogle.com")

print(r.status_code)
