import requests
import json
player_id = input("Player ID: ")
url = requests.get("https://api.vimeworld.ru/user/" + player_id + "/friends")
friends = url.json()["friends"]
"""We Will Do So To Get 3 Players."""
friend1 = friends[0]["username"]
friend2 = friends[1]["username"]
friend3 = friends[2]["username"]
print("Friends: " + friend1 + ", " + friend2 + ", " + friend3 + ".")
