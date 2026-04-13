from datetime import datetime

# Решение
now = datetime.now()

# В timestamp
timestamp = now.timestamp()
print(f"UNIX timestamp: {timestamp}")

# Обратно в datetime
dt_back = datetime.fromtimestamp(timestamp)
print(f"Обратно в дату: {dt_back}")
