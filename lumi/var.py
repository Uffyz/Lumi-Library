import configparser
# init
config = configparser.ConfigParser()
config.read("config.cfg", encoding="utf-8")
token = config["Settings"]["token"]
# static
guilds_ids = [1119281693262622720, 1260266165880623162]
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
