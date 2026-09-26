import requests
import pandas as pd

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"

res = requests.get(URL, timeout=30)
print(res.status_code)

data = res.json()
print(data.keys())
print(len(data["elements"]))