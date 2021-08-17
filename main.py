import json
import requests

API_BASE_URL = " https://superheroapi.com/api/"
TOKEN = "2619421814940190/"
name = ["Hulk", "Captain America", "Thanos"]
heroes ={}
intelligence_heroes = {}

for hero in name:
    response = requests.get(API_BASE_URL + TOKEN + "search/" + hero)
    json_dict = response.json()
    heroes[hero] = json_dict.get("results")[0].get("id")
for hero in heroes:
    character_id = heroes[hero]
    response = requests.get(API_BASE_URL + TOKEN + character_id + "/powerstats")
    intelligence_heroes[hero] = int(json.loads(response.text)["intelligence"])
int = max(intelligence_heroes.values())
int_max = {}
for name in intelligence_heroes:
    if intelligence_heroes[name] == int:
        int_max[name] = intelligence_heroes[name]
print(int_max)

