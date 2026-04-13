from datetime import datetime, timedelta

# Решение
target_date = datetime(2024, 5, 1) # Например, среда
days_ahead = 7 - target_date.weekday()

next_monday = target_date + timedelta(days=days_ahead)
print(f"Ближайший следующий понедельник: {next_monday.date()}")
