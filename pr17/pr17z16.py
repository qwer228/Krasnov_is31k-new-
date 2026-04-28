import json
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print(loaded_data)
