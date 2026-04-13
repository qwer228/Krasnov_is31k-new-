from datetime import datetime

# Решение
dates_str = ["2026-10-05", "2024-01-15", "2025-05-20"]

dates_obj = [datetime.strptime(d, "%Y-%m-%d") for d in dates_str]
dates_obj.sort()

sorted_str = [d.strftime("%Y-%m-%d") for d in dates_obj]
print(f"Отсортированные даты: {sorted_str}")
