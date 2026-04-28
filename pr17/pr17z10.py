import datetime
today = datetime.date.today()
new_date = today + datetime.timedelta(days=7)
print(f"Через 7 дней: {new_date}")
