from datetime import datetime

# Решение
deadline_str = "2023-12-31"
deadline = datetime.strptime(deadline_str, "%Y-%m-%d")

if datetime.now() > deadline:
    print("Дедлайн просрочен!")
else:
    print("Время еще есть.")
