# import pywhatkit as pkt

# pkt.search("google")

import json

filename = "./database/data1.json"

with open(filename, "r") as f:
    data = json.load(f)
    name_data = (data["names"])
    for i in name_data:
        name = (i["name"])
        print(name)