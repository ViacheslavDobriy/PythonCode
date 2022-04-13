import json
from UI import pressure_view

device = 1
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    },
    "vice-president": {
        "name": pressure_view(device),
        "why?": "I want"
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)