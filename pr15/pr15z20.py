from collections import Counter

# Создаем тестовый файл
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("2026-04-01 ERROR Something failed\n2026-04-02 INFO All good\n2026-04-03 ERROR Crash\n2026-04-03 ERROR Network")

# Решение
error_counts = Counter()

with open('log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if "ERROR" in line:
            date_part = line.split(" ")[0] # Берем дату
            error_counts[date_part] += 1

print("Ошибки по дням:")
for date, count in sorted(error_counts.items()):
    print(f"{date}: {count}")
