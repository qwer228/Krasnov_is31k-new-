from datetime import datetime

# Решение
date_str = "2024-12-31"
dt = datetime.strptime(date_str, "%Y-%m-%d")

print(f"День: {dt.day}")
print(f"Месяц: {dt.month}")
print(f"Год: {dt.year}")
