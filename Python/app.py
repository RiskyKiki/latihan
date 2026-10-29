import requests

r = requests.get("https://api.github.com")
print("Status Code:", r.status_code)
print("Content-Type:", r.headers["content-type"])
