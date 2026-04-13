import csv

# Создаем тестовый файл
with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    f.write("name,age\nAlice,23\nBob,30")

# Решение
ages = []
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ages.append(int(row['age']))

if ages:
    print(f"Средний возраст: {sum(ages) / len(ages)}")
