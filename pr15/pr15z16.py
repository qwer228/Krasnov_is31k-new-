from datetime import datetime

# Решение
dt = datetime(2024, 1, 1, 14, 30)

formatted_date = dt.strftime("%d %B %Y, %H:%M")
print(formatted_date)
