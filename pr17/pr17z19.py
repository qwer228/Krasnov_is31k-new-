import random, datetime
start_date = datetime.date(2024, 1, 1)
random_date = start_date + datetime.timedelta(days=random.randint(0, 365))
print(f"Случайная дата в 2024: {random_date}")
