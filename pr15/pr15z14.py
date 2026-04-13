from datetime import datetime

# Решение
# Для проверки в коде заложена фиксированная дата
birth_input = "2000-01-01"
birth_date = datetime.strptime(birth_input, "%Y-%m-%d")

age_days = (datetime.now() - birth_date).days
print(f"Ваш возраст в днях: {age_days}")
