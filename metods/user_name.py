import requests
import json
player_name = input("Player Name: ")
url = requests.get("https://api.vimeworld.ru/user/name/" + player_name)
player = url.json()[0]
"""Using The print() command, they showed: Username, Level, Rank."""
print("Name: " + player["username"] + "\nLevel: " + str(player["level"]) + "\nRank: " + player["rank"])
"""Und Save Player ID"""
player_id = player["id"]
