import datetime
d1 = datetime.date(2023, 1, 1)
d2 = datetime.date(2023, 12, 31)
diff = (d2 - d1).days
print(f"Разница: {diff} дней")  # 364
