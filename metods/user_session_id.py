import requests
import json
player_id = input("Player ID: ")
url = requests.get("https://api.vimeworld.ru/user/session/" + player_id)
player = url.json()[0]
print(player["username"] + " - " + player["online"]["game"])
