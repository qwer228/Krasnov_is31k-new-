import json
data = {"name": "Alice", "age": 30, "city": "Moscow"}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
print("JSON сохранён.")
