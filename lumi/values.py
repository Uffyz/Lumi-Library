import json
import configparser
# init
config = configparser.ConfigParser()
config.read("config.cfg", encoding="utf-8")
token = config["Settings"]["token"]
settings = config["Settings"]
path = "sources/"
# static
guilds_ids = [1119281693262622720, 1260266165880623162]
spisok_options = ['id_персонажа', 'раса', 'титул', 'цитата', 'возраст', 'должность', 'сила', 'ловкость', 'реакция', 'восприятие', 'выносливость',
                  'прочность', 'умения', 'магия', 'дьявольский_плод', 'уровень_нэн', 'апостольство',
                  'боевое_искусство', 'организация', 'воля_вооружения', 'воля_наблюдения', 'королевская_воля', 'ядро_души',
                  'осколок_души', 'чарьёк']
gifs = {
    "prichuda": {
        "scroll": "https://i.ibb.co/mBs53GM/1scrollprichuda.gif",
        "finish": "https://i.ibb.co/2Wv3PLf/1finishprichuda.gif"
    },
    "souls": {
        "scroll": "https://i.ibb.co/YL1zffh/2scrollsouls.gif",
        "finish": "https://i.ibb.co/R0ptQnx/2finishsouls.gif"
    },
    "contracts": {
        "scroll": "https://i.ibb.co/R4CHbNQ/3scrollcontract.gif",
        "rare": "https://i.ibb.co/59hkbwr/3rarecontract.gif",
        "epic": "https://i.ibb.co/2skn31W/3epiccontract.gif",
        "leg": "https://i.ibb.co/k2pmtBZ/3legcontract.gif",
        "myth": "https://i.ibb.co/984yLTX/3mythgif.gif"
    },
    "leaders": "https://i.ibb.co/2kf5jgQ/leaders.gif",
    "harakt": "https://i.ibb.co/c30T0qh/harakt.gif",
    "main_ticket": "https://i.ibb.co/s9NxZQ0y/110-20241202201525.png",
    "new_ticket": "https://i.ibb.co/7Jdx9wHV/111-20241202203224.png",
}

with open(f"{path}причуды.txt", "r", encoding="utf-8") as f:
    scroll_prichuda = f.read().split("\n")
with open(f"{path}души.txt", "r", encoding="utf-8") as f:
    scroll_souls = f.read().split("\n")
with open(f"{path}редкие контракты.txt", "r", encoding="utf-8") as f:
    rare_contracts = f.read().split("\n")
with open(f"{path}эпические контракты.txt", "r", encoding="utf-8") as f:
    epic_contracts = f.read().split("\n")
with open(f"{path}легендарные контракты.txt", "r", encoding="utf-8") as f:
    legendary_contracts = f.read().split("\n")
with open(f"{path}мифические контракты.txt", "r", encoding="utf-8") as f:
    mythical_contracts = f.read().split("\n")
with open(f"{path}stats.json", "r", encoding="utf-8") as f:
    statinfo = json.load(f)
# dynamic
def read_coins():
    with open(f"{path}coins.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_coins(data):
    with open(f"{path}coins.json", 'w', encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

def read_weather():
    with open(f"{path}weathers.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def read_tickets():
    with open(f"{path}tickets.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_tickets(data):
    with open(f"{path}tickets.json", 'w', encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
