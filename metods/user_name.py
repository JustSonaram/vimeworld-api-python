import requests
import json
player_name = input("Player Name: ")
url = requests.get("https://api.vimeworld.ru/user/name/" + player_name)
player = url.json()[0]
print("Name: " + player["username"] + "\nLevel: " + str(player["level"]) + "\nRank: " + player["rank"])
