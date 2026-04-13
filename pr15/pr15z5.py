import csv

# Создаем тестовый файл
with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    f.write("name,age\nAlice,23\nBob,30\nCharlie,26")

# Решение
with open('data.csv', 'r', encoding='utf-8') as infile, \
        open('data_filtered.csv', 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if int(row['age']) > 25:
            writer.writerow(row)

print("Данные сохранены в data_filtered.csv")
