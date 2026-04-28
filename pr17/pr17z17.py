import csv
users = [
    ["Имя", "Возраст", "Город"],
    ["Алексей", 28, "Москва"],
    ["Мария", 32, "Санкт-Петербург"],
    ["Иван", 25, "Казань"]
]
with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(users)
print("CSV создан.")
