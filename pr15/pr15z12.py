from datetime import datetime, timedelta

# Решение
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 1, 10)

start = min(date1, date2)
end = max(date1, date2)

workdays = 0
current = start

while current <= end:
    if current.weekday() < 5:  # 0-4 это Пн-Пт
        workdays += 1
    current += timedelta(days=1)

print(f"Количество рабочих дней: {workdays}")
