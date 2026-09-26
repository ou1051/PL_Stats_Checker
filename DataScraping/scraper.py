import requests
import pandas as pd

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"

res = requests.get(URL, timeout=30)
print(res.status_code)

data = res.json()
print(data.keys())
print(len(data["elements"]))
COLUMNS = [
    "id", "first_name", "second_name", "web_name", "team", "element_type", "birth_date",
    "minutes", "starts", "goals_scored", "assists", "penalties_missed",
    "clean_sheets", "goals_conceded", "own_goals", "saves", "penalties_saved",
    "tackles", "recoveries", "clearances_blocks_interceptions",
    "yellow_cards", "red_cards",
    "expected_goals", "expected_assists", "expected_goal_involvements", "expected_goals_conceded",
] # columns to keep for the CSV

players = pd.DataFrame(data["elements"]) # fetching 667 players data from api
players = players[COLUMNS] # selecting what we need for csv

print(players.shape)
print(players.head())

teams = {t["id"]: t["name"] for t in data["teams"]}
positions = {p["id"]: p["singular_name_short"] for p in data["element_types"]}

players["team"] = players["team"].map(teams)
players["element_type"] = players["element_type"].map(positions)
players = players.rename(columns={"element_type": "position"})

print(players[["web_name", "team", "position"]].head())

